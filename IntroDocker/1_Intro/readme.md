

# Construir la imagen
```bash
docker build -t mi-app .
```

# Ejecutar el contenedor
```bash
docker run -d -p 5000:5000 mi-app
```

# Ejecutar el contenedor y entrar
```bash
docker run -it mi-app sh
```

# Ejecutar el contenedor y entrar puerto 5000
```bash
docker run -it -p 5000:5000 mi-app sh
```
    
   
# Borrar todos los contenedores 
```bash
docker ps -a -q | xargs docker rm    
```