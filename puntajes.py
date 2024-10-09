import json
import os

# Cargar los puntajes desde el archivo JSON
def cargar_puntajes():
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r") as archivo:
            return json.load(archivo)
    else:
        return {"players": [], "machine": {"wins": 0}}  # Inicializar con estructura correcta

# Guardar los puntajes en el archivo JSON
def guardar_puntajes(puntajes):
    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo, indent=4)
