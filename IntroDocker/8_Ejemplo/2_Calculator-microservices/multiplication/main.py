from fastapi import FastAPI

app = FastAPI()

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}