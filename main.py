from typing import Union
from fastapi import FastAPI



from models.item_model import Item



App = FastAPI()

@App.get("/")
def read_root():
    return {'Hello': 'World!!!'}

@App.get("/hola")
def Presentandome():
    return {'Desarrollador': 'Maycol Lora!!'}

@App.get('/items/{item_id}')
def read_item(item_id: int, q:Union[str,None]= None):
    return {'item_id': item_id,'q':q}

@App.get('/calculadora')
def Suma(num_1: int,num_2:int):
    return {'Suma': num_1 + num_2} 

@App.get('/multiplicadora')
def multiplicar(num_1: float, num_2: float):
    resultado = num_1 * num_2
    return {'Multiplicación': resultado}

@App.put("/items/{items_id}")
def update_item(item_id: int,item:Item):
    return{"item_name":item.name,"item_id":item_id,"item_prise":item.price}