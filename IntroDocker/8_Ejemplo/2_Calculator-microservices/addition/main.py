from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}