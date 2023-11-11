from fastapi import FastAPI,Query

app = FastAPI()


@app.get('/items/')
async def read_items(q: str = Query(min_length=3,max_length=25)):
    results = {
        'items': [
            {'item_id': 'ABC'},
            {'item_id': 'XYZ'}
        ]
    }

    if q:
        results.update({'q': q})

    return results  