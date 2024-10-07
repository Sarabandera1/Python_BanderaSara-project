import os
import modules.unoversusm as mq
import modules.unoversusuno as unu
import random

def main():
    menuprincipal = """ ******************* The Cachipun ******************* 
                      Bienvenido al juego de Piedra, Papel o Tijera
                    ****************************************************

Menú
1. Jugar con la máquina
2. Jugar con otro jugador
3. Salir
""" 
def juego_con_otro_jugador(): 
    while True:
        print("---------Menú---------")
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

def addUsuario (data):

        nombre=input("ingrese su nombre: ")
        apellido=input("ingrese su apellido: ")
        apodo=input("ingrese su apodo: ")

        userValidator = False

        for element in data:
                if element['apodo'] == apodo:
                        userValidator=True


        if(userValidator==True):
                print('Este nombre esta en uso')
        else:
                nuevoJugador={
                        "nombre":nombre,
                        "apellido":apellido,
                        "apodo":apodo
                }
                data.append(nuevoJugador)
        return data