from typing import Annotated

from fastapi import Cookie, FastAPI


app = FastAPI()

@app.get('/items/')
async def read_items(
    ads_id: str = Cookie(None, description="ID de anuncio en formato de cadena")
):
    return {'ads_id': ads_id}