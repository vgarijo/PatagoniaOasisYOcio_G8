import csv
import datetime as dt

def validar_dni():
    # El DNI es un número de 7 u 8 cifras
    dni = input("Ingrese DNI: ")
    while not dni.isdigit() or len(dni) < 7 or len(dni) > 8:
        dni = input("DNI no válido, ingrese otro: ")
    return dni

def validar_mail():
    # El mail debe contener un @ y un .
    mail = input("Ingrese dirección de mail: ")
    while not "@" in mail or not "." in mail:
        mail = input("Mail no válido, ingrese otro: ")
    return mail

def validar_fec(mensaje):
    # La fecha debe tener el formato dd/mm/aaaa
    fecha = input(mensaje)
    while not "/" in fecha or len(fecha) != 10:
        fecha = input("Fecha no válida, ingrese otra: ")
    return fecha
        
def validar_respuesta_menu(rta):
    rtas=range(1, rta+1)
    # Paso los datos de rtas a string
    rtas = [str(i) for i in rtas]
    rta = input("Ingrese la opción deseada: ")
    while rta not in rtas:
        rta = (input("Respuesta no valida, ingrese otra opcion: "))
    print("")
    return int(rta)

def csvtomatriz(archivo):
    try:
        with open(archivo) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            matriz = []
            for row in reader:
                matriz.append(row)
        return matriz[1:]
    except IOError:
        print("No se encontró el archivo.")

def csvtodicc(archivo):
    try:
        with open(archivo) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            dicc = {}
            for row in reader:
                dicc[row[0]] = row[1]
        return dicc
    except IOError:
        print("No se encontró el archivo.")

def matriztocsv(archivo, matriz, tipo): #tipo se refiere a si quiero agregar una reserva "R" o un nuevo empleado "E", "Con" consumos, "Cl" cliente y "IE" ingresos y egresos
    if tipo=="R":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Numero de reserva", "DNI del cliente", "Habitacion", "Tipo", "Fecha de ingreso", "Fecha de egreso", "Cantidad de personas", "Checkin", "Checkout", "Horario de checkin", "Horario de checkout", "Precio"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])
    elif tipo=="E":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Nombre", "Apellido", "DNI", "Mail", "Password", "Fecha de Nacimiento", "Area", "Estado"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])
    elif tipo=="Con":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Numero de pedido", "DNI del cliente", "Fecha", "Item", "Cantidad","Precio"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])
    elif tipo=="Cl":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Nombre", "Apellido", "DNI", "Mail", "Password", "Fecha de Nacimiento", "Gastos", "Tipo"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])
    elif tipo=="IE":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Id_Ingreso", "DNI del empleado", "Dia", "Hora_Entrada", "Hora_Salida"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])
    elif tipo =="T":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["id_tarea", "DNI_empleado","Tarea", "Fecha"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])

def strtodatime(fecha):
    fecha = fecha.split("/")
    fecha = dt.datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
    return fecha

def stringAempleado(matriz):
    from clases import Empleado
    from clases import Lista_Enlazada
    lista_empleados=Lista_Enlazada()
    for i in range(len(matriz)):
        lista_empleados.append(Empleado(matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3],matriz[i][4],matriz[i][5],matriz[i][6],matriz[i][7]))
    return lista_empleados
