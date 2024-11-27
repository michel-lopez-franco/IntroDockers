


```bash
docker build -t mi-app-flask:v0.0.1 .
```

# Con valores por defecto
```bash
docker run mi-app-flask:v0.0.1
```

# Sobrescribir argumentos
```bash
docker run mi-app-flask:v0.0.1 --hostname "0.0.0.0" --name "mi-super-flask" --port 5001
```

# Combinar con variables de entorno
```bash
docker run -e FLASK_RUN_PORT=5002 mi-app-flask:v0.0.1 --name "mi-super-flask2"
```


# Asignando un nombre
```bash
docker run --name mi-flask mi-app-flask:v0.0.1
```

## Ejecutar aplicación web en la misma red
```bash
docker run --network mi-red-python mi-app-flask:v0.0.1
```