from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.6


items = {
    "foo": {"name": "Foo", "price": 55.5},
    "bar":{
        "name": "Bar", "description": "The bartenders",
        "price": 75, "tax": 20.5 
    },
    "baz":{
        "name": "Bar", "description": None,
        "price": 85.3, "tax": 10.5
    }
}    

@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"}
)
async def read_item_name(item_id: str):
    return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]





