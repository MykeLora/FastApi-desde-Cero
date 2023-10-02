from typing import Optional
from uuid import uuid4 as uuid

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
    producto.id(str(uuid))
    productos.append(producto)
    return {'Mensaje':'Prodcuto creado satifactoriamente.'}


@app.get('/producto/{id_producto}')
def obtener_producto_id(producto_id: str):
    for p in productos:
        if p.id == producto_id:
            return p

    return {'Mensaje' : f'El producto con el ID {producto_id} no existe.'}        