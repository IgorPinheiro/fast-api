from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Create an APP
app = FastAPI()

# list with an tuple
users = [(1, 'Joao', 'minha_Senha'),(2, 'Carlos', 'minha _enha'),(3, 'Andreia', 'My_pass')]

@app.post('/user')
def main(name):
    return {'name': name}







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