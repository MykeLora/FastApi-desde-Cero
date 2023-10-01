from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

class producto(BaseModel):
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


@app.get('/producto')
def obtener_productos():
    return productos

@app.post('/producto')
def crear_producto(producto : producto):
    productos.append(producto)
    return {'Mensaje':'Prodcuto creado satifactoriamente.'}