### FAST API k8s

Este repositorio contiene la configuración necesaria para desplegar un microservicio basado en FastAPI a traves de Kubernetes.

------------

### Requisitos previos para desplegegue utilizando kubectl:

1. **Minikube**: Debes tener Minikube instalado en tu sistema. Encuentra las instrucciones de instalación en la documentación oficial.

2. **kubectl**: Debes tener kubectl instalado y configurado para comunicarte con el clúster de Minikube. Puedes instalarlo con gestores de paquetes como Homebrew (macOS) o apt-get (Debian/Ubuntu).

3. **Docker**: Necesitarás Docker para construir y etiquetar imágenes de contenedor. 

4. **Pipenv**: Instala Pipenv para gestionar las dependencias del proyecto Python.



### **Paso 1.0 Obtención de repositorio**
Clone este repositorio:
```bash
git clone git@ssh.dev.azure.com:v3/findepdev/Arquitectura/deployments-fastapi

```


## Estructura de Archivos y Directorios
```
.
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── app
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── deployer
│   ├── config.json
│   └── deployer.py
├── k8s
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── namespace.yaml
│   └── service.yaml
└── tests
    ├── __init__.py
    └── test_main.py

```

- `Dockerfile`: Instrucciones para construir una imagen Docker de la aplicación.
- `Pipfile`: Especifica las dependencias del proyecto para Pipenv.
- `Pipfile.lock`: Bloquea las versiones exactas de las dependencias.
- `README.md`: Documentación del proyecto en formato Markdown.
- `app/`: Código fuente de la aplicación (lógica, modelos, esquemas, etc.).
- `deployer/`: Archivos relacionados con el despliegue de la aplicación.
- `k8s/`: Archivos YAML para implementar la aplicación en Kubernetes.
- `tests/`: Archivos relacionados con las pruebas de la aplicación.

## Beneficios de la Estructura del Proyecto

- **Organización clara**: Facilita la navegación y comprensión del proyecto.
- **Estructura definida**: Establece una estructura clara y coherente en el proyecto.
- **Automatización simplificada**: Facilita la automatización de las pruebas y su ejecución continua.
- **Mantenimiento más sencillo**: Ayuda a mantener el código limpio y promueve buenas prácticas de desarrollo.
- **Fomento de pruebas unitarias**: Promueve el desarrollo de pruebas unitarias, fundamentales para garantizar la calidad del código.

## Pasos para Desplegar la Aplicación en Minikube


1. **Iniciar un nuevo clúster Minikube**:
   ```sh
   minikube start --driver=docker
   ```
   🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default


2. **Navegar al directorio con los archivos de Kubernetes**:
   ```sh
   cd k8s/
   ```

3. **Aplicar los recursos de Kubernetes**:
   ```sh
   kubectl apply -f .
   ```

4. **Verificar que los pods estén en funcionamiento**:
   ```sh
   kubectl get pods
   ```

5. **Resolver problemas de imagen del contenedor** (si es necesario):
   - Si obtienes errores de `ImagePullBackOff`, asegúrate de haber construido y etiquetado correctamente la imagen del contenedor.


6. **Acceder al servicio de la aplicación**:
   ```sh
   minikube service -n app-service fastapi-service --url
   ```

7. **Acceder a la aplicación**:
   Abre el navegador web y accede a la URL proporcionada. Por ejemplo: http://127.0.0.1:42477/docs

8. **Verificar el estado del clúster Minikube con el panel de control** (opcional):
   ```sh
   minikube dashboard
   ```

Con estos pasos, podrás desplegar tu aplicación en Minikube y verificar su funcionamiento en tu navegador. Si encuentras algún problema durante el proceso, asegúrate de revisar los mensajes de error y seguir las instrucciones de resolución proporcionadas.

## Solución a Problema de Carga de Imágenes en Minikube

Si te encuentras con problemas al cargar imágenes de Docker en Minikube, sigue estos pasos para resolverlos:

     ```
     kubectl get pods
     ```

     ```
     NAME                           READY   STATUS             RESTARTS   AGE
     fastapi-app-6445655967-56f9l   0/1     ImagePullBackOff   0          4m13s
     ```
      Normal   Scheduled  6m12s                  default-scheduler  Successfully assigned app-service/fastapi-app-6445655967-56f9l to minikube       
      Normal   Pulling    4m36s (x4 over 6m12s)  kubelet            Pulling image "app_service_deployer:1.2"
      Warning  Failed     4m35s (x4 over 6m11s)  kubelet            Failed to pull image "app_service_deployer:1.2": Error response from daemon: pull access denied for app_service_deployer, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
      Warning  Failed     4m35s (x4 over 6m11s)  kubelet            Error: ErrImagePull
      Warning  Failed     4m22s (x6 over 6m10s)  kubelet            Error: ImagePullBackOff
      Normal   BackOff    69s (x20 over 6m10s)   kubelet            Back-off pulling image "app_service_deployer:1.2"


1. **Configurar Minikube con Docker**:
   - Asegúrate de que tu entorno de Docker apunte correctamente al demonio de Docker de Minikube. Ejecuta el siguiente comando:
     ```sh
     eval $(minikube -p minikube docker-env)
     ```

2. **Reconstruir y Etiquetar la Imagen del Contenedor**:
   - Verifica que la imagen del contenedor esté construida correctamente y tenga la etiqueta adecuada. Puedes reconstruir y etiquetar la imagen con el siguiente comando:
     ```sh
     docker build -t app_service_deployer:1.2 .
     ```

3. **Aplicar la Configuración de Kubernetes**:
   - Despliega la aplicación en Minikube aplicando la configuración de Kubernetes:
     ```sh
     kubectl apply -f k8s/deployment.yaml
     ```

4. **Verificar el Estado de los Pods**:
   - Comprueba que los pods estén en funcionamiento y que la imagen del contenedor se haya cargado correctamente:
     ```sh
     kubectl get pods
     ```

5. **Acceder al Servicio de la Aplicación**:
   - Obtén la URL para acceder al servicio de la aplicación desplegada en Minikube con el siguiente comando:
     ```sh
     minikube service -n app-service fastapi-service --url
     ```
   - Abre un navegador web y accede a la URL proporcionada para ver tu aplicación en funcionamiento.

6. **Acceder a la Documentación de la API**:
   - Una vez que la aplicación esté en funcionamiento, puedes acceder a su documentación Swagger visitando la ruta `/docs`. Por ejemplo, si la URL del servicio es http://127.0.0.1:42477, puedes acceder a la documentación en http://127.0.0.1:42477/docs.

Una vez seguidos estos pasos, deberías poder cargar las imágenes de Docker en Minikube, acceder a la aplicación y consultar su documentación de API sin problemas.


## Solución a Problema No resources found in default namespace.

   ```
      kubectl config set-context --current --namespace=app-service
   ```









### ** Para ejecutar el proyecto solo con Docker:


Para construir la imagen Docker necesaria para tus servicios, utiliza el siguiente comando:


```bash
docker build -t app_service_deployer:1.2 .
```

### ** Para ejecutar las pruebas:

### ** Para ejecutar :



Para este ejemplo creo la imagen con el nombre deployment-service-example
```bash
docker build -t deployment-service-example .
```


### 3. Ejecutar el Proyecto

3.1. Con el entorno virtual activado y las dependencias instaladas, puedes ejecutar el proyecto utilizando el comando:

```bash 
     uvicorn app.main:app --reload 
```

### 4. Resultado

Running on http://127.0.0.1:8000 y al acceder enlace este debe mostrar el json de respuesta {"Hello":"World FastApi"}

Accede a este enlace para ver el Swagger -> http://127.0.0.1:8000/docs


## Ejecutar Test
```bash 
pytest
```


## Prisma 

```bash 

cd app/prisma


Next steps:
1. Set the DATABASE_URL in the .env file to point to your existing database. If your database has no tables yet, read https://pris.ly/d/getting-started
2. Set the provider of the datasource block in schema.prisma to match your database: postgresql, mysql, sqlite, sqlserver, mongodb or cockroachdb.
3. Run prisma db pull to turn your database schema into a Prisma schema.
4. Run prisma generate to generate the Prisma Client. You can then start querying your database.


npx prisma migrate dev --name init
```


alembic init alembic

