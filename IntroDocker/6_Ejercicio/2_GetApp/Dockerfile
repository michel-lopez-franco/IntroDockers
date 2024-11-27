FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Check.py .

ENTRYPOINT ["python", "Check.py"]
CMD ["--hostname", "app-flask-hostname", "--name", "app-flask-name", "--port", "5000","--ip", "172.18.0.2","--op", "0"]