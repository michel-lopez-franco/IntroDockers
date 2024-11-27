FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Set up the network
ENV NETWORK_NAME mi-red-python
ENV FLASK_RUN_PORT 5000

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]