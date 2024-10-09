
def unoversusuno():
    print("Juego con otro jugador")
    print("Jugador 1")      
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("------------------------")

    opcion1 = input("Ingrese una opción: ")

    if opcion1 == "1":
        jugador1 = "Piedra"
    elif opcion1 == "2":
        jugador1 = "Papel"
    elif opcion1 == "3":
        jugador1 = "Tijera"
    else:
        print("Opción inválida")
        return unoversusuno()

    print("Jugador 2")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("------------------------")

    opcion2 = input("Ingrese una opción: ")

    if opcion2 == "1":
        jugador2 = "Piedra"
    elif opcion2 == "2":
        jugador2 = "Papel"
    elif opcion2 == "3":
        jugador2 = "Tijera"
    else:
        print("Opción inválida")
        return unoversusuno()

    print(f"\nJugador 1 elegió: {jugador1}")
    print(f"Jugador 2 elegió: {jugador2}\n")

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Papel" and jugador2 == "Piedra") or (jugador1 == "Tijera" and jugador2 == "Papel"):
        print("--Jugador 1 ganó--")
    else:
        print("--Jugador 2 ganó--")
