import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/absol")
print(response.json()["name"])