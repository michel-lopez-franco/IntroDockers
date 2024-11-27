FROM python:3.9-slim

WORKDIR /app
COPY script.py .

# ENTRYPOINT define el ejecutable
ENTRYPOINT ["python", "script.py"]

# CMD define los argumentos por defecto
CMD ["--mensaje", "Hola por defecto"]