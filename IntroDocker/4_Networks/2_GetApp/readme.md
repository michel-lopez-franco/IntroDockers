

# Ejemplo

```bash
docker build -t mi-app-check:v0.0.1 .

docker run -d --network mi-red-python mi-app-check:v0.0.1

docker run -it --network mi-red-python mi-app-check:v0.0.1 bash
```

Para ver el registro
```bash
docker logs --tail=100 923035971f04

docker attach a6994138409a
```

# Prueba la conectividad
```bash
docker exec CONTAINER_ID ping otro-servicio
```