FROM python:3.9-slim

# ARG se usa durante el build
ARG BUILD_VERSION=1.0

# ENV se puede modificar al ejecutar
ENV APP_ENV=development
ENV MESSAGE="Hola Mundo"

WORKDIR /app
COPY mi-app-parametro.py .

# Usar las variables
RUN echo "Version: $BUILD_VERSION" > version.txt

CMD ["python", "mi-app-parametro.py"]