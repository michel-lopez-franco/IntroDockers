

# Usando **ARG** (en tiempo de construcción) y **ENV** (en tiempo de ejecución):

```bash
docker build -t mi-app-parametro:v0.0.1 .
```

## 1. Pasar variables de entorno al ejecutar
```bash
docker run -e MESSAGE="Hola desde Docker" mi-app-parametro:v0.0.1

docker run -e MESSAGE="Hola desde Docker" -e APP_ENV="Build" mi-app-parametro:v0.0.1
```

## 2. Usar command override (sobrescribir CMD)
```bash
docker run mi-app-parametro:v0.0.1 python mi-app-parametro.py --mensaje "Hola"
```

## 3. Pasar argumentos de construcción
```bash
docker build --build-arg BUILD_VERSION=2.0 -t mi-app-parametro:v0.0.1 .
```