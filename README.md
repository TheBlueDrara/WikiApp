Welcome to my CI/CD project.

About:

In this project, I've created a small web wiki app that is connected to a stateful database using MongoDB and the Flask library.
Everything runs on a local Kubernetes cluster I've created using Kind and Docker Desktop.
Using Helm tools and charts, I've deployed tools and services for the process, such as Jenkins, ArgoCD, and monitoring tools like Grafana and Prometheus.

As part of the CI process, I've coded some testing code that tests the pushed code before it sends a merge request.

So, I have a CI/CD flow that every time a developer pushes code to GitHub, it starts a CI process that builds an environment for testing, and if all the tests are passed, it sends a merge request.

After the merge request is accepted, the pipeline continues. It creates an image and pushes it to Docker Hub.
Then ArgoCD pulls the new artifact from Docker Hub and deploys it using my configurations.

By using Prometheus, I've created some alerts to see that all the replicas are running smoothly and not overloaded. If they are overloaded, then an alert will be shown.
Everything is monitored using Grafana.




How to run the app:

To run the app locally, make sure you have MongoDB, ShibariWiki, test_app Python files, and the Docker Compose YAML file in the same directory.
And make sure you have Docker Desktop installed on your machine if youre using Windows.

Run the next command to build the environment:

** docker-compose up --build -d **

![image](https://github.com/TheBlueDrara/WikiApp/assets/143508761/76ca4ad0-8d75-48eb-99f9-50d263676425)


If you want to see if the tests passed or failed, use this command to read the test container's log:

** docker-compose logs test **

![image](https://github.com/TheBlueDrara/WikiApp/assets/143508761/d3338e3e-2f8d-4ba5-9c0a-4aebe11c4a0b)


If everything is correct, you should be able to go to your webpage and access the wiki by typing localhost:5000 in the web search bar.

![image](https://github.com/TheBlueDrara/WikiApp/assets/143508761/907a84ec-b703-41cd-b048-1fe073afcfd0)

About the App:

You can add new items to the database.
You can see info about every technique.
You can use the filter option by entering the amount of resources you have to search for available techniques you can use.
Alternatively, you can delete items from the list.

Enjoy!
