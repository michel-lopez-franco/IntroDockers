# Crear una red para una aplicación web y su base de datos

```bash
docker network ls
```

```bash
docker network create app-network
```

## Ejecutar MySQL en la red
```bash
docker run --name db --network app-network mysql
```

## Ejecutar aplicación web en la misma red
```bash
docker run --network app-network mi-aplicacion
```

# Ejemplo

```bash
docker network ls

docker network create mi-red-python

docker build -t mi-app-python-web .
╰─ docker build -t mi-app-python-web:v0.0.1 .

docker run -d --network mi-red-python -p 5000:5000 mi-app-python-web 

docker run -it -p 5000:5000 mi-app-python-web bash
```

Para ver el registro
```bash
docker logs --tail=100 923035971f04
```