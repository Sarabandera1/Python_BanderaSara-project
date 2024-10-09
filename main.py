import json
import os
from puntajes import cargar_puntajes, guardar_puntajes
from unoversusuno import *
from unoversusm import *
from escudo import cargarEscudo, guardarEscudo, aplicar_escudo, verificar_escudo
from estadisticas import *


def cargar_puntajes():
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r") as archivo:
            return json.load(archivo)
    else:
        return {"players": [], "machine": []} 


def guardar_puntajes(puntajes):
    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo, indent=4)

def estadisticas():
    puntajes = cargar_puntajes()
    print("\n*** Estadísticas del Juego ***")
    
    # Mostrar los puntajes de los jugadores
    print("\nPuntajes de los jugadores:")
    for player in puntajes["players"]:
        # Verifica que el jugador tenga las claves 'name' y 'wins'
        if 'name' in player and 'wins' in player:
            print(f"Jugador: {player['name']}, Ganó: {player['wins']} veces")
        else:
            print("Jugador con datos incompletos.")

    # Mostrar los puntajes de la máquina
    print("\nPuntajes de la máquina:")
    print(f"La máquina ganó: {puntajes['machine']['wins']} veces" if puntajes['machine'] else "No hay puntajes registrados para la máquina.")

def menu():
    while True:
        print( """ 
    ******************* The Chachipun ******************* 
        ¡Bienvenido al juego de Piedra, Papel o Tijera!
    *****************************************************
    
    Menú Principal:
    1. Jugar Uno versus Uno
    2. Jugar Uno versus Máquina
    3. Ver estadísticas del juego
    8. Salir
    
    *****************************************************
    """)
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            unoversusuno()
        elif opcion == 2:
            unoversusm()
        elif opcion == 3:
            estadisticas()
        elif opcion == 8:
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()
