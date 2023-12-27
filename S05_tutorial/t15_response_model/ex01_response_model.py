from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post('/items')
async def create_item(item: Item) -> Item:
    return item

@app.get('/items')
async def read_items() -> list[Item]:
    return [
        Item(name='Mause gamer', price=2000.33),
        Item(name='Monitor gamer', price=3500.60),
        Item
    ]
