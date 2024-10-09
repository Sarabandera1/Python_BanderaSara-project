def addUsuario (data):
        nombre=input("ingrese su nombre: ")
        apellido=input("ingrese su apellido: ")
        apodo=input("ingrese su apodo: ")

        userValidator = False

        for element in data:
                if element['apodo'] == apodo:
                        userValidator=True
while (addUsuario):
        os.system('clear')
        diccionario={
                jugador={
                "nombre":nombre,
                "apellido": apellido,
                "apodo": apodo
            }
        }       
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
