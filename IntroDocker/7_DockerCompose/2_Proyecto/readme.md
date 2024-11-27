


# ubicacion de archivos


```markdonw
proyecto/
├── .devcontainer/
│   ├── Dockerfile.dev         # Aquí
│   └── devcontainer.json
├── src/
├── requirements.txt
└── Dockerfile                 # Dockerfile de producción
```


# 1. Abre VS Code en la carpeta del proyecto
code .

# 2. Presiona F1 y escribe:
"Remote-Containers: Open Folder in Container"

# 3. VS Code reconstruirá y abrirá el entorno de desarrollo

# En la terminal de VS Code
python src/app.py


# Verificar conexión con Redis
redis-cli -h redis ping

# Ver las claves en Redis
redis-cli -h redis keys *

# Ver el valor del contador
redis-cli -h redis get visits


# Script para construir para producción:

```bash
#!/bin/bash
# build.sh
docker build -t myapp:prod -f Dockerfile .
docker tag myapp:prod registry.example.com/myapp:prod
docker push registry.example.com/myapp:prod
```