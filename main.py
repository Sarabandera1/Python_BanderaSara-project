import json
import os
from unoversusuno import *
from unoversusm import *

def cargar_puntajes():
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r") as archivo:
            return json.load(archivo)
    else:
        return []

def guardar_puntajes(puntajes):
    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo, indent=4)

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
