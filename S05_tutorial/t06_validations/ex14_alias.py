from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/items')
async def read_items(q: str | None = Query(default=None, alias='item-query')):
    results = {
        'items': [
            {'item_id': 'ABC'},
            {'item_id': 'DEF'}
        ]
    }

    if results:
        results.update({'q': q})
    return results    
                     