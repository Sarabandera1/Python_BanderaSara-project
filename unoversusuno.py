from puntajes import cargar_puntajes, guardar_puntajes

def solicitar_info_jugador(nicknames_usados):
    nombre_completo = input("Ingrese su nombre completo: ")
    while True:
        nickname = input("Ingrese su nickname: ")
        if nickname in nicknames_usados:
            print("Nickname ocupado, ingrese otro.")
        else:
            return {"name": nombre_completo, "nickname": nickname}

def unoversusuno():
    puntajes = cargar_puntajes()

    print("Juego con otro jugador")
    
    nicknames_usados = [player["nickname"] for player in puntajes["players"]]
    jugador1 = solicitar_info_jugador(nicknames_usados)
    jugador2 = solicitar_info_jugador(nicknames_usados)

    print(f"{jugador1['nickname']} vs {jugador2['nickname']}")

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

    print(f"\n{jugador1['nickname']} eligió: {jugador1_move}")
    print(f"{jugador2['nickname']} eligió: {jugador2_move}\n")

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "Piedra" and jugador2 == "Tijera") or (jugador1 == "Papel" and jugador2 == "Piedra") or (jugador1 == "Tijera" and jugador2 == "Papel"):
        print("--Jugador 1 ganó--")
   
    else:
        print(f"--{jugador2['nickname']} ganó--")
        registrar_puntaje(puntajes, jugador2["nickname"])
    mostrar_marcador(puntajes)


    guardar_puntajes(puntajes)

def registrar_puntaje(puntajes, nickname):
    for player in puntajes["players"]:
        if player["nickname"] == nickname:
            player["wins"] += 1
            return

    puntajes["players"].append({"nickname": nickname, "wins": 1})

def mostrar_marcador(puntajes):
    print("\n*** Marcador Actual ***")
    for player in puntajes["players"]:
        print(f"{player['nickname']}: {player['wins']} victorias")
    print("------------------------")
