from fastapi import FastAPI, Form

app = FastAPI()

@app.post('/post/')
async def login(username: str = Form(), password: str = Form()):
    return {'Username': username}