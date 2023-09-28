from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return{'Mensaje': 'Bienvenidos a la API de productos'}


