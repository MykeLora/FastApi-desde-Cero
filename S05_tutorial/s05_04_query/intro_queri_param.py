from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {'Item_name': 'foo'},
    {"item_name": 'Bar'},
    {"item_name": "Baz"},
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]