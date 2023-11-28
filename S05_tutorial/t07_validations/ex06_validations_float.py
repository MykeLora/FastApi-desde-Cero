from fastapi import FastAPI, Path, Query

app =FastAPI()


@app.get('/items/{item_id}')
async def read_item(
    *,
    item_id: int = Path(title='The ID of the item to get', ge=0, le=100),
    q: str,
    size: float = Query(gt=0, le=10.5, alias= 'Query-item'),

):
    results = {'item_id': item_id}

    if q:
        results.update({'q': q})

    return results    