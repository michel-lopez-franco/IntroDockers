#!/bin/bash
# build.sh
# chmod +x build.sh
# ./build.sh

#docker network ls | grep -w calc-network > /dev/null 2>&1 || docker network create calc-network
#docker-compose -f ../2_Calculator-microservices/docker-compose.yaml -f ./docker-compose.yaml up 
#docker-compose -f ../2_Calculator-microservices/docker-compose.yaml up --build -d
#docker-compose -f ./docker-compose.yaml up --build -d



set -e  # Terminar si ocurre un error

# Crear la red si no existe
docker network ls | grep -w calc-network > /dev/null 2>&1 || docker network create calc-network

# Obtener rutas absolutas
CURRENT_DIR=$(dirname "$(realpath "$0")")
MICROSERVICES_DIR="$CURRENT_DIR/../2_Calculator-microservices"

# Ejecutar Docker Compose para los microservicios
echo "Levantando servicios básicos..."
docker-compose -f "$MICROSERVICES_DIR/docker-compose.yaml" up --build -d

# Esperar a que los servicios estén listos
echo "Esperando 10 segundos para que los servicios iniciales estén listos..."
sleep 10

# Ejecutar Docker Compose para el servicio de calculadora
echo "Levantando servicio de calculadora..."
docker-compose -f "$CURRENT_DIR/docker-compose.yaml" up --build -d
