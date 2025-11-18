from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "API funcionando!"}

@app.post("/somar")
def somar(a: float, b: float):
    return {"resultado": a + b}

@app.get("/usuario/{user_id}")
def usuario(user_id: int):
    return {"usuario": user_id, "nome": "Fulano de Tal"}
