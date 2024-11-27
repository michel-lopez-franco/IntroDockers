

# Ejemplo

```bash
docker build -t mi-app-check:v0.1.1 .

docker run -d --network mi-red-python mi-app-check:v0.1.1

docker run -it --network mi-red-python mi-app-check:v0.1.1 bash
```


# Haciendo pruebas
```bash
docker run mi-app-check:v0.1.1 

#si
docker run mi-app-check:v0.1.1 --ip 172.17.0.2

# NO 
docker run mi-app-check:v0.1.1 --hostname "mi-host-flask" --op 1
docker run mi-app-check:v0.1.1 --hostname "mi-host-flask" --op 3

docker run mi-app-check:v0.1.1 --name "mi-flask" --op 2
docker run mi-app-check:v0.1.1 --name "mi-flask" --op 4
```


## Ejecutar aplicación web en la misma red
```bash
# SI
docker run --network mi-red-python mi-app-check:v0.1.1

# NO
docker run --network mi-red-python mi-app-check:v0.1.1 --hostname "mi-host-flask" --op 1
```


# Entrar al contenedor
```bash
docker exec -it contenedor2 bash
```