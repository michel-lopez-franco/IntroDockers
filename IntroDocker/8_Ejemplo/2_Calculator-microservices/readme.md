

```bash
docker-compose up --build
```


Puedes probar cada operación directamente desde un navegador o usar herramientas como curl o Postman:


```bash
curl "http://localhost:8001/add?a=5&b=3"
curl "http://localhost:8002/subtract?a=5&b=3"
curl "http://localhost:8003/multiply?a=5&b=3"
curl "http://localhost:8004/divide?a=6&b=3"
```