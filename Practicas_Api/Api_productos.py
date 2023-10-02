from typing import Optional
from uuid import uuid4 as uuid 

from fastapi import FastAPI,HTTPException
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
    producto_id = str(uuid())
    producto.id = producto_id
    productos.append(producto)
    return {'Mensaje':'Prodcuto creado satifactoriamente.'}




@app.get('/producto/{id_producto}')
def obtener_producto_id(producto_id: str):
    respuesta = list(filter(lambda p:p.id == producto_id,productos))
    

    if len(respuesta):
        return respuesta[0]

    raise HTTPException(status_code=404,detail=f'El producto con el ID {producto_id} no existe.')

        