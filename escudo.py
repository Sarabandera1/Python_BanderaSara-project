import json

def cargarEscudo(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"jugadores_list": []}

def guardarEscudo(filename, puntuaciones):
    with open(filename, 'w') as file:
        json.dump(puntuaciones, file, indent=4)

def aplicar_escudo(jugador_index, puntuaciones):
    escudo_usado = False
    jugador = puntuaciones["jugadores_list"][jugador_index]
    if jugador["escudos"] > 0:
        jugador["escudos"] -= 1
        escudo_usado = True
    return puntuaciones, escudo_usado

def verificar_escudo(jugador_index, won, puntuaciones):
    jugador = puntuaciones["jugadores_list"][jugador_index]
    if won:
        jugador["ganadas_consecutivas"] += 1
        if jugador["ganadas_consecutivas"] >= 2:
            jugador["escudos"] += 1 
    else:
        jugador["ganadas_consecutivas"] = 0  
    return puntuaciones

