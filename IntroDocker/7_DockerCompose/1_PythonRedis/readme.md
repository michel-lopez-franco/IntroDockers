


# Con solo Dockerfile:
docker build -t miapp .
docker run -d miapp
docker run -d redis

# Tendrías que configurar redes y conexiones manualmente

# Con Docker Compose:
docker-compose up -d
# Configura todo automáticamente



docker-compose down