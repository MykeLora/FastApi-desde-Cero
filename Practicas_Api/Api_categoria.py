from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI,HTTPException

from uuid import uuid4 as uuid 

class Category(BaseModel):
    id : Optional[str]
    nombre : str
    esActivo : bool 
    fechaRegistro : str

app = FastAPI()

categorias = []

@app.get('/')
def index():
    return{'Mensaje': 'Bienvenidos a la API de categoria'}

@app.get('/category')
def obtener_categoria():
    return categorias

@app.post('/category')
def crear_categoria(categoria : Category):
    categoria_id = str(uuid())
    categoria.id = categoria_id
    categorias.append(categoria)

    return {'Mensaje':'Categoria creada satisfatoriamente.'}

@app.get('/category/{categoria_id}')
def obtener_categoria_por_id(categoria_id : str):
    resultado = list(filter(lambda c:c.id == categoria_id,categorias))

    if(len(resultado)):
        return resultado[0]
    
    raise HTTPException(status_code=404,detail=f"La categoria con el id {categoria_id} no existe.")

@app.delete('/category/{categoria_id}')
def eliminar_categoria_por_id(categoria_id : str):
    resultado = list(filter(lambda c:c.id == categoria_id,categorias))

    if(len(categorias)):
        categoria = resultado[0]
        categorias.remove(categoria)

        return {'Mensaje':'La categoria ha sido eliminada satisfatoriamente.'}

    raise HTTPException(status_code=404,detail=f'La categoria con el ID {categoria_id} no existe.')


@app.put('/category/{categoria_id}')
def actualizar_categoria_por_id(categoria_id : str, categoria: Category):
    respuesta = list(filter(lambda p:p.id == categoria_id,categorias))

    if len(respuesta):
        categoria_buscada = respuesta[0]
        categoria_buscada.nombre = categoria.nombre
        categoria_buscada.esActivo = categoria.esActivo
        categoria_buscada.fecha_registro = categoria.fecha_registro

        return categoria_buscada
    
    raise HTTPException(status_code=404,detail=f'El producto con el ID {categoria_id} no existe')



