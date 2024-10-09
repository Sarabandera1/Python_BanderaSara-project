# #   4. Los tres mejores jugadores
#     5. El jugador en el último puesto
#     6. Los jugadores que más han perdido contra la máquina
#     7. Ver el promedio de jugadores que han ganado a la máquina

def estadisticas():
    puntajes = cargar_puntajes()
    print("\n*** Estadísticas del Juego ***")
    
    print("\nPuntajes de los jugadores:")
    if puntajes["players"]:
        for player in puntajes["players"]:
            print(f"Jugador: {player['name']}, Ganó: {player['wins']} veces")
    else:
        print("No hay puntajes registrados para los jugadores.")

    print("\nPuntajes de la máquina:")
    if "machine" in puntajes and puntajes["machine"]["wins"] > 0:
        print(f"La máquina ganó: {puntajes['machine']['wins']} veces")
    else:
        print("No hay puntajes registrados para la máquina.")

    input('\nPresione una tecla para volver al menú')
