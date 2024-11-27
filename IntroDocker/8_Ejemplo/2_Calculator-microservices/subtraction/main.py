from fastapi import FastAPI

app = FastAPI()

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}