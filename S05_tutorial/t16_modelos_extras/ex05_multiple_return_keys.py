from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/keyword-weights/", response_model=dict[str, float])
async def read_keyword_weights():
    return {'foo': 2.3, 'bar': 3.4}