# Etapa de construcción
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Etapa final
FROM python:3.9-slim

WORKDIR /app

# Copiar solo lo necesario
COPY --from=builder /app/wheels /wheels
COPY . .

# Instalar dependencias
RUN pip install --no-cache /wheels/*

# Usuario no root para seguridad
RUN useradd -m appuser
USER appuser

# Comando para producción
CMD ["gunicorn", "app:app"]