import json
import os

def cargar_puntajes():
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r") as archivo:
            return json.load(archivo)
    else:
        return {"players": [], "machine": {"wins": 0}}  


def guardar_puntajes(puntajes):
    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo, indent=4)

{
    "players": [
        {"name": "Juan Pérez", "nickname": "JPerez", "wins": 3},
        {"name": "María López", "nickname": "MLopez", "wins": 2}
    ],
    "machine": {"wins": 5}
}
