from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class productos(BaseModel):
    id : Optional[str]
    nombre : str
    precio_compra : float
    precio_venta : float
    proveedor : str

app = FastAPI()

productos = []

@app.get('/')
def index():
    return{'Mensaje': 'Bienvenidos a la API de productos'}


