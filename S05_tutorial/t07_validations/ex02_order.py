from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/items/{item_id}/{price}')
async def read_items(
    q: str | None = Query(default=None, alias='item_id'),
    item_id: int = Path(title='The ID of the item to get'),
    price: float = Path(title='Price of the price')    
): 
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})

    return results    