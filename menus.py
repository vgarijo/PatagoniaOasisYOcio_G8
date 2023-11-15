import datetime as dt
from clases import *
from funciones import *

# Menu principal
def menuPOO():
    print("Bienvenido al Hotel Patagonia Oasis y Ocio.")
    print("¿A qué menu desea ingresar?")
    print("1. Menu de cliente")
    print("2. Menu de empleado")
    print("3. Menu de gerente")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:

        print("¿Desea registrarse o ingresar?")
        print("1. Registrarse")
        print("2. Ingresar")
        print("3. Volver")
        rta = validar_respuesta_menu(3)

        if rta == 1:
            matriz_clientes = csvtomatriz("clientes.csv")
            cliente = Cliente("","","","","","","","")
            print("Ingrese sus datos:")
            cliente.nombre = input("Nombre: ")
            cliente.apellido = input("Apellido: ")
            DNI = validar_dni()
            for i in range(len(matriz_clientes)):
                if DNI == matriz_clientes[i][2]:
                    print("Ya existe un usuario con ese DNI.")
                    print("")
                    menuPOO()
                    exit()
            cliente.DNI = DNI
            mail = validar_mail()
            for i in range(len(matriz_clientes)):
                if mail == matriz_clientes[i][3]:
                    print("Ya existe un usuario con ese mail.")
                    print("")
                    menuPOO()
                    exit()
            cliente.mail = mail
            cliente.password = input("Contraseña: ")
            cliente.fec_nac = validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
            cliente.gastos = "0"
            cliente.tipo = "basico"

            print("¿Desea confirmar su registro?")
            print(cliente)
            print("")
            print("1. Confirmar")
            print("2. Cancelar")
            rta = validar_respuesta_menu(2)

            if rta == 1:
                matriz_clientes.append([cliente.nombre, cliente.apellido, cliente.DNI, cliente.mail, cliente.password, cliente.fec_nac, cliente.gastos, cliente.tipo])
                matriztocsv("clientes.csv", matriz_clientes,"Cl")
                print("Registro exitoso. Ingrese sus datos para ingresar al sistema.")
                print("")
            else:
                print("Cancelando...")
                print("")
            
            menuPOO()
            exit()
        elif rta == 2:
            matriz_clientes=csvtomatriz("clientes.csv")
            # Ejecuta ingreso_usuario, chequea el mail si está registrado o vuelve a pedir el mail
            
            while True:
                mail = input("Ingrese su mail. Presione 0 para volver: ")
                if mail == "0":
                    menuPOO()
                    break
                else:
                    contrasena = input("Ingrese su contraseña: ")
                    print("")
                
                for i in range(len(matriz_clientes)):
                    if mail == matriz_clientes[i][3]:
                        if contrasena == matriz_clientes[i][4]:
                            print("Ingreso exitoso")
                            print("")
                            cliente = Cliente(matriz_clientes[i][0], matriz_clientes[i][1], matriz_clientes[i][2], matriz_clientes[i][3], matriz_clientes[i][4], matriz_clientes[i][5],matriz_clientes[i][6],matriz_clientes[i][7])
                            menu_cliente(cliente)
                            exit()
                print("Mail o contraseña incorrectos. Intente nuevamente.")
        else:
            menuPOO()

    elif rta == 2:
        matriz_empleados=csvtomatriz("empleados.csv")
        # Ejecuta ingreso_usuario, chequea el mail si está registrado o vuelve a pedir el mail
        
        while True:
            mail = input("Ingrese su mail. Presione 0 para volver: ")
            if mail == "0":
                menuPOO()
                break
            else:
                contrasena = input("Ingrese su contraseña: ")
                print("")
            
            for i in range(len(matriz_empleados)):
                if mail == matriz_empleados[i][3]:
                    if contrasena == matriz_empleados[i][4]:
                        print("Ingreso exitoso")
                        print("")
                        empleado = Empleado(matriz_empleados[i][0], matriz_empleados[i][1], matriz_empleados[i][2], matriz_empleados[i][3], matriz_empleados[i][4], matriz_empleados[i][5],matriz_empleados[i][6],matriz_empleados[i][7])
                        menu_empleado(empleado)
                        exit()
            print("Mail o contraseña incorrectos. Intente nuevamente.")

    elif rta == 3:
        matriz_empleados=csvtomatriz("empleados.csv")
        # Ejecuta ingreso_usuario, chequea el mail si está registrado o vuelve a pedir el mail
        
        while True:
            mail = input("Ingrese su mail. Presione 0 para volver: ")
            if mail == "0":
                menuPOO()
                break
            else:
                contrasena = input("Ingrese su contraseña: ")
                print("")
            
            for i in range(len(matriz_empleados)):
                if mail == matriz_empleados[i][3]:
                    if contrasena == matriz_empleados[i][4] and matriz_empleados[i][6] == "gerente":
                        print("Ingreso exitoso")
                        print("")
                        gerente = Gerente(matriz_empleados[i][0], matriz_empleados[i][1], matriz_empleados[i][2], matriz_empleados[i][3], matriz_empleados[i][4], matriz_empleados[i][5],matriz_empleados[i][6],matriz_empleados[i][7])
                        menu_gerente(gerente)
                        exit()
            print("Mail o contraseña incorrectos. Intente nuevamente.")

    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu cliente
def menu_cliente(cliente): 
    print("Bienvenido", cliente.nombre, "al menu de cliente.")
    print("¿Qué desea hacer?")
    print("1. Mis Reservas")
    print("2. Mis Consumos")
    print("3. Datos Personales")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(5)
    if rta == 1:
        menu_reservas(cliente)
    elif rta == 2:
        menu_consumos(cliente)
    elif rta == 3:
        menu_datos_personales(cliente)
    elif rta == 4:
        menuPOO()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu Reservas
def menu_reservas(cliente):
    print("Mis reservas")
    print("¿Qué desea hacer?")
    print("1. Reserva actual")
    print("2. Reservas anteriores")
    print("3. Nueva Reserva")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(5)

    if rta == 1:
        reservas_actuales = []
        for i in range(len(cliente.reservas)):
            if strtodatime(cliente.reservas[i].fecha_egr) >= dt.datetime.now():
                reservas_actuales.append(cliente.reservas[i])
        
        if len(reservas_actuales) == 0:
            menu_reserva_actual(cliente, None)
        elif len(reservas_actuales) == 1:
            menu_reserva_actual(cliente, reservas_actuales[0])
        else:
            print("Tiene varias reservas actuales. Seleccione una:")
            print("")
            for i in range(len(reservas_actuales)):
                print(i+1, ". ", reservas_actuales[i])
                print("")
            rta = validar_respuesta_menu(len(reservas_actuales))
            menu_reserva_actual(cliente, reservas_actuales[rta-1])

    elif rta == 2:
        menu_reservas_anteriores(cliente)

    elif rta == 3:
        cliente.nueva_reserva()

    elif rta == 4:
        menu_cliente(cliente)

    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

def menu_reserva_actual(cliente, reserva_actual):
    if reserva_actual == None:
        print("No tiene una reserva actual")
        print("¿Qué desea hacer?")
        print("1. Volver atras")
        print("2. Salir")
        rta = validar_respuesta_menu(2)
        if rta == 1:
            menu_reservas(cliente)
        
    else:
        print("Su reserva actual es:")
        print(reserva_actual)
        print("")
        print("¿Qué desea hacer?")
        print("1. Modificar Reserva")
        print("2. Cancelar Reserva")
        print("3. Check In")
        print("4. Check Out")
        print("5. Volver atras")
        print("6. Salir")
        rta = validar_respuesta_menu(7)
        if rta == 1:
            cliente.modificar_reserva(reserva_actual)
            pass
        elif rta == 2:
            cliente.cancelar_reserva(reserva_actual)
            pass
        elif rta == 3:
            cliente.checkin(reserva_actual)
        elif rta == 4:
            cliente.checkout(reserva_actual)
                
        elif rta == 5:
            menu_reservas(cliente)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()

    print("")

def menu_reservas_anteriores(cliente):
    print("Reservas anteriores:")
    print("")
    for i in range(len(cliente.reservas)):
        if strtodatime(cliente.reservas[i].fecha_egr) < dt.datetime.now():
            print(cliente.reservas[i])
            print("")
    print("¿Qué desea hacer?")
    print("1. Atrás")
    print("2. Salir")
    rta = validar_respuesta_menu(2)
    if rta == 1:
        menu_reservas(cliente)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu consumos
def menu_consumos(cliente):
    print("Consumos")
    print("¿Qué desea hacer?")
    print("1. Historial de Consumos")
    print("2. Nuevo Consumo")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        print(cliente.consumos)
        menu_consumos(cliente)
        pass
    elif rta == 2:
        cliente.consumir()
        pass
    elif rta == 3:
        menu_cliente(cliente)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

# Menu datos personales
def menu_datos_personales(persona):
    print("Datos personales")
    print("¿Qué desea hacer?")
    print("1. Ver Datos Personales")
    print("2. Modificar Datos Personales")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        print(persona)
        print("")
        menu_datos_personales(persona)
    elif rta == 2:
        persona.modificar_datos_personales()

    elif rta == 3:
        if type(persona)==Cliente:
            menu_cliente(persona)

        elif type(persona)==Empleado:
            menu_empleado(persona)

        else:
            menu_gerente(persona)

    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

# Menu empleado
def menu_empleado(empleado):
    print("Bienvenido al menu de empleado")
    print("¿Qué desea hacer?")
    print("1. Ingreso")
    print("2. Egreso")
    print("3. Datos Personales")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(5)
    if rta == 1:
        empleado.ingreso()
    if rta == 2:
        empleado.egreso()
    if rta == 3:
        menu_datos_personales(empleado)
    if rta == 4:
        menuPOO()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu gerente
def menu_gerente(gerente):
    print("Bienvenido al menu de gerente")
    print("¿Qué desea hacer?")
    print("1. Ingreso")
    print("2. Egreso")
    print("3. Datos Personales")
    print("4. Administración de personal")
    print("5. Estadísticas")
    print("6. Actualizar tipo de clientes")
    print("7. Volver atras")
    print("8. Salir")
    rta = validar_respuesta_menu(8)
    if rta == 1:
        gerente.ingreso_egreso("I")
        print("Ingreso efectuado")
        menu_gerente(gerente)
    elif rta == 2:
        gerente.ingreso_egreso("E")
        print("Egreso efectuado")
        menu_gerente(gerente)
    elif rta == 3:
        menu_datos_personales(gerente)
    if rta == 4:
        menu_administracion_personal(gerente)
    if rta == 5:
        menu_estadisticas(gerente)
    elif rta == 6:
        gerente.actualizar_tipo_clientes()
    elif rta == 7:
        menuPOO()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu administracion de personal
def menu_administracion_personal(gerente):
    print("Bienvenido al menu de administración de personal")
    print("¿Qué desea hacer?")
    print("1. Ver empleados")
    print("2. Agregar empleado")
    print("3. Modificar empleado")
    print("4. Eliminar empleado")
    print("5. Volver atras")
    print("6. Salir")
    rta = validar_respuesta_menu(6)
    matriz_empleados=csvtomatriz("empleados.csv")
    lista_empleados=stringAempleado(matriz_empleados)

    if rta == 1:
        # ver empleados
        for i in range(len(lista_empleados)):
            print(lista_empleados[i])
            print('\n')
        menu_administracion_personal(gerente)
        
    if rta == 2:
        # Agregar empleado
        matriz_empleados=csvtomatriz("empleados.csv")
        gerente.agregar_empleado(matriz_empleados)
        menu_administracion_personal(gerente)
 
    if rta == 3:
        # Modificar empleado
        for i in range(len(lista_empleados)):
            print(lista_empleados[i])
            print("")
        dni_requerido=validar_dni()
        for i in range(len(lista_empleados)):
            if lista_empleados[i].DNI==dni_requerido:
                print("")
                gerente.modificarEmpleado(lista_empleados[i])
            elif i == len(lista_empleados)-1:
                print("No se encontró el empleado.")
                print("")
        menu_administracion_personal(gerente)

    if rta == 4:
        # Eliminar empleado
        dni_requerido=validar_dni()
        for i in range(len(matriz_empleados)):
            if dni_requerido==matriz_empleados[i][2]:
                matriz_empleados.pop(i)
                matriztocsv("empleados.csv",matriz_empleados,"E")
        menu_administracion_personal(gerente)

    if rta == 5:
        menu_gerente(gerente)
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu estadisticas
def menu_estadisticas(gerente):
    print("Bienvenido al menu de estadísticas")
    print("¿Qué desea hacer?")
    print("1. Ver porcentajes de ocupación")
    print("2. Ver porcentajes de ocupación por tipo de habitación")
    print("3. Cantidad de clientes por tipo")
    print("4. Recaudación diaria")
    print("5. Volver atras")
    print("6. Salir")
    rta = validar_respuesta_menu(6)
    if rta == 1:
        gerente.porcentaje_ocupacion(None)
        menu_estadisticas(gerente)
    elif rta == 2:
        print("¿Qué tipo de habitación desea ver?")
        print("1. Simple")
        print("2. Doble")
        print("3. Triple")
        print("4. Suite")
        print("5. Volver atras")
        print("6. Salir")
        rta = validar_respuesta_menu(4)
        
        if rta == 1:
            gerente.porcentaje_ocupacion("simple")
        if rta == 2:
            gerente.porcentaje_ocupacion("doble")
        if rta == 3:
            gerente.porcentaje_ocupacion("triple")
        if rta == 4:
            gerente.porcentaje_ocupacion("suite")

        if rta < 6:
            menu_estadisticas(gerente)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()
    elif rta == 3:
        print ("¿Qué tipo de cliente desea ver?")
        print("1. Basico")
        print("2. Regular")
        print("3. Premium")
        print("4. Gold")
        print("5. Volver atras")
        print("6. Salir")
        rta = validar_respuesta_menu(6)

        if rta == 1:
            gerente.cantidad_clientes("Basico")
        if rta == 2:
            gerente.cantidad_clientes("Regular")
        if rta == 3:
            gerente.cantidad_clientes("Premium")
        if rta == 4:
            gerente.cantidad_clientes("Gold")
        
        if rta < 6:
            menu_estadisticas(gerente)
            exit()
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()
    elif rta == 4:
        gerente.recaudacion_diaria()
    elif rta == 5:
        menu_gerente(gerente)
        exit()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

def menu_recaudacion_diaria(gerente):
        print("Ver recaudación diaria de:")
        print("1. Hoy")
        print("2. Seleccionar una fecha")
        print("3. Volver atras")
        print("4. Salir")
        rta = validar_respuesta_menu(4)
        if rta == 1:
            gerente.recaudacion_diaria(dt.datetime.today())
        elif rta == 2:
            fecha = validar_fec("Ingrese la fecha (DD/MM/AAAA): ")
            gerente.recaudacion_diaria(strtodatime(fecha))
        if rta < 3:
            menu_estadisticas(gerente)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()