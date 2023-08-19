from fastapi import FastAPI
from typing import Union

App = FastAPI()

@App.get("/")

def read_root():
    return {'Hello': 'World!'}

@App.get("/hola")
def Presentandome():
    return {'Desarrollador': 'Maycol Lora'}

@App.get('/items/{item_id}')
def read_item(item_id: int, q:Union[str,None]= None):
    return {'item_id': item_id,'q':q}