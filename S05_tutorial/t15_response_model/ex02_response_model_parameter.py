from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get('/items/',response_model=list[Item])
async def read_items() -> Any:
    return [
        {'name': 'Mause gamer', 'price': 1500.5},
        {'name': 'Monitor gamer', 'price': 3500.5},
        {'name': 'Tablet Amazon', 'price': 4000.5},
        {'name': 'Cpu gamer', 'price': 35000.5},
        {'name': 'Proyector hp', 'price': 2000.5},
    ]
    
