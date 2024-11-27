FROM python:3.9-slim

ENV APP_ENV=development
WORKDIR /app
COPY script.py .

ENTRYPOINT ["python", "script.py"]
CMD ["--env", "development", "--mensaje", "Hola por defecto"]