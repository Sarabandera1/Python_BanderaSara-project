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
        print("--------Empate---------")
    elif (jugador == "Piedra" and maquina == "Tijera") or (jugador == "Papel" and maquina == "Piedra") or (jugador == "Tijera" and maquina == "Papel"):
        print("--------Ganaste---------")
    else:
        print("--------Perdiste---------")