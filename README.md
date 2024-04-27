WikiApp

Welcome to my CI/CD project.

In this project, I've created a small web wiki app that is connected to a stateful database using MongoDB and the Flask library.
Everything runs on a local Kubernetes cluster I've created using Kind and Docker Desktop.
Using Helm tools and charts, I've deployed tools and services for the process, such as Jenkins, ArgoCD, and monitoring tools like Grafana and Prometheus.

As part of the CI process, I've coded some testing code that tests the pushed code before it sends a merge request.

So, I have a CI/CD flow that every time a developer pushes code to GitHub, it starts a CI process that builds an environment for testing, and if all the tests are passed, it sends a merge request.

After the merge request is accepted, the pipeline continues. It creates an image and pushes it to Docker Hub.
Then ArgoCD pulls the new artifact from Docker Hub and deploys it using my configurations.

By using Prometheus, I've created some alerts to see that all the replicas are running smoothly and not overloaded. If they are overloaded, then an alert will be shown.
Everything is monitored using Grafana.

How to run the app?

To run the app locally, make sure you have MongoDB, ShibariWiki, test_app Python files, and the Docker Compose YAML file in the same directory.
And make sure you have kubectl installed on your machine.

Run the next command to build the environment:

** docker-compose up --build -d **

If you want to see if the tests passed or failed, use this command to read the test container's log:

** docker-compose logs test **

If everything is correct, you should be able to go to your webpage and access the wiki by typing localhost:5000 in the web search bar.