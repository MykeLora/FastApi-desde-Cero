from fastapi import FastAPI
from typing import Union

App = FastAPI()

@App.get("/")

def read_root():
    return {'Hello': 'World!'}

@App.get("/hola")
def Presentandome():
    return {'Desarrollador': 'Maycol Lora'}