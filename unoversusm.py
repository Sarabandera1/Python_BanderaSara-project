import random
from puntajes import cargar_puntajes, guardar_puntajes  

def unoversusm():
    print("Juego con la máquina")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("---------------------")

    opcion = int(input("Ingrese una opción: "))
    
    jugador=True
    if opcion == 1:
        jugador = "Piedra"
    elif opcion == 2:
        jugador = "Papel"
    elif opcion == 3:
        jugador = "Tijera"
    else:
        print("-----------------")
        print(type(opcion))
        print("-----------------")
        print(jugador)
        print("------------------")
        print("Opción inválida")
        return unoversusm()

    maquina = random.choice(["Piedra", "Papel", "Tijera"])

    print(f"\nTú elegiste: {jugador}")
    print(f"Máquina elegió: {maquina}\n")

    resultado = ""

    if jugador == maquina:
        print("--------Empate---------")
    elif (jugador == "Piedra" and maquina == "Tijera") or (jugador == "Papel" and maquina == "Piedra") or (jugador == "Tijera" and maquina == "Papel"):
        print("--------Ganaste---------")
        
    else:
        print("--------Perdiste---------")

    puntajes = cargar_puntajes()
    


    if resultado == "Ganaste":
        if not puntajes["players"]:
            puntajes["players"].append({"name": "Jugador", "wins": 1})
        else:
            puntajes["players"][0]["wins"] += 1
    elif resultado == "Perdiste":
        if not puntajes["machine"]:
            puntajes["machine"] = {"wins": 1}
        else:
            puntajes["machine"]["wins"] += 1

    guardar_puntajes(puntajes)

    input('Presione una tecla para continuar')