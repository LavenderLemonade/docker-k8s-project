# fetch_pokemon.py
import requests

def main():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/absol")
    print(response.json()["name"])

if __name__ == "__main__":
    main()
