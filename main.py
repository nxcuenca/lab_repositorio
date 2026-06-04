from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hola_mundo():
    return {"mesagge":"Hola Equipo"}

@app.get("/")
def root_endpoint():
    return {"mesagge":"Bienvenido a mi API - LAB"}

@app.get("/suma")
def sumar(a:int, b:int):
    resultado = a + b
    return {"resultado": resultado}