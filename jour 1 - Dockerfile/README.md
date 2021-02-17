### Build de l'application

docker build . -t deploy_flask


sudo docker run -p 5000:5000 deploy_flask:latest
