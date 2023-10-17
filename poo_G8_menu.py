def validar_respuesta_menu(rtas):   #rtas es una lista de numeros
    rta= int(input("Ingrese opción deseada: "))
    while rta not in rtas:
        rta= int(input("Respuesta no válida, ingrese otra opción: "))
    return rta

def validar_usuario(archivo, dni, contraseña):
    #pensar cómo hacerlo, si con una matriz o desde el archivo, pero tenemos que ver el estatus de la persona para mostrar el menú correspondiente.
    # quiero que me devuelva si es cliente, empleado o gerente y el nombre
    pass


def menuPOO():
    print("Bienvenido al Hotel Patagonia Oasis y Ocio.")
    archivo_personas=""
    usuario=input("Ingrese su DNI: ")
    contraseña=input("Ingrese su contraseña: ")   # revisar como pedimos sus datos
    status,nombre_cliente=validar_usuario(archivo_personas,usuario,contraseña)
    print("Bienvenido", nombre_cliente, "al menpu interactivo del hotel POO.")
    if status == "cliente":
        validar_respuesta_menu([1,2,3])
        # acá va el menú cliente con sus opciones, lo hacemos acá o en una función aparte?
        pass
    elif status== "empleado":
        validar_respuesta_menu([1,2,3])
        # acá va el menú empleado con sus opciones, lo hacemos acá o en una función aparte?
        pass
    elif status== "gerente":
        validar_respuesta_menu([1,2])
        # acá va el menú gerente con sus opciones, lo hacemos acá o en una función aparte?
        pass

        














