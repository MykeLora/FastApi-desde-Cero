from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        'json_schema_extra':{
            'examples': [
                {

                    'name': 'mause gamer',
                    'description': 'A very nice Item',
                    'price': 2500.4,
                    'tax': 150.2,
                }
            ]
        }
    }

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {
        'item_id': item_id,
        'item': item
    }
    return results
