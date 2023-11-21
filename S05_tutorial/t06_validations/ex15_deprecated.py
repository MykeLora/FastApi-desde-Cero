from fastapi import FastAPI,Query

app = FastAPI()


@app.get('/items')
async def read_items(
    q: str | None = Query(
        default= None,
        alias= 'item-query',
        title= 'Query string',
        description= 'Query string for the items to search in the database that have a good match',
        min_length= 3,
        max_digits= 50,
        pattern= '^fixedquery$',
        deprecated= True,
    ),

):
    results = {
        'items':[
            {'item_id': 'ABC'},
            {'item_id': 'EFG'} 
        ]
    }

    if q:
        results.update({'q': q})

    return results    