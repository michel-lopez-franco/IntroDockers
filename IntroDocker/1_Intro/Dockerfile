# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los requisitos de la aplicación
COPY requirements.txt .

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]