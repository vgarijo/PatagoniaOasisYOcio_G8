import csv
import numpy as np
import random as rd
import datetime as dt

class Persona:
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.mail = mail
        self.password = password
        self.fec_nac = fec_nac

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nMail: {self.mail}\nFecha de nacimiento: {self.fec_nac}"


    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. DNI")
        print("4. Mail")
        print("5. Fecha de nacimiento")
        rta=validar_respuesta_menu(5)
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
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, tipo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac)
        self.tipo = tipo
        
        self.reservas = Lista_Enlazada()
        self.consumos = Lista_Enlazada()

        matriz=csvtomatriz("reservas.csv")
        for i in range(len(matriz)):
            if self.DNI == matriz[i][1]:
                self.reservas.append(Reserva(matriz[i][0], matriz[i][1], matriz[i][2], matriz[i][3], matriz[i][4], matriz[i][5]))
        
        matriz=csvtomatriz("consumos.csv")
        for i in range(len(matriz)):
            if self.DNI == matriz[i][1]:
                self.consumos.append(Consumo(matriz[i][0], matriz[i][1], matriz[i][2], matriz[i][3], matriz[i][4]))
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nMail: {self.mail}\nFecha de nacimiento: {self.fec_nac}\nTipo: {self.tipo}\nReservas: {self.reservas}\nConsumos: {self.consumos}"

    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. DNI")
        print("4. Mail")
        print("5. Contraseña")
        print("6. Fecha de nacimiento")
        print("7. Volver atras")
        print("8. Salir")
        rta=validar_respuesta_menu(8)
        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
        elif rta == 3:
            self.DNI = validar_dni()
        elif rta == 4:
            self.mail = validar_mail()
        elif rta == 5:
            self.cambiar_password()
        elif rta == 6:
            self.fec_nac=validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA):")
        elif rta == 7: 
            menu_cliente()
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()


    def modificar_reserva(self, reserva): ### este es el metodo de reservas, después hago el de cliente
        while True:
            print("¿Qué desea modificar?")
            print("1. Habitacion:", reserva.habitacion, "Tipo:", reserva.tipo)
            print("2. Cantidad de personas:", reserva.cant_personas)
            print("3. Fecha de ingreso:", reserva.fecha_ing)
            print("4. Fecha de egreso:", reserva.fecha_egr)
            print("5. Volver atras")
            rta = validar_respuesta_menu(5)
            if rta == 1: #modificar habitacion
                self.elegir_habitacion(reserva)
            elif rta == 2: #modificar cant de personas
                pass
            elif rta == 3: #modificar fecha de comienzo de reserva
                pass
            elif rta == 4: #modificar fecha de salida
                pass
            elif rta == 5:
                menu_reserva_actual(self, reserva)
        
    def elegir_habitacion(self, reserva):

        habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")


        print("Habitaciones disponibles:")
        print(f"1. Habitación Simple: Precio ${habitaciones_desc[0][1]} por noche. Capacidad máxima: 1 persona. 1 cama individual. Baño compartido. No tiene ventana balcón")
        print(f"2. Habitación Doble: Precio ${habitaciones_desc[1][1]} por noche. Capacidad máxima: 2 personas. 1 cama matrimonial. Baño compartido. No tiene ventana balcón")
        print(f"3. Suite: Precio ${habitaciones_desc[2][1]} por noche. Capacidad máxima: 2 personas. 1 cama matrimonial. Baño privado. Tiene ventana balcón")
        print(f"4. Habitación Familiar: Precio ${habitaciones_desc[3][1]} por noche. Capacidad máxima: 4 personas. 2 camas individuales y 1 cama matrimonial. Baño privado. Tiene ventana balcón")
        print("5. Volver")
        rta = validar_respuesta_menu(5)
        
        if rta == 1:
            habitacion = self.chequear_disponibilidad("simple", reserva)
            if habitacion != reserva.habitacion:
                print("¿Desea confirmar la reserva?")
                print("1. Si")
                print("2. No")
                rta = validar_respuesta_menu(2)

                if rta == 1:
                    reserva.habitacion = habitacion
                    reserva.tipo = "simple"

                    matriz=csvtomatriz("reservas.csv")
                    for i in range(len(matriz)):
                        if reserva.numero_res == matriz[i][0]:
                            matriz[i][1] = habitacion
                            matriz[i][2] = "simple"
                    matriztocsv("reservas.csv", matriz,"R")
                    print("Reserva confirmada.")

        if rta == 2:
            habitacion = self.chequear_disponibilidad("doble", reserva)
        if rta == 3:
            habitacion = self.chequear_disponibilidad("suite", reserva)
        if rta == 4:
            habitacion = self.chequear_disponibilidad("familiar", reserva)
        if rta == 5:
            if reserva == None:
                self.nuevareserva()
            else:
                self.modificar_reserva(reserva)
        
    def chequear_disponibilidad(self, tipo, reserva):

        habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")
        reservas = csvtomatriz("reservas.csv")
        habitaciones = csvtomatriz("habitaciones.csv")

        # Borro de habitaciones las que no son del tipo seleccionado
        for i in range(len(habitaciones)):
            if habitaciones[i][1] != tipo:
                habitaciones.pop(i)
        
        #Agrego una columna a habitaciones que digan "disponible"
        for i in range(len(habitaciones)):
            habitaciones[i].append("disponible")

        # Chequeo que la cantidad de personas esté ok
        if reserva.can_personas > int(habitaciones_desc[tipo][2]):
            print("La cantidad de personas supera la capacidad máxima de la habitación.")
            return reserva.habitacion
        
        # Chequeo que el tipo de habitación sea distinto al actual
        if reserva.tipo == tipo:
            print("El tipo de habitación seleccionado es el misma que el actual.")
            return reserva.habitacion
        
        # Chequeo que haya alguna habitación del tipo nuevo disponible
        for i in range(len(habitaciones)):
            for i in range(len(reservas)):
                if reservas[i][2] == habitaciones[i][0]:
                    if strtodatime(reservas[i][3]) <= strtodatime(reserva.fecha_egr):
                        if strtodatime(reservas[i][4]) >= strtodatime(reserva.fecha_ing):
                            habitaciones[i][2] = "no disponible"
        
        # Recorro las habitaciones a ver si hay una disponible y asigno la primera que encuentre
        for i in range(len(habitaciones)):
            if habitaciones[i][2] == "disponible":
                print("Habitación asignada:", habitaciones[i][0])
                return habitaciones[i][0]
        
        # Si no hay habitaciones disponibles, retorno la que haya estaba
        print("No hay habitaciones disponibles del tipo seleccionado.")
        return reserva.habitacion



class Empleado(Persona):
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, area, activo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac)
        self.area = area
        self.activo = activo
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nMail: {self.mail}\nFecha de nacimiento: {self.fec_nac}\nArea: {self.area}\nStatus: {self.activo}"

    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. DNI")
        print("4. Mail")
        print("5. Contraseña")
        print("6. Fecha de nacimiento")
        print("7. Area")
        print("8. Estado")
        print("9. Volver atras")
        print("10. Salir")
        rta=validar_respuesta_menu(10)
        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
        elif rta == 3:
            self.DNI = validar_dni()
        elif rta == 4:
            self.mail = validar_mail()
        elif rta == 5:
            self.cambiar_password()
        elif rta == 6:
            self.fec_nac=validar_fec("Ingrese la fecha de nacimiento (DD/MM/AAAA):")
        elif rta == 7:
            self.area = input("Ingrese su nueva area: ")
        elif rta == 8:
            self.activo = input("Ingrese su nuevo estado: ")
        elif rta == 9: 
            menu_empleado()
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()

class Gerente(Empleado):
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, area, activo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac, area, activo)
    
    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. DNI")
        print("4. Mail")
        print("5. Contraseña")
        print("6. Fecha de nacimiento")
        print("7. Area")
        print("8. Estado")
        print("9. Volver atras")
        print("10. Salir")
        rta=validar_respuesta_menu(10)
        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
        elif rta == 3:
            self.DNI = validar_dni()
        elif rta == 4:
            self.mail = validar_mail()
        elif rta == 5:
            self.cambiar_password()
        elif rta == 6:
            self.fec_nac=validar_fec("Ingrese la fecha de nacimiento (DD/MM/AAAA):")
        elif rta == 7:
            self.area = input("Ingrese su nueva area: ")
        elif rta == 8:
            self.activo = input("Ingrese su nuevo estado: ")
        elif rta == 9: 
            menu_gerente()
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()
        
class Reserva():
    def __init__(self, numero_res, dni_cliente, habitacion, tipo, fecha_ing, fecha_egr, cant_personas):
        self.dni_cliente = dni_cliente
        self.habitacion = habitacion
        self.tipo = tipo
        self.fecha_ing = fecha_ing
        self.fecha_egr = fecha_egr
        self.numero_res = numero_res
        self.cant_personas = cant_personas

    def __str__(self) -> str:
        return f"Numero de reserva: {self.numero_res}\nDNI del cliente: {self.dni_cliente}\nHabitacion: {self.habitacion}\nFecha de ingreso: {self.fecha_ing}\nFecha de egreso: {self.fecha_egr}\nCantidad de personas: {self.cant_personas}"   

class Consumo():
    def __init__(self, nro_pedido, cliente, fecha, item, precio):
        self.numero_pedido = nro_pedido
        self.cliente = cliente
        self.fecha = fecha
        self.item = item
        self.precio = precio
    
    def __str__(self) -> str:
        return f"Numero de pedido: {self.numero_pedido}\nCliente: {self.cliente}\nFecha: {self.fecha}\nItem: {self.item}\nPrecio: {self.precio}"

class Nodo(): # Nodo de la lista enlazada
    def __init__(self,dato=None,prox=None): # Constructor de la clase
        self.dato=dato # dato del nodo
        self.prox=prox # Puntero al siguiente nodo
    def __str__(self): # Devuelve una cadena con el dato del nodo
        return str(self.dato)

class Lista_Enlazada(): # Lista enlazada
    def __init__(self): # Constructor de la clase
        self.head=None
        self.len=0 # Longitud de la lista
    
    def insertarinicio(self,dato): # Agrega un elemento al inicio de la lista
        nodo=Nodo(dato) # Crea un nuevo nodo
        nodo.prox=self.head # El nodo siguiente del nuevo nodo es el nodo inicial
        self.head=nodo # El nodo inicial es el nuevo nodo
        self.len+=1 # Incrementa la longitud de la lista

    def append(self,dato): # Agrega un elemento al final de la lista
        nodo=Nodo(dato) # Crea un nuevo nodo
        if self.head==None: # Si la lista está vacía
            self.head=nodo # El nodo inicial es el nuevo nodo
        else: # Si la lista no está vacía
            act=self.head # Crea un nodo auxiliar
            while act.prox!=None: # Recorre la lista hasta el último nodo
                act=act.prox # Avanza al siguiente nodo
            act.prox=nodo # El nodo siguiente del último nodo es el nuevo nodo
        self.len+=1 # Incrementa la longitud de la lista

    def pop (self): # Elimina el último elemento de la lista
        if self.head==None: # Si la lista está vacía
            print("Lista vacía") # Muestra un mensaje de error
        elif self.head.prox==None: # Si la lista tiene un solo elemento
            self.head=None # El nodo inicial es None
            self.len-=1 # Decrementa la longitud de la lista
        else: # Si la lista tiene más de un elemento
            act=self.head # Crea un nodo auxiliar
            while act.prox.prox!=None: # Recorre la lista hasta el penúltimo nodo
                act=act.prox # Avanza al siguiente nodo
            act.prox=None # El nodo siguiente del penúltimo nodo es None
            self.len-=1 # Decrementa la longitud de la lista    

    def insertar(self,dato,pos): # Inserta un elemento en la posición indicada
        if pos<=self.len: # Si la posición es válida
            nodo=Nodo(dato) # Crea un nuevo nodo
            act=self.head # Crea un nodo auxiliar
            if pos==0: # Si la posición es la primera
                nodo.prox=self.head # El nodo siguiente del nuevo nodo es el nodo inicial
                self.head=nodo # El nodo inicial es el nuevo nodo
            else: # Si la posición no es la primera
                for i in range(1,pos): # Recorre la lista hasta la posición anterior a la indicada
                    act=act.prox # Avanza al siguiente nodo
                nodo.prox=act.prox # El nodo siguiente del nuevo nodo es el nodo siguiente del nodo actual
                act.prox=nodo # El nodo siguiente del nodo actual es el nuevo nodo
            self.len+=1 # Incrementa la longitud de la lista
        else:
            print("Posición inválida") # Si la posición no es válida, muestra un mensaje de error
    
    def eliminar(self,pos): # Elimina un elemento de la posición indicada
        if pos<self.len: # Si la posición es válida
            if pos==0: # Si la posición es la primera
                self.head=self.head.prox # El nodo inicial es el nodo siguiente del nodo inicial
            else: # Si la posición no es la primera
                act=self.head # Crea un nodo auxiliar
                for i in range(1,pos): # Recorre la lista hasta la posición anterior a la indicada
                    act=act.prox # Avanza al siguiente nodo
                act.prox=act.sig.prox # El nodo siguiente del nodo actual es el nodo siguiente del nodo siguiente del nodo actual
            self.len-=1 # Decrementa la longitud de la lista
        else:
            print("Posición inválida")
    
    def mostrar(self): # Muestra los elementos de la lista
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            print(act.dato) # Muestra el dato del nodo actual
            act=act.prox # Avanza al siguiente nodo
    
    def buscar(self,dato): # Busca un elemento en la lista
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            if act.dato==dato: # Si el dato del nodo actual es el buscado
                return i # Devuelve la posición del nodo actual
            act=act.prox # Avanza al siguiente nodo
        return -1 # Si no se encuentra el dato, devuelve -1
    
    def obtener(self,pos): # Obtiene el dato de un elemento de la lista
        if pos<self.len: # Si la posición es válida
            act=self.head # Crea un nodo auxiliar
            for i in range(pos): # Recorre la lista hasta la posición indicada
                act=act.prox # Avanza al siguiente nodo
            return act.dato # Devuelve el dato del nodo actual
        else:
            print("Posición inválida")
            return None
    
    def modificar(self,dato,pos): # Modifica el dato de un elemento de la lista
        if pos<self.len: # Si la posición es válida
            act=self.head # Crea un nodo auxiliar
            for i in range(pos): # Recorre la lista hasta la posición indicada
                act=act.prox # Avanza al siguiente nodo
            act.dato=dato # Modifica el dato del nodo actual
        else:
            print("Posición inválida")
    
    def intercambiar(self,pos1,pos2): # Intercambia dos elementos de la lista
        if pos1<self.len and pos2<self.len: # Si las posiciones son válidas
            act1=self.head # Crea un nodo auxiliar
            for i in range(pos1): # Recorre la lista hasta la posición indicada
                act1=act1.prox # Avanza al siguiente nodo
            act2=self.head # Crea un nodo auxiliar
            for i in range(pos2): # Recorre la lista hasta la posición indicada
                act2=act2.prox # Avanza al siguiente nodo
            aux=act1.dato # Guarda el dato del nodo actual
            act1.dato=act2.dato # Modifica el dato del nodo actual
            act2.dato=aux # Modifica el dato del nodo actual
        else:
            print("Posición inválida")
    
    def ordenar(self): # Ordena los elementos de la lista
        for i in range(self.len-1): # Recorre la lista
            for j in range(i+1,self.len): # Recorre la lista
                if self.obtener(i)>self.obtener(j): # Si el dato del nodo actual es mayor que el dato del nodo siguiente
                    self.intercambiar(i,j) # Intercambia los datoes de los nodos
    
    def invertir(self): # Invierte los elementos de la lista
        for i in range(self.len//2): # Recorre la lista hasta la mitad
            self.intercambiar(i,self.len-i-1) # Intercambia los datoes de los nodos
        
    def vacia(self): # Devuelve True si la lista está vacía
        return self.len==0
    
    def longitud(self): # Devuelve la longitud de la lista
        return self.len
    
    def limpiar(self): # Elimina todos los elementos de la lista
        self.head=None
        self.len=0
    
    def clonar(self): # Devuelve una copia de la lista
        nueva=Lista_Enlazada() # Crea una nueva lista
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            nueva.insertar(act.dato,i) # Inserta el dato del nodo actual en la nueva lista
            act=act.prox # Avanza al siguiente nodo
        return nueva # Devuelve la nueva lista
    
    def __del__(self): # Destructor de la clase
        self.limpiar() # Elimina todos los elementos de la lista
    
    def __str__(self): # Devuelve una cadena con los elementos de la lista
        cadena=""
        act=self.head # Crea un nodo auxiliar
        for i in range(self.len): # Recorre la lista
            cadena+=str(act.dato)+" " # Agrega el dato del nodo actual a la cadena
            cadena+="\n"
            act=act.prox # Avanza al siguiente nodo
        if cadena == "": # Si la cadena está vacía
            cadena = "Lista vacía"
        return cadena # Devuelve la cadena
    
    def __len__(self): # Devuelve la longitud de la lista
        return self.len
    
    def __getitem__(self,pos): # Devuelve el dato de un elemento de la lista
        return self.obtener(pos)
    
    def __setitem__(self,pos,dato): # Modifica el dato de un elemento de la lista
        self.modificar(dato,pos)
    
    def __eq__(self,otra): # Devuelve True si las listas son iguales
        if self.len==otra.len: # Si los longituds de las listas son iguales
            act1=self.head # Crea un nodo auxiliar
            act2=otra.head # Crea un nodo auxiliar
            for i in range(self.len): # Recorre la lista
                if act1.dato!=act2.dato: # Si los datoes de los nodos actuales son distintos
                    return False # Devuelve False
                act1=act1.prox # Avanza al siguiente nodo
                act2=act2.prox # Avanza al siguiente nodo
            return True # Devuelve True
        else:
            return False
    
    def __ne__(self,otra): # Devuelve True si las listas son distintas
        return not self==otra
    
    def __lt__(self,otra): # Devuelve True si la lista es menor que la otra
        if self.len<otra.len: # Si la longitud de la lista es menor que el de la otra
            return True # Devuelve True
        elif self.len==otra.len: # Si la longitud de la lista es igual que el de la otra
            act1=self.head # Crea un nodo auxiliar
            act2=otra.head # Crea un nodo auxiliar
            for i in range(self.len): # Recorre la lista
                if act1.dato>act2.dato: # Si el dato del nodo actual es mayor que el dato del nodo actual de la otra lista
                    return False # Devuelve False
                act1=act1.prox # Avanza al siguiente nodo
                act2=act2.prox # Avanza al siguiente nodo
            return True # Devuelve True
        else:
            return False
    
    def __le__(self,otra): # Devuelve True si la lista es menor o igual que la otra
        return self<otra or self==otra
    
    def __gt__(self,otra): # Devuelve True si la lista es mayor que la otra
        return not self<=otra
    
    def __ge__(self,otra): # Devuelve True si la lista es mayor o igual que la otra
        return not self<otra

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

def matriztocsv(archivo, matriz, tipo): #tipo se refiere a si quiero agregar una reserva "R" o un nuevo empleado "E"
    if tipo=="R":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Numero de reserva", "DNI del cliente", "Habitacion", "Fecha de ingreso", "Fecha de egreso", "Cantidad de personas"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])
    elif tipo=="E":
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Nombre", "Apellido", "DNI", "Mail", "Contraseña", "Fecha de Nacimiento", "Area", "Estado"])
            for i in range(len(matriz)):
                writer.writerow(matriz[i])

def strtodatime(fecha):
    fecha = fecha.split("/")
    fecha = dt.datetime(int(fecha[2]), int(fecha[1]), int(fecha[0]))
    return fecha

def stringAempleado(matriz):
    lista_empleados=[]
    for i in range(len(matriz)):
        lista_empleados.append(Empleado(matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3],matriz[i][4],matriz[i][5],matriz[i][6],matriz[i][7]))
    return lista_empleados

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
                        cliente = Cliente(matriz_clientes[i][0], matriz_clientes[i][1], matriz_clientes[i][2], matriz_clientes[i][3], matriz_clientes[i][4], matriz_clientes[i][5],matriz_clientes[i][6])
                        menu_cliente(cliente)
                        break
            print("Mail o contraseña incorrectos. Intente nuevamente.")

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
                        empleado = Empleado(matriz_empleados[i][0], matriz_empleados[i][1], matriz_empleados[i][2], matriz_empleados[i][3], matriz_empleados[i][4], matriz_empleados[i][5],matriz_empleados[i][6],matriz_empleados[i][7])
                        menu_empleado(empleado)
                        break
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
                        gerente = Gerente(matriz_empleados[i][0], matriz_empleados[i][1], matriz_empleados[i][2], matriz_empleados[i][3], matriz_empleados[i][4], matriz_empleados[i][5],matriz_empleados[i][6],matriz_empleados[i][7])
                        menu_gerente(gerente)
                        break
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
            for i in range(len(reservas_actuales)):
                print(i+1, ". ", reservas_actuales[i])
            rta = validar_respuesta_menu(len(reservas_actuales))
            menu_reserva_actual(cliente, reservas_actuales[rta-1])

    elif rta == 2:
        menu_reservas_anteriores(cliente)

    elif rta == 3:
        menu_nueva_reserva(cliente)

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
            menu_reservas(cliente)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()

    print("")

def menu_reservas_anteriores(cliente):
    print("Reservas anteriores")
    print("¿Qué desea hacer?")
    print("1. Atrás")
    print("2. Salir")
    rta = validar_respuesta_menu(2)
    if rta == 1:
        menu_reservas(cliente)
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
def menu_datos_personales(persona):
    print("Personales")
    print("¿Qué desea hacer?")
    print("1. Ver Datos Personales")
    print("2. Modificar Datos Personales")
    print("3. Cambiar Contraseña")
    print("4. Volver atras")
    print("5. Salir")
    rta = validar_respuesta_menu(5)
    if rta == 1:
        print(persona)
    
    elif rta == 2:
        persona.modificar_datos_personales()
        
    elif rta == 3:
        persona.cambiar_password()
        
    elif rta == 4:
        if type(persona)==Cliente:
            menu_cliente()

        elif type(persona)==Empleado:
            menu_empleado()

        else:
            menu_gerente()

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
        print("Ingreso efectuado")
    if rta == 2:
        print("Egreso efectuado")
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
    print("6. Volver atras")
    print("7. Salir")
    rta = validar_respuesta_menu(7)
    if rta == 1:
        print("Ingreso efectuado")
    if rta == 2:
        print("Egreso efectuado")
    if rta == 3:
        menu_datos_personales(gerente)
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
    matriz_empleados=csvtomatriz("empleados.csv")
    lista_empleados=stringAempleado(matriz_empleados)

    if rta == 1:
        # ver empleados
        for i in range(lista_empleados):
            print(lista_empleados[i])
            print('\n')
        
    if rta == 2:
        # Agregar empleado
        print('Ingrese los datos del nuevo empleado:')
        print("\n")  #nombre, apellido, DNI, mail, password, fec_nac, area, activo
        nombre=input("Nombre del empleado: ")
        apellido=input("Apellido del empleado: ")
        dni=validar_dni()
        mail=validar_mail()
        password=input("Constraseña del empleado: ")
        print("Ingrese fecha de nacimiento: ")
        fecha_nac=validar_fec("")
        area=input("Área del empleado: ")
        activo=input("Área del empleado (Activo o No activo): ")
        matriz_empleados.append([nombre,apellido,dni,mail,password,fecha_nac,area,activo])
        matriztocsv("empleados.csv",matriz_empleados,"E")
        
    if rta == 3:
        # Modificar empleado
        dni_requerido=validar_dni()
        for empleado in lista_empleados:
            if empleado.DNI==dni_requerido:
                empleado.modificar_datos_personales()
                for i in range(len(matriz_empleados)):
                    if dni_requerido==matriz_empleados[i][2]:
                        matriz_empleados[i]=[empleado.nombre,empleado.apellido,empleado.DNI,empleado.mail,empleado.password,empleado.fec_nac,empleado.area,empleado.activo]
                        matriztocsv("empleados.csv",matriz_empleados,"E")

    if rta == 4:
        # Eliminar empleado
        dni_requerido=validar_dni()
        for i in range(len(matriz_empleados)):
                    if dni_requerido==matriz_empleados[i][2]:
                        matriz_empleados.pop(i)
                        matriztocsv("empleados.csv",matriz_empleados,"E")

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
