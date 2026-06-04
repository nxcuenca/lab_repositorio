from fastapi import FastAPI
from config import settings

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

@app.get("/resta")
def resta(a:int, b:int):
    resultado = a - b
    return {"resultado": resultado}

@app.get("/multiplicacion")
def multiplicacion(a:int, b:int):
    resultado = a * b
    return {"resultado": resultado}

@app.get("/division")
def division(a:int, b:int):
    resultado = a / b
    return {"resultado": resultado}