#!/bin/bash
# build.sh
#chmod +x build.sh
docker build -t myapp:prod -f Dockerfile .
docker tag myapp:prod registry.example.com/myapp:prod
docker push registry.example.com/myapp:prod