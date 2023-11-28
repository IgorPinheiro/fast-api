import requests

# Request type GET
# retorno = requests.get("http://127.0.0.1:8000")
# retorno = requests.get("http://127.0.0.1:8000/cadastro")

# Request type POST
retorno = requests.post("http://127.0.0.1:8000/user", params={'name': 'Igor Pinheiro'})


print(retorno.json())
# print(retorno.json()['mensagem'])

