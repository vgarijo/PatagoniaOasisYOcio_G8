def pedirUsuario():
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    print("")
    return usuario, contrasena

def validar_respuesta_menu(rta):
    rtas=range(1, rta+1)
    rta= int(input("Ingrese la opción deseada: "))
    while rta not in rtas:
        rta= int(input("Respuesta no valida, ingrese otra opcion: "))
    print("")
    return rta

def menuPOO():
    print("Bienvenido al Hotel Patagonia Oasis y Ocio.")
    print("¿A qué menu desea ingresar?")
    print("1. Menu de cliente")
    print("2. Menu de empleado")
    print("3. Menu de gerente")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        usuario,contrasena=pedirUsuario()
        menu_cliente()
    elif rta == 2:
        usuario,contrasena=pedirUsuario()
        menu_empleado()
    elif rta == 3:
        usuario,contrasena=pedirUsuario()
        menu_gerente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu cliente
def menu_cliente(): 
    print("Bienvenido al menu de cliente")
    print("¿Qué desea hacer?")
    print("1. Mis Reservas")
    print("2. Mis Consumos")
    print("3. Datos Personales")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(5)
    if rta == 1:
        menu_reservas()
    elif rta == 2:
        menu_consumos()
    elif rta == 3:
        menu_datos_personales()
    elif rta == 4:
        menuPOO()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu Reservas
def menu_reservas():
    print("Mis reservas")
    print("¿Qué desea hacer?")
    print("1. Historial de Reservas")
    print("2. Nueva Reserva")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        menu_historial_reservas()
    elif rta == 2:
        menu_nueva_reserva()
        pass
    elif rta == 3:
        menu_cliente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_historial_reservas():
    print("Historial de reservas")
    print("¿Qué desea hacer?")
    print("1. Reserva Actual")
    print("2. Visualizar Reservas Anteriores")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        menu_reserva_actual()
    elif rta == 2:
        menu_reservas_anteriores()
        pass
    elif rta == 3:
        menu_reservas()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_reservas_anteriores():
    print("Reservas anteriores")
    print("¿Qué desea hacer?")
    print("1. Atrás")
    print("2. Salir")
    rta = validar_respuesta_menu(2)
    if rta == 1:
        menu_historial_reservas()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

def menu_nueva_reserva():
    print("Nueva reserva")
    print("¿Qué desea hacer?")
    print("1. Atrás")
    print("2. Salir")
    rta = validar_respuesta_menu(2)
    if rta == 1:
        menu_reservas()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

def menu_reserva_actual():
    reserva_actual = None
    if reserva_actual == None:
        print("No tiene una reserva actual")
        print("¿Qué desea hacer?")
        print("1. Volver atras")
        print("2. Salir")
        rta = validar_respuesta_menu(2)
        if rta == 1:
            menu_historial_reservas()
        
    else:
        print("Reserva actual")
        print("¿Qué desea hacer?")
        print("1. Ver Reserva")
        print("2. Modificar Reserva")
        print("3. Cancelar Reserva")
        print("4. Check In")
        print("5. Check Out")
        print("6. Volver atras")
        print("7. Salir")
        rta = validar_respuesta_menu(7)
        if rta == 1:
            print("")
            # método para ver reserva actual
            pass
        elif rta == 2:
            print("")
            # método para modificar reserva actual
            pass
        elif rta == 3:
            print("")
            # método para cancelar reserva actual
            pass
        elif rta == 4:
            print("")
            # método para hacer check in
            pass
        elif rta == 5:
            print("")
            # método para hacer check out
            pass
        elif rta == 6:
            menu_historial_reservas()
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()

    print("")

def menu_consumos():
    print("Consumos")
    print("¿Qué desea hacer?")
    print("1. Historial de Consumos")
    print("2. Nuevo Consumo")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        # método para visualizar historial de consumos
        pass
    elif rta == 2:
        # método para hacer un nuevo consumo
        pass
    elif rta == 3:
        menu_cliente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_datos_personales():
    print("Personales")
    print("¿Qué desea hacer?")
    print("1. Ver Datos Personales")
    print("2. Modificar Datos Personales")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        # método para ver datos personales
        pass
    elif rta == 2:
        # método para modificar datos personales
        pass
    elif rta == 3:
        menu_cliente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")


def menu_empleado():
    print("")

def menu_gerente():
    print("")


menuPOO()
