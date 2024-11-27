

# Generar una Imagen desde un Contenedor ya Ejecutado

Para generar una imagen desde un contenedor ya ejecutado, sigue estos pasos:

1. **Ejecuta el contenedor anterior**:
    ```bash
    docker run -it -p 5000:5000 mi-app bash
    ```
1. **Añade un archivo nuevo**:
    
    ```bash
    touch suma.py
    echo 'print("Hola Mundo desde suma") >> suma.py'
    cat suma.py
    ```

1. **Lista de los contenedores ocultos**:
   
    ```bash
    docker ps -a --latest
    ```

1. **Lista los contenedores en ejecución**:
    ```bash
    docker ps
    ```

2. **Obtén el ID del contenedor** que deseas convertir en una imagen.

3. **Crea la imagen** usando el comando `docker commit`:
    ```bash
    docker commit <container_id> <new_image_name>
    ```

    Reemplaza `<container_id>` con el ID del contenedor y `<new_image_name>` con el nombre que deseas darle a la nueva imagen.

4. **Verifica que la imagen ha sido creada**:
    ```bash
    docker images
    ```

    Deberías ver `<new_image_name>` en la lista de imágenes disponibles.

## Ejemplo

Supongamos que tienes un contenedor en ejecución con el ID `abc123` y deseas crear una imagen llamada `mi_nueva_imagen`.

1. Lista los contenedores en ejecución:
    ```bash
    docker ps
    ```

2. Crea la imagen:
    ```bash
    docker commit abc123 mi_nueva_imagen
    ```

3. Verifica que la imagen ha sido creada:
    ```bash
    docker images
    ```

    Deberías ver `mi_nueva_imagen` en la lista de imágenes disponibles.

¡Y eso es todo! Ahora has creado una nueva imagen desde un contenedor ya ejecutado.

4. **Ejecutar la nueva imagen**


    ```bash
    docker run -it mi-app:v0.0.1 bash
    ```
1. **Verifica el contenido**

    ```bash
    ls
    cat suma.py
    python suma.py
    ```