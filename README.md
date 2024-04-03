# k8s, microservice Fastapi

Solo Python 3.8+ estándar.


## Instalación

Para instalar este proyecto, sigue estos pasos:

1. Clona este repositorio:

    ```
    git clone https://github.com/tu_usuario/tu_proyecto.git
    ```

2. Instala las dependencias utilizando pipenv:

    ```
    pipenv install
    ```

## Uso

Para ejecutar el proyecto, sigue estos pasos:

1. Activa el entorno virtual:

    ```
    pipenv shell
    ```

2. Ejecuta el servidor:

    ```
    uvicorn app.main:app --reload
    ```

3. Ahora ve a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) en tu navegador para acceder a la documentación interactiva de la API.

## Documentación

Puedes encontrar más detalles sobre cómo interactuar con la API en la documentación interactiva. [Haz clic aquí para acceder](http://127.0.0.1:8000/docs).


## Documentación

docker build -t app_service_deployer:1.2 .
docker run -d -p 80:80 app_service_deployer:1.2

minikube start --driver=docker

Minikube configurará automáticamente tu entorno de Docker para que apunte al demonio de Docker de Minikube.
eval $(minikube -p minikube docker-env -u)

alias kubectl="minikube kubectl --"
cd k8s/
kubectl apply -f .
kubectl config set-context --current --namespace=<nombre-del-namespace>
kubectl config set-context --current --namespace=c
kubectl get pods
docker build -t app_service_deployer:1.2 .
kubectl apply -f  k8s/deployment.yaml 
kubectl get pods    
kubectl  delete pods --all
kubectl delete deployments --all
kubectl get services

NAME              TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
fastapi-service   NodePort   10.109.154.191   <none>        80:31053/TCP   9m36s


minikube status
minikube tunnel
kubectl get ingress fastapi-ingress -n app-service
minikube service -n app-service fastapi-service --url
