from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(
        examples=['mause']
    )
    description: str | None = Field( 
        default=None,examples=['A very nice Item ']
    )
    price: float = Field(examples=[1500.8])
    tax: float | None = Field(default=None, examples=[150.6])

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {
        'item_id': item_id,
        'item': item
    }

    return results