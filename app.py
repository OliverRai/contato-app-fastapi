from fastapi import FastAPI

from model import Contato

app = FastAPI()

@app.get("/api/v1/{id}")
async def get_contato(id: int):
    return {1: {
        "nome":"Raiane"
    }}

@app.post("/api/v1/")
async def get_contato(contato: Contato):
    return contato

@app.put("/api/v1/{id}")
async def update_contato(contato: Contato):
    return contato