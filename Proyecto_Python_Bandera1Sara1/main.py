import json
import os
import modules.unoversusuno as unu
import modules.unoversusm as um



def cargar_puntajes():
    if os.path.exists("puntajes.json"):
        with open("puntajes.json", "r") as archivo:
            return json.load(archivo)
    else:
        return []

def guardar_puntajes(puntajes):
    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo, indent=4)

def mostrar_menu():
    menu = """ 
    ******************* The Chachipun ******************* 
        ¡Bienvenido al juego de Piedra, Papel o Tijera!
    *****************************************************
    
    Menú Principal:
    1. Jugar Uno versus Uno
    2. Jugar Uno versus Máquina
    3. Ver estadísticas del juego
    8. Salir
    
    ***************************************************************
    """
    print(menu)

def main():
    puntajes = cargar_puntajes()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            unoversusuno(puntajes)
        elif opcion == "2":
            unoversusm(puntajes)
        elif opcion == "3":
            estadisticas(puntajes)
        elif opcion == "8":
            print("Gracias por jugar. ¡Hasta luego!")
            guardar_puntajes(puntajes)
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def unoversusuno(puntajes):
    print("Iniciando juego Uno versus Uno")

def unoversusm(puntajes):
    print("Iniciando juego Uno versus Máquina")
    

def estadisticas(puntajes):
    print("Mostrando estadísticas del juego")
   
if __name__ == "__main__":
    main()

