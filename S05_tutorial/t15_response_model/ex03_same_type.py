from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

@app.post('/user')
async def create_user(user: UserIn) -> UserIn:
    return user


    
