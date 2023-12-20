from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get('/items/')
async def read_items(
    strange_header: Annotated[str | None, Header(
        convert_underscores=False)
    ] = None
):
    return {'strnge_header': strange_header}
