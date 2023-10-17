def pedirUsuario():
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    return usuario, contrasena

def validar_respuesta_menu(rta):
    rtas=range(1, rta+1)
    rta= int(input("Ingrese la opción deseada: "))
    while rta not in rtas:
        rta= int(input("Respuesta no valida, ingrese otra opcion: "))
    return rta

def validar_persona(archivo, usuario, contrasena):
    with open(archivo, "r") as file:
        for line in file:
            if usuario in line and contrasena in line:
                return True 
        return False

def menuPOO(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("Bienvenido al Hotel Patagonia Oasis y Ocio.")
    print("¿A qué menu desea ingresar?")
    print("1. Menu de cliente")
    print("2. Menu de empleado")
    print("3. Menu de gerente")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        usuario,contrasena=pedirUsuario()
        validar_persona(archivo_clientes, usuario, contrasena)
        if validar_persona(archivo_clientes, usuario, contrasena):
            menu_cliente()
        else:
            print("Usuario o contraseña incorrectos")
            menuPOO(archivo_clientes, archivo_empleados, archivo_gerentes)

    elif rta == 2:
        usuario,contrasena=pedirUsuario()
        validar_persona(archivo_empleados, usuario, contrasena)
        if validar_persona(archivo_empleados, usuario, contrasena):
            menu_empleado()
        else:
            print("Usuario o contraseña incorrectos")
            menuPOO(archivo_clientes, archivo_empleados, archivo_gerentes)

    elif rta == 3:
        usuario,contrasena=pedirUsuario()
        validar_persona(archivo_gerentes, usuario, contrasena)
        if validar_persona(archivo_gerentes, usuario, contrasena):
            menu_gerente()
        else:
            print("Usuario o contraseña incorrectos")
            menuPOO(archivo_clientes, archivo_empleados, archivo_gerentes)

    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()


def menu_cliente(archivo_clientes, archivo_empleados, archivo_gerentes): 
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
        menuPOO(archivo_clientes, archivo_empleados, archivo_gerentes)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_reservas(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("Bienvenido al menu de reservas")
    print("¿Qué desea hacer?")
    print("1. Historial de Reservas")
    print("2. Nueva Reserva")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        menu_historial_reservas()
    elif rta == 2:
        # método para hacer una nueva reserva en cliente y agregarlo a un archivo de reservas
    elif rta == 3:
        menu_cliente(archivo_clientes, archivo_empleados, archivo_gerentes)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_historial_reservas(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("Bienvenido al menu de historial de reservas")
    print("¿Qué desea hacer?")
    print("1. Reserva Actual")
    print("2. Visualizar Reservas Anteriores")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        menu_reserva_actual()
    elif rta == 2:
        # método para ver historial de reservas
    elif rta == 3:
        menu_reservas(archivo_clientes, archivo_empleados, archivo_gerentes)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_reserva_actual(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("Bienvenido al menu de reserva actual")
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
        # método para ver reserva actual
    elif rta == 2:
        # método para modificar reserva actual
    elif rta == 3:
        # método para cancelar reserva actual
    elif rta == 4:
        # método para hacer check in
    elif rta == 5:
        # método para hacer check out
    elif rta == 6:
        menu_historial_reservas(archivo_clientes, archivo_empleados, archivo_gerentes)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_consumos(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("Bienvenido al menu de consumos")
    print("¿Qué desea hacer?")
    print("1. Historial de Consumos")
    print("2. Nuevo Consumo")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        # método para visualizar historial de consumos
    elif rta == 2:
        # método para hacer un nuevo consumo
    elif rta == 3:
        menu_cliente(archivo_clientes, archivo_empleados, archivo_gerentes)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_datos_personales(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("Bienvenido al menu de datos personales")
    print("¿Qué desea hacer?")
    print("1. Ver Datos Personales")
    print("2. Modificar Datos Personales")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        # método para ver datos personales
    elif rta == 2:
        # método para modificar datos personales
    elif rta == 3:
        menu_cliente(archivo_clientes, archivo_empleados, archivo_gerentes)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")


def menu_empleado(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("")

def menu_gerente(archivo_clientes, archivo_empleados, archivo_gerentes):
    print("")















