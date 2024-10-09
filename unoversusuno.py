from puntajes import cargar_puntajes, guardar_puntajes

def registrar_jugador(nicknames_registrados):
    nombre = input("Ingrese su nombre completo: ")
    while True:
        nickname = input("Ingrese su nickname: ")
        if nickname in nicknames_registrados:
            print("Nickname ocupado, ingrese otro.")
        else:
            nicknames_registrados.add(nickname)
            return {"name": nombre, "nickname": nickname, "wins": 0}

def unoversusuno():
 
    puntajes = cargar_puntajes()
    nicknames_registrados = {player['nickname'] for player in puntajes['players']}
    
    print("Registro de Jugador 1:")
    jugador1 = registrar_jugador(nicknames_registrados)
    
    print("Registro de Jugador 2:")
    jugador2 = registrar_jugador(nicknames_registrados)

    while True:
        print(f"\n{jugador1['nickname']} vs {jugador2['nickname']}")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")
        print("------------------------")
        
        opcion1 = input(f"{jugador1['nickname']}, ingrese una opción: ")
        opcion2 = input(f"{jugador2['nickname']}, ingrese una opción: ")

        if opcion1 == "1":
            jugador1_opcion = "Piedra"
        elif opcion1 == "2":
            jugador1_opcion = "Papel"
        elif opcion1 == "3":
            jugador1_opcion = "Tijera"
        else:
            print("Opción inválida")
            continue

        if opcion2 == "1":
            jugador2_opcion = "Piedra"
        elif opcion2 == "2":
            jugador2_opcion = "Papel"
        elif opcion2 == "3":
            jugador2_opcion = "Tijera"
        else:
            print("Opción inválida")
            continue

        print(f"\n{jugador1['nickname']} eligió: {jugador1_opcion}")
        print(f"{jugador2['nickname']} eligió: {jugador2_opcion}\n")

   
        if jugador1_opcion == jugador2_opcion:
            print("Empate")
        elif (jugador1_opcion == "Piedra" and jugador2_opcion == "Tijera") or (jugador1_opcion == "Papel" and jugador2_opcion == "Piedra") or (jugador1_opcion == "Tijera" and jugador2_opcion == "Papel"):
            print(f"-- {jugador1['nickname']} ganó esta ronda --")
            jugador1['wins'] += 1
        else:
            print(f"-- {jugador2['nickname']} ganó esta ronda --")
            jugador2['wins'] += 1

     
        print(f"\n*** Marcador Actual ***")
        print(f"{jugador1['nickname']} ha ganado {jugador1['wins']} veces.")
        print(f"{jugador2['nickname']} ha ganado {jugador2['wins']} veces.")
        
    
        continuar = input("¿Desean jugar otra ronda? (s/n): ")
        if continuar.lower() != 's':
            
            puntajes['players'].append(jugador1)
            puntajes['players'].append(jugador2)
            guardar_puntajes(puntajes)
            break
