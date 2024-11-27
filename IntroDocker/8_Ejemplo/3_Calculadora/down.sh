#!/bin/bash
# build.sh
# chmod +x build.sh
# ./build.sh

set -e  # Terminar si ocurre un error

# Crear la red si no existe
docker network ls | grep -w calc-network > /dev/null 2>&1 

# Obtener rutas absolutas
CURRENT_DIR=$(dirname "$(realpath "$0")")
MICROSERVICES_DIR="$CURRENT_DIR/../2_Calculator-microservices"

# Ejecutar Docker Compose para los microservicios
echo "Deteniendo servicios básicos..."
docker-compose -f "$MICROSERVICES_DIR/docker-compose.yaml" down

# Esperar a que los servicios estén listos
echo "Esperando 10 segundos para que los servicios iniciales estén detenidos..."
sleep 10

# Ejecutar Docker Compose para el servicio de calculadora
echo "Deteniendo servicio de calculadora..."
docker-compose -f "$CURRENT_DIR/docker-compose.yaml" down
