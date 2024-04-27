pipeline {
    agent {
        kubernetes {
            label 'ez-joy-friends'
            idleMinutes 5
            yamlFile 'build-pod.yaml'
            defaultContainer 'ez-docker-helm-build'
        }
    }

    environment {
        // GITLAB_URL = 'https://gitlab.com/sela-tracks/1101/alex/alex_shibariwiki_proj.git'
        GITLAB_URL = 'https://gitlab.com'
        MONGODB_URI = 'mongodb://mongo:27017/MyDataBase'
        PROJECT_ID = '55375725'
        IMAGE_NAME = 'thebluedrara/wikiapp' // Replace with your desired image name
        GITLAB_CREDENTIALS_ID = credentials('jenkins-cred')
        DOCKER_HUB_CREDENTIALS_ID = credentials('docker-cred')

    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    // Build Docker image
                    dockerImage = docker.build("${IMAGE_NAME}:latest", "--no-cache .")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yaml up -d'
                    sh 'docker-compose -f docker-compose.yaml run test pytest'
                    sh 'docker-compose -f docker-compose.yaml down'
                }
            }
        }

        stage('Create Merge Request') {
            when {
                not {
                    branch 'main'
                }
            }
            steps {
                script {
                    withCredentials([string(credentialsId: 'soony0737', variable: 'GITLAB_API_TOKEN')]) {
                        def response = sh(script: """
                        curl -s -o response.json -w "%{http_code}" --header "PRIVATE-TOKEN: ${GITLAB_API_TOKEN}" -X POST "${GITLAB_URL}/api/v4/projects/${PROJECT_ID}/merge_requests" \
                        --form "source_branch=${env.BRANCH_NAME}" \
                        --form "target_branch=main" \
                        --form "title=MR from ${env.BRANCH_NAME} into main" \
                        --form "remove_source_branch=true"
                        """, returnStdout: true).trim()
                        if (response.startsWith("20")) {
                            echo "Merge request created successfully."
                        } else {
                            echo "Failed to create merge request. Response Code: ${response}"
                            def jsonResponse = readJSON file: 'response.json'
                            echo "Error message: ${jsonResponse.message}"
                            error "Merge request creation failed."
                        }
                    }
                }
            }
        }

        stage('Push Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Push Docker image to registry
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-cred') {
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }
}
