from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Create an APP
app = FastAPI()

# Object User to integration with pydantci.
class User(BaseModel):
    id: int
    name: str
    password: str

@app.post('/user')
def main(user: User):
    return user







# Create a logic to get the user by name.
# @app.post('/usuario')
# def main(nome):
#     for i in usuarios:
#         if i[1] == nome:
#             return i
#     return 'User do not exist'


# Rquest type GET

# @app.get('/usuario/{id}')
# def main(id: int):
#     for i in usuarios:
#         if i[0] == id:
#             return i
#     return 'User do not exist'