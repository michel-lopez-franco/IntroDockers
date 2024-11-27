

# Opción 1: Combinar los archivos docker-compose.yml

Si combinas ambos archivos en uno, docker-compose podrá manejar todos los servicios sin problema. El archivo combinado podría verse así:


```yaml
version: "3.8"

services:
  addition:
    build:
      context: ./addition
    ports:
      - "8001:8000"
    networks:
      - calc-network

  subtraction:
    build:
      context: ./subtraction
    ports:
      - "8002:8000"
    networks:
      - calc-network

  multiplication:
    build:
      context: ./multiplication
    ports:
      - "8003:8000"
    networks:
      - calc-network

  division:
    build:
      context: ./division
    ports:
      - "8004:8000"
    networks:
      - calc-network

  calculator:
    depends_on:
      - addition
      - subtraction
      - multiplication
      - division
    build:
      context: ./calculator
    ports:
      - "8000:8000"
    networks:
      - calc-network

networks:
  calc-network:
    driver: bridge

```


Luego puedes levantar todos los servicios con:

```bash
docker-compose up --build
```

# Opción 2: Usar múltiples archivos docker-compose

Si prefieres mantener los archivos separados, puedes usar el comando docker-compose para combinarlos al momento de ejecutarlos. Usa la opción -f para especificar ambos archivos:


```bash
docker-compose -f path/to/docker-compose-1.yml -f path/to/docker-compose-2.yml up --build

```


# Opción 3: Usar una red externa compartida

Si prefieres mantener completamente separados los archivos y levantar los servicios independientemente, puedes configurar una red externa en ambos archivos.

Levanta los servicios básicos (addition, subtraction, etc.): Actualiza el primer archivo para usar una red externa:

```yaml
version: "3.8"

services:
  addition:
    build:
      context: ./addition
    ports:
      - "8001:8000"
    networks:
      - calc-network

  subtraction:
    build:
      context: ./subtraction
    ports:
      - "8002:8000"
    networks:
      - calc-network

  multiplication:
    build:
      context: ./multiplication
    ports:
      - "8003:8000"
    networks:
      - calc-network

  division:
    build:
      context: ./division
    ports:
      - "8004:8000"
    networks:
      - calc-network

networks:
  calc-network:
    external: true

```

Levanta el servicio calculator: Actualiza el segundo archivo para usar la misma red externa:

```yaml
version: "3.8"

services:
  calculator:
    build:
      context: ./calculator
    ports:
      - "8000:8000"
    networks:
      - calc-network

networks:
  calc-network:
    external: true

```
Crear la red compartida manualmente: Antes de ejecutar los servicios, crea la red externa con este comando:

```bash
docker network create calc-network
```
Levanta los servicios: Primero, levanta los servicios básicos:

```bash
docker-compose -f path/to/docker-compose-1.yml up --build -d

```
Luego, levanta el servicio calculator:
```bash
docker-compose -f path/to/docker-compose-2.yml up --build -d

```

# ¿Cuál es la mejor opción?

- Si no tienes necesidad de mantener los archivos separados, la Opción 1 (combinar los archivos) es la más sencilla.
- Si necesitas mantener los archivos separados para modularidad o trabajo en equipo, la Opción 2 (múltiples archivos) es ideal.
- Si planeas ejecutar servicios independientemente, la Opción 3 (red externa compartida) es más flexible.


# construir un archivo sh

```bash
#!/bin/bash
# build.sh
# chmod +x build.sh
# ./build.sh
```

## Ejecutar servicios
```bash
./build.sh
curl "http://localhost:8000/add?a=5&b=3"
```
## Detener servicios
```bash
./down.sh
curl "http://localhost:8000/add?a=5&b=3"
```


# Ejecutar manualmente 

```bash
docker network ls | grep -w calc-network > /dev/null 2>&1 || docker network create calc-network
#docker-compose -f ../2_Calculator-microservices/docker-compose.yaml -f ./docker-compose.yaml up 
docker-compose -f ../2_Calculator-microservices/docker-compose.yaml up --build -d
docker-compose -f ./docker-compose.yaml up --build -d
```

```bash
docker-compose -f ./docker-compose.yaml down 
docker-compose -f ../2_Calculator-microservices/docker-compose.yaml down
```


# PORT vs EXPOSE

Si deseas que los puertos de los servicios solo sean accesibles dentro de la red calc-network y no desde el exterior, puedes omitir la configuración de ports en los servicios y usar solo expose. Esto permite que los contenedores sean accesibles únicamente por otros contenedores dentro de la misma red.

```yaml
expose:
  - "8000"
```

```yaml
ports:
  - "8004:8000"
```