from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# Base URLs de los servicios
services = {
    "add": "http://addition:8000/add",
    "subtract": "http://subtraction:8000/subtract",
    "multiply": "http://multiplication:8000/multiply",
    "divide": "http://division:8000/divide"
}

@app.get("/{operation}")
async def calculate(operation: str, a: float, b: float):
    # Verifica si la operación es válida
    print("-"*50)
    print(f"Operation: {operation}")
    print(f"a: {a}")
    print(f"b: {b}")
    print("-"*50)
    if operation not in services:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose from: add, subtract, multiply, divide")
    
    # Realiza la solicitud al servicio correspondiente
    async with httpx.AsyncClient() as client:
        response = await client.get(services[operation], params={"a": a, "b": b})
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    return response.json()
