from fastapi import FastAPI
from config import settings

app = FastAPI()

SECRET_KEY = settings.clave_secreta.get_secret_value()

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

@app.get("/clave-secreta")
def obtener_clave_secreta():
    return {"clave": SECRET_KEY}

@app.get("/titulo-api")
def titulo_api():
    return {"titulo": settings.title_api}