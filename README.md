# Flask App Kubernetes Deployment

This project demonstrates deploying a Flask application in a Kubernetes environment. The Flask app exposes an API at `/ip`, returning the IP address of the running pod. The setup includes multiple layers of load balancing and ensures high availability and scalability using Kubernetes, an Ingress controller, and an NGINX reverse proxy. Deployment is automated through a CI/CD pipeline.

## Prerequisites

- Docker
- Kubernetes Cluster with `kubectl` access
- Jenkins for CI/CD
- GitHub PAT (Personal Access Token) for repo access
- DockerHub account for pushing images

## Project Structure

flask-k8s-app/ ├── app │ ├── app.py # Flask app returning pod IP │ ├── Dockerfile # Dockerfile for Flask app │ ├── requirements.txt # Dependencies ├── k8s │ ├── deployment.yaml # Flask app Deployment │ ├── service.yaml # LoadBalancer Service │ ├── ingress.yaml # Ingress resource │ ├── nginx-deployment.yaml # NGINX reverse proxy Deployment │ ├── nginx-service.yaml # NGINX LoadBalancer Service │ ── ci │ ├── Jenkinsfile # CI/CD pipeline ├── README.md # Project documentation


## Flask Application

### Running Locally

1. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
Start the Flask app:
```bash
python app/app.py
Access at http://localhost:5000/ip.
```

Dockerization
Build the Docker image:
```
docker build -t your-dockerhub-username/flask-app:latest -f app/Dockerfile .
```
Kubernetes Deployment
Deploy the Application
Apply the manifests to deploy the app:
```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
Set up Ingress:
```
kubectl apply -f k8s/ingress.yaml
```
Deploy NGINX as a reverse proxy:
```
kubectl apply -f k8s/nginx-deployment.yaml
kubectl apply -f k8s/nginx-service.yaml
kubectl apply -f k8s/nginx-configmap.yaml
```

CI/CD Pipeline
The Jenkins pipeline automates:

Cloning the repo from GitHub using a PAT.
Building and testing the Docker image.
Pushing the image to DockerHub.
Deploying the app to Kubernetes.
Jenkins Setup
Add GitHub PAT as github-pat in Jenkins credentials.
Add DockerHub credentials as docker-credentials.
To run the pipeline, the Jenkinsfile is in the ci/ directory.

Accessing the Application
Via Kubernetes LoadBalancer: Use the external IP of the Service.
Via Ingress: Access through the Ingress controller.
Via NGINX Reverse Proxy: Access through NGINX, which forwards requests to the Flask app.
