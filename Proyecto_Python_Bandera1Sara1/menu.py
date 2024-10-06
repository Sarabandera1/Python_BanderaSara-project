import os
import modules.unoversusm as mk
menuprincipal = """ ******************* The Cachipun ******************* 
                      Bienvenido al juego de Piedra, Papel o Tijera
                    ****************************************************

Menú
1. Jugar con la máquina
2. Jugar con otro jugador
3. Salir
"""
import random

def juego_con_maquina():
    print("Juego con la máquina")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        jugador = "Piedra"
    elif opcion == "2":
        jugador = "Papel"
    elif opcion == "3":
        jugador = "Tijera"
    else:
        print("Opción inválida")
        return juego_con_maquina()

    maquina = random.choice(["Piedra", "Papel", "Tijera"])

    print(f"\nTú elegiste: {jugador}")
    print(f"Máquina elegió: {maquina}\n")

    if jugador == maquina:
        print("*******************Empate******************* ")
    elif (jugador == "Piedra" and maquina == "Tijera") or (jugador == "Papel" and maquina == "Piedra") or (jugador == "Tijera" and maquina == "Papel"):
        print("*******************Ganaste*******************")
    else:
        print("*******************Perdiste*******************")


def juego_con_otro_jugador():
    print("Juego con otro jugador")
    print("Jugador 1")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcion1 = input("Ingrese una opción: ")

    if opcion1 == "1":
        jugador1 = "Piedra"
    elif opcion1 == "2":
        jugador1 = "Papel"
    elif opcion1 == "3":
        jugador1 = "Tijera"
    else:
        print("Opción inválida")
        return juego_con_otro_jugador()

    print("Jugador 2")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    opcion2 = input("Ingrese una opción: ")

    if opcion2 == "1":
        jugador2 = "Piedra"
    elif opcion2 == "2":
        jugador2 = "Papel"
    elif opcion2 == "3":
        jugador2 = "Tijera"
    else:
        print("Opción inválida")
        return juego_con_otro_jugador()

    print(f"\nJugador 1 elegió: {jugador1}")
    print(f"Jugador 2 elegió: {jugador2}\n")

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Papel" and jugador2 == "Piedra") or (jugador1 == "Tijera" and jugador2 == "Papel"):
        print("Jugador 1 ganó")
    else:
        print("Jugador 2 ganó")


def main():
    while True:
        print("Menú")
        print("1. Jugar con la máquina")
        print("2. Jugar con otro jugador")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            juego_con_maquina()
        elif opcion == "2":
            juego_con_otro_jugador()
        elif opcion == "3":
            print("Adiós")
            break
        else:
            print("Opción inválida")
            
if __name__ == "__main__":
    main()