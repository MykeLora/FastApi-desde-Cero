from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get('/items')
async def read_items(
    x_token: Annotated[list[str] | None, Header()] = None
):
    return {'X_Token values': x_token}
