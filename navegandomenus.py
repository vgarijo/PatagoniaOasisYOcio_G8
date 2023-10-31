class Persona:
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.mail = mail
        self.password = password
        self.fec_nac = fec_nac

    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. DNI")
        print("4. Mail")
        print("5. Fecha de nacimiento")
        print("6. Volver atras")
        print("7. Salir")
        rta=validar_respuesta_menu(7)
        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
        elif rta == 3:
            self.DNI = validar_dni()
        elif rta == 4:
            self.mail = validar_mail()
        elif rta == 5:
            self.fec_nac=validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA):")

    def cambiar_password(self):
        act = input("Ingrese su contraseña actual: ")
        while act != self.password:
            print("Contraseña incorrecta")
            act = input("Ingrese su contraseña actual. Presione 0 para salir: ")
            if act == "0":
                break
        nueva = input("Ingrese su nueva contraseña: ")
        self.password = nueva

class Cliente(Persona): 
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, reservas, consumos, tipo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac)
        self.reservas = reservas #lista_enlazada
        self.consumos = consumos 
        self.tipo = tipo

class Empleado(Persona):
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, area, activo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac)
        self.area = area
        self.activo = activo

class Gerente(Empleado):
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, area, activo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac, area, activo)

class Reserva():
    def __init__(self, cliente, habitacion, fecha_reserva, fecha_ing, fecha_egr, numero_res, cant_personas):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_reserva=fecha_reserva
        self.fecha_ing = fecha_ing
        self.fecha_egr = fecha_egr
        self.numero_res = numero_res
        self.cant_personas = cant_personas


def validar_dni():
    # El DNI es un número de 7 u 8 cifras
    dni = input("Ingrese su DNI: ")
    while not dni.isdigit() or len(dni) < 7 or len(dni) > 8:
        dni = input("DNI no válido, ingrese otro: ")
    return dni

def validar_mail():
    # El mail debe contener un @ y un .
    mail = input("Ingrese su mail: ")
    while not "@" in mail or not "." in mail:
        mail = input("Mail no válido, ingrese otro: ")
    return mail

def validar_fec(mensaje):
    # La fecha debe tener el formato dd/mm/aaaa
    fecha = input(mensaje)
    while not "/" in fecha or len(fecha) != 10:
        fecha = input("Fecha no válida, ingrese otra: ")
    return fecha

def ingreso_usuario():
    mail = input("Ingrese su mail: ")
    contrasena = input("Ingrese su contraseña: ")
    print("")
    return mail, contrasena

def validar_respuesta_menu(rta):
    rtas=range(1, rta+1)
    rta= int(input("Ingrese la opción deseada: "))
    while rta not in rtas:
        rta= int(input("Respuesta no valida, ingrese otra opcion: "))
    print("")
    return rta

from csvtomatriz import *

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
        matriz=csvtomatriz("clientes.csv")
        # Ejecuta ingreso_usuario, chequea el mail si está registrado o vuelve a pedir el mail
        
        menu_cliente()
    elif rta == 2:
        mail,contrasena=ingreso_usuario()
        menu_empleado()
    elif rta == 3:
        mail,contrasena=ingreso_usuario()
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

# Menu consumos
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

# Menu datos personales
def menu_datos_personales():
    print("Personales")
    print("¿Qué desea hacer?")
    print("1. Ver Datos Personales")
    print("2. Modificar Datos Personales")
    print("3. Cambiar Contraseña")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        # método para ver datos personales
        pass
    elif rta == 2:
        # método para modificar datos personales
        pass
    elif rta == 3:
        # método para cambiar contraseña
        pass
    elif rta == 4:
        menu_cliente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

    print("")

# Menu empleado
def menu_empleado():
    print("Bienvenido al menu de empleado")
    print("¿Qué desea hacer?")
    print("1. Ingreso")
    print("2. Egreso")
    print("3. Datos Personales")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(5)
    if rta == 1:
        print("Ingreso efectuado")
    if rta == 2:
        print("Egreso efectuado")
    if rta == 3:
        menu_datos_personales()
    if rta == 4:
        menuPOO()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu gerente
def menu_gerente():
    print("Bienvenido al menu de gerente")
    print("¿Qué desea hacer?")
    print("1. Ingreso")
    print("2. Egreso")
    print("3. Datos Personales")
    print("4. Administración de personal")
    print("5. Estadísticas")
    print("6. Volver atras")
    print("7. Salir")
    rta = validar_respuesta_menu(7)
    if rta == 1:
        print("Ingreso efectuado")
    if rta == 2:
        print("Egreso efectuado")
    if rta == 3:
        menu_datos_personales()
    if rta == 4:
        menu_administracion_personal()
    if rta == 5:
        menu_estadisticas()
    if rta == 6:
        menuPOO()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu administracion de personal
def menu_administracion_personal():
    print("Bienvenido al menu de administración de personal")
    print("¿Qué desea hacer?")
    print("1. Ver empleados")
    print("2. Agregar empleado")
    print("3. Modificar empleado")
    print("4. Eliminar empleado")
    print("5. Volver atras")
    print("6. Salir")
    rta = validar_respuesta_menu(6)
    if rta == 1:
        # método para ver empleados
        pass
    if rta == 2:
        # método para agregar empleado
        pass
    if rta == 3:
        # método para modificar empleado
        pass
    if rta == 4:
        # método para eliminar empleado
        pass
    if rta == 5:
        menu_gerente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

# Menu estadisticas
def menu_estadisticas():
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
        # método para ver porcentajes de ocupación
        pass
    if rta == 2:
        # método para ver porcentajes de ocupación por tipo de habitación
        pass
    if rta == 3:
        # método para ver cantidad de clientes por tipo
        pass
    if rta == 4:
        recaudacion_diaria()
    if rta == 5:
        menu_gerente()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()

def recaudacion_diaria():
    print("Ver recaudación diaria de:")
    print("1. Hoy")
    print("2. Seleccionar una fecha")
    print("3. Volver atras")
    print("4. Salir")
    rta = validar_respuesta_menu(4)
    if rta == 1:
        # método para ver recaudación diaria de hoy
        pass
    if rta == 2:
        # método para ver recaudación diaria de una fecha
        pass
    if rta == 3:
        menu_estadisticas()
    else:
        print("Gracias por utilizar nuestros servicios. Hasta pronto.")
        exit()


menuPOO()
