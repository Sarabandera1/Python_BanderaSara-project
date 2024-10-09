import random
from puntajes import cargar_puntajes, guardar_puntajes  

# Función para jugar contra la máquina
def unoversusm():
    print("Juego con la máquina")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("---------------------")

    opcion = int(input("Ingrese una opción: "))
    
    jugador=True
    # Variable que almacenará la elección del jugador
    # Asigna el valor adecuado a 'jugador' según la opción seleccionada
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
     # Si la opción es inválida, muestra un mensaje y vuelve a solicitar la opción

 # La máquina elige aleatoriamente entre Piedra, Papel o Tijera
    maquina = random.choice(["Piedra", "Papel", "Tijera"])

# Muestra las selecciones tanto del jugador como de la máquina
    print(f"\nTú elegiste: {jugador}")
    print(f"Máquina elegió: {maquina}\n")

    resultado = "" # Variable para almacenar el resultado del juego

# Determina el resultado del juego
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