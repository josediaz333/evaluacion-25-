#evaluacion parcial 25%

usuarios = {}


def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    while nombre in usuarios:
        print("Usuario ya existe. Intente otro.")
        nombre = input("Ingrese nombre de usuario: ")
    sexo = input("Ingrese sexo (M/F): ")
    while sexo != "M" and sexo != "F":
        print("Debe ingresar M o F solamente.")
        sexo = input("Ingrese sexo (M/F): ")
    while True:
        contraseña = input("Ingrese contraseña: ")
        if len(contraseña) >= 8
            print("Contraseña válida.")
            break
        else:
            print("Contraseña no válida. Intente otra.")
    usuarios[nombre] = [sexo, contraseña]
    print("Usuario ingresado con éxito!!\n")
def buscar_usuario():
    nombre = input("Ingrese usuario a buscar: ")
    if nombre in usuarios:
        print("El sexo del usuario es:", usuarios[nombre], "y la contraseña es:", usuarios[nombre], "\n")
    else:
        print("El usuario no se encuentra.\n")
def eliminar_usuario():
    nombre = input("Ingrese usuario a buscar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado con éxito!\n")
    else:
        print("No se pudo eliminar usuario!\n")
while True:
    print("MENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!\n")
       