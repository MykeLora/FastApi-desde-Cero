from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id = int 
    name = 'Maycol Lora Caceres'
    signup_ts : datetime | None = None
    friends: list[int] = []

#Desde el exterior podriamos recibir estos datos
external_data = {
    'id': 1002,
    'signup_ts': '2023-9-26 14:10',
    'friends': [1003,10004,1005]
}    
user = User(**external_data)
print(user)
print(user.id)