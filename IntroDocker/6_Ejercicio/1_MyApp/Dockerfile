FROM python:3.11-slim

ARG PORT=5000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV NETWORK_NAME mi-red-python
ENV FLASK_RUN_PORT $PORT

COPY app.py .

EXPOSE $PORT

ENTRYPOINT ["python", "app.py"]
CMD ["--hostname", "0.0.0.0", "--name", "app-flask", "--port", "5000"]







