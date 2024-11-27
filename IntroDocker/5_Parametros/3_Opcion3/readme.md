

```bash
docker build -t mi-app-parametro3:v0.0.1 .
```

# Con valores por defecto
```bash
docker run mi-app-parametro3:v0.0.1
```

# Sobrescribir argumentos
```bash
docker run mi-app-parametro3:v0.0.1 --env production --mensaje "Hola Prod"
```

# Combinar con variables de entorno
```bash
docker run -e APP_ENV=staging mi-app-parametro3:v0.0.1 --mensaje "Hola Staging"
```