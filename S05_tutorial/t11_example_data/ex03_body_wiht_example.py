from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    'name': 'Mause gamer',
                    'description': 'A very nice Item',
                    'price': 1800.5,
                    'tax': 140.3,

                }
            ],
        ),
    ],
):
    results = {
        'item_id': item_id,
        'item': item
    }  
    return results  