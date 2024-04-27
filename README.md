# WikiApp
welcome to my CI/CD project.

In this project ive created a small web wiki app that is connected to a statefull state Database using MongoDb and Flask Library.
everything runs on a local kubernetes cluster ive created using Kind and Docker Desktop.
using Helm tools and charts ive deployed tools and services and for the process sach as Jenkins, ArgoCD, and monitoring tools like Garfana and Promethues.
part of the CI process ive coded some testing code that tests the pushed code before it sends a merge request.

so i have a CI\CD flow that everytime a developer pushes code to github, it starts a CI process that builds an eviroment for testing, and if all the tests are passed it sends a merge request.

after the merge request is accpeted the pipeline contiues. it crates an image and pushes it to Dockerhub.
than ArgoCD pulls the new artifact from Dockerhub and deploys it using my configurations.

by using Promethuers ive created some alerts to see that all the replicas are running smothly and not overloaded, and if so than an alert will be shown.
everything is monitored using Garfana.



How to run the app?

to run the app localy make sure to have to MongoDB, ShibariWiki, test_app python files, and Docker-compose yaml file in the same directory.
and make sure you have kubectl installed on your machine.

run the command 
docoker-compose --build -d 