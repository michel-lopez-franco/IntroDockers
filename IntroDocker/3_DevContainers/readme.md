

# **Añadir un archivo de configuracion**
presiona ctrl+shift p 

```bash
> add dev container
```

# **Dev Containers: Reopen in Container**
presiona ctrl+shift p 

```bash
> reopen in container
```

# **Desde una terminal verificar los archivos**

```bash
> docker ps -a --latest
```
copiamos su **CONTAINER ID**
```bash
> docker start <ContainerID>
```

ejecutamos el contenedor con su **CONTAINER ID**
```bash
> docker exec -it <ContainerID> bash
```

Buscamos los archivos:
```bash
> ls
> whoami
> cd workspaces
> cd 3_DevContainers
> cat main.py
```


TODO: docker commit contaiderID mi-app:v0.0.2