import datetime as dt
from clases import *
from funciones import *
from menus import *

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

    def cambiar_password(self):
        act = input("Ingrese su contraseña actual: ")
        while act != self.password:
            print("Contraseña incorrecta")
            act = input("Ingrese su contraseña actual. Presione 0 para salir: ")
            if act == "0":
                return self.password
        nueva = input("Ingrese su nueva contraseña: ")
        return nueva

class Cliente(Persona):
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, gastos,tipo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac)
        self.gastos = gastos
        self.tipo = tipo
        
        self.reservas = Lista_Enlazada()
        self.consumos = Lista_Enlazada()

        matriz=csvtomatriz("reservas.csv")
        for i in range(len(matriz)):
            if self.DNI == matriz[i][1]:
                self.reservas.append(Reserva(matriz[i][0], matriz[i][1], matriz[i][2], matriz[i][3], matriz[i][4],matriz[i][5], matriz[i][6],matriz[i][7],matriz[i][8],matriz[i][9],matriz[i][10],matriz[i][11]))
        
        matriz=csvtomatriz("consumos.csv")
        for i in range(len(matriz)):
            if self.DNI == matriz[i][1]:
                self.consumos.append(Consumo(matriz[i][0], matriz[i][1], matriz[i][2], matriz[i][3], matriz[i][4],matriz[i][5]))
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nMail: {self.mail}\nFecha de nacimiento: {self.fec_nac}\nGastos:{self.gastos}\nTipo: {self.tipo}\n\nReservas:\n{self.reservas}\n\nConsumos:\n{self.consumos}"

    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Mail")
        print("4. Contraseña")
        print("5. Fecha de nacimiento")
        print("6. Volver atras")
        print("7. Salir")
        rta=validar_respuesta_menu(7)
        
        matriz_cliente = csvtomatriz("clientes.csv")

        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
            for i in range(len(matriz_cliente)):
                if self.DNI == matriz_cliente[i][2]:
                    matriz_cliente[i][0] = self.nombre
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
            for i in range(len(matriz_cliente)):
                if self.DNI == matriz_cliente[i][2]:
                    matriz_cliente[i][1] = self.apellido
        elif rta == 3:
            self.mail = validar_mail()
            for i in range(len(matriz_cliente)):
                if self.DNI == matriz_cliente[i][2]:
                    matriz_cliente[i][3] = self.mail
        elif rta == 4:
            password=self.cambiar_password()
            for i in range(len(matriz_cliente)):
                if self.DNI == matriz_cliente[i][2]:
                    matriz_cliente[i][4] = password
        elif rta == 5:
            self.fec_nac=validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA):")
            for i in range(len(matriz_cliente)):
                if self.DNI == matriz_cliente[i][2]:
                    matriz_cliente[i][5] = self.fec_nac            
        
        if rta < 6:
            matriztocsv("clientes.csv", matriz_cliente,"Cl")
            print("Modificación realizada.")
            print("")
            self.modificar_datos_personales()
        elif rta == 6: 
            menu_datos_personales(self)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()

    def modificar_reserva(self, reserva): ### este es el metodo de reservas, después hago el de cliente
        while True:

            habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")
            for i in range(len(habitaciones_desc)):
                if habitaciones_desc[i][0] == reserva.tipo:
                    precio = int(habitaciones_desc[i][1])
                    break
            
            costo_actual = precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days

            print("¿Qué desea modificar?")
            print("1. Habitacion:", reserva.habitacion, "Tipo:", reserva.tipo)
            print("2. Cantidad de personas:", reserva.cant_personas)
            print("3. Fecha de ingreso:", reserva.fecha_ing)
            print("4. Fecha de egreso:", reserva.fecha_egr)
            print("5. Volver atras")
            rta = validar_respuesta_menu(5)
            if rta == 1: #modificar habitacion
                self.elegir_habitacion(reserva,costo_actual)
            elif rta == 2: #modificar cant de personas
                self.elegir_cantidad_personas(reserva)
            elif rta == 3: #modificar fecha de comienzo de reserva
                self.modificar_ingreso(reserva,costo_actual)
            elif rta == 4: #modificar fecha de salida
                self.modificar_egreso(reserva,costo_actual)
            elif rta == 5:
                menu_reserva_actual(self, reserva)
        
    def elegir_habitacion(self, reserva, costo_actual):

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
                print(f"¿Desea confirmar la reserva? Precio: ${str(int(habitaciones_desc[0][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))}")
                print("1. Si")
                print("2. No")
                rta = validar_respuesta_menu(2)

                if rta == 1:
                    reserva.habitacion = habitacion
                    reserva.tipo = "simple"
                    reserva.precio = str(int(habitaciones_desc[0][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))

                    matriz=csvtomatriz("reservas.csv")
                    for i in range(len(matriz)):
                        if reserva.numero_res == matriz[i][0]:
                            matriz[i][2] = habitacion
                            matriz[i][3] = "simple"
                            matriz[i][11] = reserva.precio
                    matriztocsv("reservas.csv", matriz,"R")

                    for i in range(len(habitaciones_desc)):
                        if habitaciones_desc[i][0] == reserva.tipo:
                            precio = int(habitaciones_desc[i][1])
                            break

                    matriz=csvtomatriz("clientes.csv")
                    for i in range(len(matriz)):
                        if self.DNI == matriz[i][2]:
                            self.gastos = str(int(self.gastos) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                            matriz[i][6] = str(int(matriz[i][6]) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                    matriztocsv("clientes.csv", matriz,"Cl")

                    print("Reserva confirmada.")
                    print("")
        if rta == 2:
            habitacion = self.chequear_disponibilidad("doble", reserva)
            if habitacion != reserva.habitacion:
                print(f"¿Desea confirmar la reserva? Precio: ${str(int(habitaciones_desc[1][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))}")
                print("1. Si")
                print("2. No")
                rta = validar_respuesta_menu(2)

                if rta == 1:
                    reserva.habitacion = habitacion
                    reserva.tipo = "doble"
                    reserva.precio = str(int(habitaciones_desc[1][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))

                    matriz=csvtomatriz("reservas.csv")
                    for i in range(len(matriz)):
                        if reserva.numero_res == matriz[i][0]:
                            matriz[i][2] = habitacion
                            matriz[i][3] = "doble"
                            matriz[i][11] = reserva.precio
                    matriztocsv("reservas.csv", matriz,"R")

                    for i in range(len(habitaciones_desc)):
                        if habitaciones_desc[i][0] == reserva.tipo:
                            precio = int(habitaciones_desc[i][1])
                            break

                    matriz=csvtomatriz("clientes.csv")
                    for i in range(len(matriz)):
                        if self.DNI == matriz[i][2]:
                            self.gastos = str(int(self.gastos) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                            matriz[i][6] = str(int(matriz[i][6]) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                    matriztocsv("clientes.csv", matriz,"Cl")
                    
                    print("Reserva confirmada.")
                    print("")
        if rta == 3:
            habitacion = self.chequear_disponibilidad("suite", reserva)
            if habitacion != reserva.habitacion:
                print(f"¿Desea confirmar la reserva? Precio: ${str(int(habitaciones_desc[2][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))}")
                print("1. Si")
                print("2. No")
                rta = validar_respuesta_menu(2)

                if rta == 1:
                    reserva.habitacion = habitacion
                    reserva.tipo = "suite"
                    reserva.precio = str(int(habitaciones_desc[2][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))

                    matriz=csvtomatriz("reservas.csv")
                    for i in range(len(matriz)):
                        if reserva.numero_res == matriz[i][0]:
                            matriz[i][2] = habitacion
                            matriz[i][3] = "suite"
                            matriz[i][11] = reserva.precio
                    matriztocsv("reservas.csv", matriz,"R")

                    for i in range(len(habitaciones_desc)):
                        if habitaciones_desc[i][0] == reserva.tipo:
                            precio = int(habitaciones_desc[i][1])
                            break

                    matriz=csvtomatriz("clientes.csv")
                    for i in range(len(matriz)):
                        if self.DNI == matriz[i][2]:
                            self.gastos = str(int(self.gastos) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                            matriz[i][6] = str(int(matriz[i][6]) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                    matriztocsv("clientes.csv", matriz,"Cl")

                    print("Reserva confirmada.")
                    print("")
        if rta == 4:
            habitacion = self.chequear_disponibilidad("familiar", reserva)
            if habitacion != reserva.habitacion:
                print(f"¿Desea confirmar la reserva? Precio: ${str(int(habitaciones_desc[3][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))}")
                print("1. Si")
                print("2. No")
                rta = validar_respuesta_menu(2)

                if rta == 1:
                    reserva.habitacion = habitacion
                    reserva.tipo = "familiar"
                    reserva.precio = str(int(habitaciones_desc[3][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))

                    matriz=csvtomatriz("reservas.csv")
                    for i in range(len(matriz)):
                        if reserva.numero_res == matriz[i][0]:
                            matriz[i][2] = habitacion
                            matriz[i][3] = "familiar"
                            matriz[i][11] = reserva.precio
                    matriztocsv("reservas.csv", matriz,"R")

                    for i in range(len(habitaciones_desc)):
                        if habitaciones_desc[i][0] == reserva.tipo:
                            precio = int(habitaciones_desc[i][1])
                            break

                    matriz=csvtomatriz("clientes.csv")
                    for i in range(len(matriz)):
                        if self.DNI == matriz[i][2]:
                            self.gastos = str(int(self.gastos) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                            matriz[i][6] = str(int(matriz[i][6]) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                    matriztocsv("clientes.csv", matriz,"Cl")

                    print("Reserva confirmada.")
                    print("")
        if rta == 5:
            self.modificar_reserva(reserva)
        
    def chequear_disponibilidad(self, tipo, reserva):

        habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")
        reservas = csvtomatriz("reservas.csv")
        habitaciones = csvtomatriz("habitaciones.csv")

        # Agrego a filtradas las habitaciones del tipo seleccionado
        habitaciones_filtradas = []
        for i in range(len(habitaciones)):
            if habitaciones[i][1] == tipo:
                habitaciones_filtradas.append(habitaciones[i])
        
        #Agrego una columna a habitaciones que digan "disponible"
        for i in range(len(habitaciones_filtradas)):
            habitaciones_filtradas[i].append("disponible")

        # Chequeo que la cantidad de personas esté ok
        
        # Busco la fila del tipo de habitación seleccionado
        for i in range(len(habitaciones_desc)):
            if habitaciones_desc[i][0] == tipo:
                nro_tipo = i
                break

        if int(reserva.cant_personas) > int(habitaciones_desc[nro_tipo][2]):
            print("La cantidad de personas supera la capacidad máxima de la habitación.")
            print("")
            return reserva.habitacion
        
        # Chequeo que el tipo de habitación sea distinto al actual
        if reserva.tipo == tipo:
            print("El tipo de habitación seleccionado es el misma que el actual.")
            print("")
            return reserva.habitacion
        
        # Chequeo que haya alguna habitación del tipo nuevo disponible
        for i in range(len(habitaciones_filtradas)):
            for j in range(len(reservas)):
                if reservas[j][2] == habitaciones_filtradas[i][0]:
                    if strtodatime(reservas[j][4]) <= strtodatime(reserva.fecha_egr):
                        if strtodatime(reservas[j][5]) >= strtodatime(reserva.fecha_ing):
                            habitaciones_filtradas[i][2] = "no disponible"
        
        # Recorro las habitaciones a ver si hay una disponible y asigno la primera que encuentre
        for i in range(len(habitaciones_filtradas)):
            if habitaciones_filtradas[i][2] == "disponible":
                print("Habitación asignada:", habitaciones_filtradas[i][0])
                return habitaciones_filtradas[i][0]
        
        # Si no hay habitaciones disponibles, retorno la que haya estaba
        print("No hay habitaciones disponibles del tipo seleccionado.")
        print("")
        return reserva.habitacion

    def elegir_cantidad_personas(self, reserva):
        habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")
        
        # Cantidad máxima segun el tipo
        for i in range(len(habitaciones_desc)):
            if habitaciones_desc[i][0] == reserva.tipo:
                cant_max = habitaciones_desc[i][2]
                break
        
        # Pido la cantidad de personas
        cant_personas = input("Ingrese la cantidad de personas. Presione 0 para cancelar: ")
        
        # Chequeo que sea un número
        while not cant_personas.isdigit():
            cant_personas = input("Cantidad no válida, ingrese otra. Presione 0 para cancelar: ")

        if cant_personas == "0":
            print("Cancelando...")
            print("")
        elif int(cant_personas) > int(cant_max):
            print("La cantidad de personas supera la capacidad máxima de la habitación.")
            print("")
        else:
            print("Cantidad de personas asignada:", cant_personas)
            print("¿Desea confirmar la modificación?")
            print("1. Si")
            print("2. No")
            rta = validar_respuesta_menu(2)
            if rta == 1:
                reserva.cant_personas = cant_personas
                matriz=csvtomatriz("reservas.csv")
                for i in range(len(matriz)):
                    if reserva.numero_res == matriz[i][0]:
                        matriz[i][6] = cant_personas
                matriztocsv("reservas.csv", matriz,"R")
                print("Modificación confirmada.")
                print("")
       
    def modificar_ingreso(self, reserva,costo_actual):

        ing_nuevo = validar_fec("Ingrese la nueva fecha de ingreso (DD/MM/AAAA): ")

        # Chequeo que la fecha de ingreso sea posterior a la actual
        if strtodatime(ing_nuevo) < dt.datetime.now():
            print("La fecha de ingreso debe ser posterior a la actual.")
            print("")
        # Chequeo que la fecha de ingreso sea anterior a la de egreso
        elif strtodatime(ing_nuevo) > strtodatime(reserva.fecha_egr):
            print("La fecha de ingreso debe ser anterior a la de egreso.")
            print("")
        else:
            habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")
            reservas = csvtomatriz("reservas.csv")
            habitaciones = csvtomatriz("habitaciones.csv")

            # Agrego a filtradas las habitaciones del tipo seleccionado
            habitaciones_filtradas = []
            for i in range(len(habitaciones)):
                if habitaciones[i][1] == reserva.tipo:
                    habitaciones_filtradas.append(habitaciones[i])
            
            #Agrego una columna a habitaciones que digan "disponible"
            for i in range(len(habitaciones_filtradas)):
                habitaciones_filtradas[i].append("disponible")
            
            # Chequeo que haya alguna disponible
            for i in range(len(habitaciones_filtradas)):
                for j in range(len(reservas)):
                    if reservas[j][2] == habitaciones_filtradas[i][0] and reservas[j][0] != reserva.numero_res:
                        if strtodatime(reservas[j][4]) <= strtodatime(reserva.fecha_egr):
                            if strtodatime(reservas[j][5]) >= strtodatime(ing_nuevo):
                                habitaciones_filtradas[i][2] = "no disponible"
            
            for i in range(len(habitaciones_desc)):
                            if habitaciones_desc[i][0] == reserva.tipo:
                                precio = int(habitaciones_desc[i][1])
                                break
            
            # Recorro las habitaciones a ver si hay una disponible y asigno la primera que encuentre
            for i in range(len(habitaciones_filtradas)):
                if habitaciones_filtradas[i][2] == "disponible":
                    print("Habitación asignada:", habitaciones_filtradas[i][0])
                    print(f"¿Desea confirmar la reserva? Precio: ${precio* (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days})")
                    print("1. Si")
                    print("2. No")
                    rta = validar_respuesta_menu(2)
                    if rta == 1:
                        reserva.habitacion = habitaciones_filtradas[i][0]
                        reserva.fecha_ing = ing_nuevo
                        reserva.precio = str(int(habitaciones_desc[i][1])* int((strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days))
                        matriz=csvtomatriz("reservas.csv")
                        for j in range(len(matriz)):
                            if reserva.numero_res == matriz[j][0]:
                                matriz[j][2] = habitaciones_filtradas[i][0]
                                matriz[j][4] = ing_nuevo
                                matriz[j][11] = reserva.precio
                        matriztocsv("reservas.csv", matriz,"R")

                        matriz=csvtomatriz("clientes.csv")
                        for i in range(len(matriz)):
                            if self.DNI == matriz[i][2]:
                                self.gastos = str(int(self.gastos) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                                matriz[i][6] = str(int(matriz[i][6]) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                        matriztocsv("clientes.csv", matriz,"Cl")

                        print("Reserva confirmada.")
                        break
                    
            
            # Si no hay habitaciones disponibles, retorno la que haya estaba
            print("No hay habitaciones disponibles para la fecha asignada.")
            print("")

    def modificar_egreso(self, reserva,costo_actual):
        
        egr_nuevo = validar_fec("Ingrese la nueva fecha de egreso (DD/MM/AAAA): ")

        # Chequeo que la fecha de ingreso sea posterior a la actual
        if strtodatime(egr_nuevo) < dt.datetime.now():
            print("La fecha de egreso debe ser posterior a la actual.")
            print("")
        # Chequeo que la fecha de ingreso sea posterior a la de ingreso
        elif strtodatime(reserva.fecha_ing) > strtodatime(egr_nuevo)  :
            print("La fecha de ingreso debe ser posterior a la de ingreso.")
            print("")
        else:
            habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")
            reservas = csvtomatriz("reservas.csv")
            habitaciones = csvtomatriz("habitaciones.csv")

            # Agrego a filtradas las habitaciones del tipo seleccionado
            habitaciones_filtradas = []
            for i in range(len(habitaciones)):
                if habitaciones[i][1] == reserva.tipo:
                    habitaciones_filtradas.append(habitaciones[i])
            
            #Agrego una columna a habitaciones que digan "disponible"
            for i in range(len(habitaciones_filtradas)):
                habitaciones_filtradas[i].append("disponible")
            
            # Chequeo que haya alguna disponible
            for i in range(len(habitaciones_filtradas)):
                for j in range(len(reservas)):
                    if reservas[j][2] == habitaciones_filtradas[i][0] and reservas[j][0] != reserva.numero_res:
                        if strtodatime(reservas[j][4]) <= strtodatime(egr_nuevo):
                            if strtodatime(reservas[j][5]) >= strtodatime(reserva.fecha_ing):
                                habitaciones_filtradas[i][2] = "no disponible"
            
            for i in range(len(habitaciones_desc)):
                        if habitaciones_desc[i][0] == reserva.tipo:
                            precio = int(habitaciones_desc[i][1])
                            break
            
            # Recorro las habitaciones a ver si hay una disponible y asigno la primera que encuentre
            for i in range(len(habitaciones_filtradas)):
                if habitaciones_filtradas[i][2] == "disponible":
                    print("Habitación asignada:", habitaciones_filtradas[i][0])
                    print(f"¿Desea confirmar la reserva? Precio: ${precio* (strtodatime(egr_nuevo) - strtodatime(reserva.fecha_ing)).days})")
                    print("1. Si")
                    print("2. No")
                    rta = validar_respuesta_menu(2)
                    if rta == 1:
                        reserva.habitacion = habitaciones_filtradas[i][0]
                        reserva.fecha_egr = egr_nuevo
                        reserva.precio = str(int(habitaciones_desc[i][1])* int((strtodatime(egr_nuevo) - strtodatime(reserva.fecha_ing)).days))
                        matriz=csvtomatriz("reservas.csv")
                        for j in range(len(matriz)):
                            if reserva.numero_res == matriz[j][0]:
                                matriz[j][2] = habitaciones_filtradas[i][0]
                                matriz[j][5] = egr_nuevo
                                matriz[j][11] = reserva.precio
                        matriztocsv("reservas.csv", matriz,"R")

                    matriz=csvtomatriz("clientes.csv")
                    for i in range(len(matriz)):
                        if self.DNI == matriz[i][2]:
                            self.gastos = str(int(self.gastos) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                            matriz[i][6] = str(int(matriz[i][6]) + precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days - costo_actual)
                    matriztocsv("clientes.csv", matriz,"Cl")

                    print("Reserva confirmada.")
                    self.modificar_reserva(reserva)
                    exit()
                    
            
            # Si no hay habitaciones disponibles, retorno la que haya estaba
            print("No hay habitaciones disponibles para la fecha asignada.")
            print("")

    def checkin(self, reserva):

        if reserva.checkin == "si":
            print("Ya realizó el check in")
            print("")
            menu_reserva_actual(self, reserva)
            fecha=dt.datetime.now()
            fecha2=strtodatime(reserva.fecha_ing)
        elif reserva.fecha_ing != dt.datetime.today().strftime("%d/%m/%Y"):
            print("No puede realizar el check una fecha distinta al del ingrso")
            print("")
            menu_reserva_actual(self, reserva)
        else:
            print("¿Desea realizar el check in?")
            print("1. Si")
            print("2. No")
            rta = validar_respuesta_menu(2)
            if rta == 1:
                reserva.checkin = "si"
                reserva.horario_checkin = dt.datetime.now().strftime("%H:%M")
                matriz=csvtomatriz("reservas.csv")
                for i in range(len(matriz)):
                    if reserva.numero_res == matriz[i][0]:
                        matriz[i][7] = "si"
                        matriz[i][9] = dt.datetime.now().strftime("%H:%M")
                matriztocsv("reservas.csv", matriz,"R")
                print("Check in realizado.")
                print("")
                menu_reserva_actual(self, reserva)
            else:
                menu_reserva_actual(self, reserva)

    def checkout(self, reserva):
        if reserva.checkout == "si":
            print("Ya realizó el check out")
            print("")
            menu_reserva_actual(self, reserva)
        elif reserva.checkin == "no":
            print("No puede realizar el check out sin haber realizado el check in")
            print("")
            menu_reserva_actual(self, reserva)
        elif strtodatime(reserva.fecha_egr) != dt.datetime.now():
            print("No puede realizar el check out si no es la fecha de egreso")
            print("")
            menu_reserva_actual(self, reserva)
        else:
            print("¿Desea realizar el check out?")
            print("1. Si")
            print("2. No")
            rta = validar_respuesta_menu(2)
            if rta == 1:
                reserva.checkout = "si"
                reserva.horario_checkout = dt.datetime.now().strftime("%H:%M")
                matriz=csvtomatriz("reservas.csv")
                for i in range(len(matriz)):
                    if reserva.numero_res == matriz[i][0]:
                        matriz[i][8] = "si"
                        matriz[i][10] = dt.datetime.now().strftime("%H:%M")
                matriztocsv("reservas.csv", matriz,"R")
                print("Check out realizado.")
                print("")
                menu_reserva_actual(self, reserva)
            else:
                menu_reserva_actual(self, reserva)

    def cancelar_reserva(self, reserva):
        print("¿Está seguro que desea cancelar la reserva?")
        print("1. Si")
        print("2. No")
        rta = validar_respuesta_menu(2)
        if rta == 1:

            habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")

            # Calculo el precio según el tipo de res
            for i in range (len(habitaciones_desc)):
                if habitaciones_desc[i][0] == reserva.tipo:
                    precio = int(habitaciones_desc[i][1])
                    break

            matriz=csvtomatriz("clientes.csv")
            for i in range(len(matriz)):
                if self.DNI == matriz[i][2]:
                    self.gastos = str(int(self.gastos) - precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days)
                    matriz[i][6] = str(int(matriz[i][6]) - precio * (strtodatime(reserva.fecha_egr) - strtodatime(reserva.fecha_ing)).days)
            matriztocsv("clientes.csv", matriz,"Cl")

            matriz=csvtomatriz("reservas.csv")
            matriz_nueva = []
            for i in range(len(matriz)):
                if reserva.numero_res != matriz[i][0]:
                    matriz_nueva.append(matriz[i])
            matriztocsv("reservas.csv", matriz_nueva,"R")
            print("Reserva cancelada.")
            print("")
            menu_reservas(self)
        else:
            menu_reserva_actual(self, reserva)
        
    def nueva_reserva(self):
        
        print("Iniciando una nueva reserva...")
        print("")
        
        nueva_reserva = Reserva(None, self.DNI, None, None, None, None, None, None, None, None, None)

        reservas=csvtomatriz("reservas.csv")
        nueva_reserva.numero_res = str(int(reservas[-1][0]) + 1)
        
        habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")

        print("Habitaciones disponibles:")
        print(f"1. Habitación Simple: Precio ${habitaciones_desc[0][1]} por noche. Capacidad máxima: 1 persona. 1 cama individual. Baño compartido. No tiene ventana balcón")
        print(f"2. Habitación Doble: Precio ${habitaciones_desc[1][1]} por noche. Capacidad máxima: 2 personas. 1 cama matrimonial. Baño compartido. No tiene ventana balcón")
        print(f"3. Suite: Precio ${habitaciones_desc[2][1]} por noche. Capacidad máxima: 2 personas. 1 cama matrimonial. Baño privado. Tiene ventana balcón")
        print(f"4. Habitación Familiar: Precio ${habitaciones_desc[3][1]} por noche. Capacidad máxima: 4 personas. 2 camas individuales y 1 cama matrimonial. Baño privado. Tiene ventana balcón")
        print("5. Volver")
        rta = validar_respuesta_menu(5)

        if rta == 1:
            nueva_reserva.tipo = "simple"
        elif rta == 2:
            nueva_reserva.tipo = "doble"
        elif rta == 3:
            nueva_reserva.tipo = "suite"
        elif rta == 4:
            nueva_reserva.tipo = "familiar"
        
        if rta < 5:
            
            # Cantidad máxima segun el tipo
            for i in range(len(habitaciones_desc)):
                if habitaciones_desc[i][0] == nueva_reserva.tipo:
                    cant_max = habitaciones_desc[i][2]
                    break
            
            # Pido la cantidad de personas
            cant_personas = input("Ingrese la cantidad de personas. Presione 0 para cancelar: ")
            
            # Chequeo que sea un número menor a la cant máxima
            while not cant_personas.isdigit() or int(cant_max) < int(cant_personas):
                if not cant_personas.isdigit():
                    cant_personas = input("Cantidad no válida, ingrese otra. Presione 0 para cancelar: ")
                else:
                    cant_personas = input("La cantidad de personas supera la capacidad máxima de la habitación. Ingrese otra. Presione 0 para cancelar: ")

            if cant_personas == "0":
                print("Cancelando...")
                print("")
            else:
                print("Cantidad de personas asignada:", cant_personas)
                nueva_reserva.cant_personas = cant_personas

                # Pido la fecha de ingreso
                fecha_ing = validar_fec("Ingrese la fecha de ingreso (DD/MM/AAAA): ")

                # Chequeo que la fecha de ingreso sea posterior a la actual
                while strtodatime(fecha_ing) < dt.datetime.now():
                    print("La fecha de ingreso debe ser posterior a la actual.")
                    fecha_ing = validar_fec("Ingrese la fecha de ingreso (DD/MM/AAAA): ")
                
                nueva_reserva.fecha_ing = fecha_ing

                # Pido la fecha de egreso
                fecha_egr = validar_fec("Ingrese la fecha de egreso (DD/MM/AAAA): ")

                # Chequeo que la fecha de egreso sea posterior a la de ingreso
                while strtodatime(fecha_ing) > strtodatime(fecha_egr):
                    print("La fecha de egreso debe ser posterior a la de ingreso.")
                    fecha_egr = validar_fec("Ingrese la fecha de egreso (DD/MM/AAAA): ")
                
                nueva_reserva.fecha_egr = fecha_egr

                # Chequeo que haya alguna habitación disponible
                habitaciones = csvtomatriz("habitaciones.csv")
                reservas = csvtomatriz("reservas.csv")
                habitaciones_desc = csvtomatriz("habitaciones_descripciones.csv")

                # Agrego a filtradas las habitaciones del tipo seleccionado
                habitaciones_filtradas = []
                for i in range(len(habitaciones)):
                    if habitaciones[i][1] == nueva_reserva.tipo:
                        habitaciones_filtradas.append(habitaciones[i])
                
                #Agrego una columna a habitaciones que digan "disponible"
                for i in range(len(habitaciones_filtradas)):
                    habitaciones_filtradas[i].append("disponible")
                
                # Chequeo que haya alguna disponible
                for i in range(len(habitaciones_filtradas)):
                    for j in range(len(reservas)):
                        if reservas[j][2] == habitaciones_filtradas[i][0]:
                            if strtodatime(reservas[j][4]) <= strtodatime(fecha_egr):
                                if strtodatime(reservas[j][5]) >= strtodatime(fecha_ing):
                                    habitaciones_filtradas[i][2] = "no disponible"
                
                # Recorro las habitaciones a ver si hay una disponible y asigno la primera que encuentre
                for i in range(len(habitaciones_filtradas)):
                    if habitaciones_filtradas[i][2] == "disponible":
                        print("Habitación asignada:", habitaciones_filtradas[i][0])
                        print("¿Desea confirmar la reserva?")
                        print("1. Si")
                        print("2. No")
                        rta = validar_respuesta_menu(2)
                        if rta == 1:
                            nueva_reserva.habitacion = habitaciones_filtradas[i][0]
                            nueva_reserva.checkin = "no"
                            nueva_reserva.checkout = "no"
                            self.reservas.append(nueva_reserva)
                            matriz=csvtomatriz("reservas.csv")
                            matriz.append([nueva_reserva.numero_res, nueva_reserva.dni_cliente, nueva_reserva.habitacion, nueva_reserva.tipo, nueva_reserva.fecha_ing, nueva_reserva.fecha_egr, nueva_reserva.cant_personas, "no", "no","no","no"])
                            matriztocsv("reservas.csv", matriz,"R")
                            print("Reserva confirmada.")

                            matriz=csvtomatriz("clientes.csv")
                            for j in range(len(matriz)):
                                if self.DNI == matriz[j][2]:
                                    self.gastos = str(int(self.gastos) + int(habitaciones_desc[i][1]) * (strtodatime(nueva_reserva.fecha_egr) - strtodatime(nueva_reserva.fecha_ing)).days)
                                    matriz[j][6] = str(int(matriz[j][6]) + int(habitaciones_desc[i][1]) * (strtodatime(nueva_reserva.fecha_egr) - strtodatime(nueva_reserva.fecha_ing)).days)
                            matriztocsv("clientes.csv", matriz,"Cl")
                            print("")
                            menu_reservas(self)
                            break          

        menu_reservas(self) 

    def consumir(self):
        
        consumo = Consumo(None, self.DNI, dt.datetime.today().strftime("%d/%m/%Y"), None, None, None)

        consumiciones = csvtomatriz("consumiciones.csv")

        print("¿Qué desea consumir?")
        print("1. Bebida")
        print("2. Comida")
        print("3. Postre")
        print("4. Volver")
        rta = validar_respuesta_menu(4)
        
        if rta == 1:
            consumo.item = "bebida"
            for i in consumiciones:
                if i[0] == "bebida":
                    precio = int(i[1])
        elif rta == 2:
            consumo.item = "comida"
            for i in consumiciones:
                if i[0] == "comida":
                    precio = int(i[1])
        elif rta == 3:
            consumo.item = "postre"
            for i in consumiciones:
                if i[0] == "postre":
                    precio = int(i[1])
        
        if rta < 4:
            cantidad = input("Ingrese la cantidad: ")
            while not cantidad.isdigit():
                cantidad = input("Cantidad no válida, ingrese otra: ")
            consumo.cantidad = cantidad
            consumo.precio = str(precio * int(cantidad))

            print ("¿Desea confirmar el consumo?")
            print (f"Precio: ${consumo.precio}")
            print("1. Si")
            print("2. No")

            rta = validar_respuesta_menu(2)

            if rta == 1:

                matriz=csvtomatriz("consumos.csv")
                consumo.numero_pedido = str(int(matriz[-1][0]) + 1)

                matriz.append([consumo.numero_pedido, consumo.cliente, consumo.fecha, consumo.item, consumo.cantidad, consumo.precio])
                matriztocsv("consumos.csv", matriz,"Con")

                matriz = csvtomatriz("clientes.csv")
                for i in range(len(matriz)):
                    if self.DNI == matriz[i][2]:
                        self.gastos = str(int(self.gastos) + int(consumo.precio))
                        matriz[i][6] = str(int(matriz[i][6]) + int(consumo.precio))

                matriztocsv("clientes.csv", matriz,"Cl")

                print("Consumo confirmado.")
                print("")

            else:
                print("Cancelando...")
                print("")
        
        menu_consumos(self)

class Empleado(Persona):
    def __init__(self, nombre, apellido, DNI, mail, password, fec_nac, area, activo):
        super().__init__(nombre, apellido, DNI, mail, password, fec_nac)
        self.area = area
        self.activo = activo

        

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nMail: {self.mail}\nFecha de nacimiento: {self.fec_nac}\nArea: {self.area}\nStatus: {self.activo}"

    def ingreso(self):

        ingresos = csvtomatriz("ingresos_egresos.csv")
        
        # Me fijo si ingresó hoy
        ingreso = False
        for i in range(len(ingresos)):
            if ingresos[i][1] == self.DNI and ingresos[i][2] == dt.datetime.today().strftime("%d/%m/%Y"):
                print("Ya ingresó hoy.")
                print("")
                ingreso = True
                menu_empleado(self)
        
        # Si no ingresó, lo agrego
        if not ingreso:
            ingresos.append([str(int(ingresos[-1][0]) + 1), self.DNI, dt.datetime.today().strftime("%d/%m/%Y"), dt.datetime.now().strftime("%H:%M"), "No"])
            matriztocsv("ingresos_egresos.csv", ingresos,"IE")
            print("Ingreso registrado.")
            print("")
            menu_empleado(self)

    def egreso(self):

        egresos = csvtomatriz("ingresos_egresos.csv")

        # Me fijo si ingresó hoy
        ingreso = False
        for i in range(len(egresos)):
            if egresos[i][1] == self.DNI and egresos[i][2] == dt.datetime.today().strftime("%d/%m/%Y"):
                if egresos[i][4] != "No":
                    print("Ya egresó hoy.")
                    print("")
                    ingreso = True
                    menu_empleado(self)
                else:
                    egresos[i][4] = dt.datetime.now().strftime("%H:%M")
                    matriztocsv("ingresos_egresos.csv", egresos,"IE")
                    print("Egreso registrado.")
                    print("")
                    menu_empleado(self)
        
        # Si no ingresó, no puede efectuar el egreso
        if not ingreso:
            print("No puede registrar un egreso sin haber ingresado.")
            print("")


    def modificar_datos_personales(self):
        print("¿Qué dato desea modificar?")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Mail")
        print("4. Contraseña")
        print("5. Fecha de nacimiento")
        print("6. Volver atras")
        print("7. Salir")
        rta=validar_respuesta_menu(7)
        matriz_empleados = csvtomatriz("empleados.csv")

        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][0] = self.nombre
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][1] = self.apellido
        elif rta == 3:
            self.mail = validar_mail()
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][3] = self.mail
        elif rta == 4:
            password=self.cambiar_password()
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][4] = password
        elif rta == 5:
            self.fec_nac=validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA):")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][5] = self.fec_nac
        if rta < 6:
            matriztocsv("empleados.csv", matriz_empleados,"E")
            print("Modificación realizada.")
            print("")
            self.modificar_datos_personales()
        elif rta == 6: 
            menu_datos_personales(self)
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
        print("3. Mail")
        print("4. Contraseña")
        print("5. Fecha de nacimiento")
        print("6. Area")
        print("7. Estado")
        print("8. Volver atras")
        print("9. Salir")
        rta=validar_respuesta_menu(9)
        matriz_empleados = csvtomatriz("empleados.csv")

        if rta == 1:
            self.nombre=input("Ingrese su nuevo nombre: ")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][0] = self.nombre
        elif rta == 2:
            self.apellido=input("Ingrese su nuevo apellido: ")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][1] = self.apellido
        elif rta == 3:
            self.mail = validar_mail()
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][3] = self.mail
        elif rta == 4:
            password=self.cambiar_password()
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][4] = password
        elif rta == 5:
            self.fec_nac=validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA):")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][5] = self.fec_nac
        elif rta == 6:
            self.area=input("Ingrese su nueva area de trabajo: ")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][6] = self.area
        elif rta == 7:
            self.activo=input("Ingrese su nuevo status: ")
            for i in range(len(matriz_empleados)):
                if self.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][1] = self.activo
        
        if rta < 8:
            matriztocsv("empleados.csv", matriz_empleados,"E")
            print("Modificación realizada.")
            print("")
            self.modificar_datos_personales()
        
        elif rta == 8: 
            menu_gerente(self)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()
    
    def actualizar_tipo_clientes(self):
        # El tipo de cliente varía según sus gastos totales
        # De 0 a 5000: Basico
        # De 5000 a 10000: Regular
        # De 10000 a 20000: Premium
        # Más de 20000: Gold

        matriz_clientes = csvtomatriz("clientes.csv")

        for i in range(len(matriz_clientes)):
            if int(matriz_clientes[i][6]) < 5000:
                matriz_clientes[i][7] = "Basico"
            elif int(matriz_clientes[i][6]) < 10000:
                matriz_clientes[i][7] = "Regular"
            elif int(matriz_clientes[i][6]) < 20000:
                matriz_clientes[i][7] = "Premium"
            else:
                matriz_clientes[i][7] = "Gold"
        
        matriztocsv("clientes.csv", matriz_clientes,"Cl")

        print ("Tipos de clientes actualizados.")
        print("")
        menu_gerente(self)

    def agregar_empleado(self, matriz_empleados):
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

    def modificarEmpleado(self,empleado):
        print("¿Qué dato desea modificar?")
        print(f"1. Nombre: {empleado.nombre}")
        print(f"2. Apellido: {empleado.apellido}")
        print(f"3. Mail: {empleado.mail}")
        print(f"4. Contraseña: {empleado.password}")
        print(f"5. Fecha de nacimiento: {empleado.fec_nac}")
        print(f"6. Area: {empleado.area}")
        print(f"7. Estado: {empleado.activo}")
        print("8. Volver atras")
        print("9. Salir")

        rta=validar_respuesta_menu(9)
        matriz_empleados = csvtomatriz("empleados.csv")

        if rta == 1:
            empleado.nombre=input("Ingrese su nuevo nombre: ")
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                        matriz_empleados[i][0] = empleado.nombre
        elif rta == 2:
            empleado.apellido=input("Ingrese su nuevo apellido: ")
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                        matriz_empleados[i][1] = empleado.apellido
        elif rta == 3:
            empleado.mail = validar_mail()
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][3] = empleado.mail
        elif rta == 4:
            password=empleado.cambiar_password()
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                        matriz_empleados[i][4] = password
        elif rta == 5:
            empleado.fec_nac=validar_fec("Ingrese su fecha de nacimiento (DD/MM/AAAA):")
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                        matriz_empleados[i][5] = empleado.fec_nac
            
        elif rta == 6:
            empleado.area=input("Ingrese su nueva area de trabajo: ")
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                        matriz_empleados[i][6] = empleado.area
        elif rta == 7:
            empleado.activo=input("Ingrese su nuevo status: ")
            for i in range(len(matriz_empleados)):
                if empleado.DNI == matriz_empleados[i][2]:
                    matriz_empleados[i][1] = empleado.activo
            
        if rta < 8:
            matriztocsv("empleados.csv", matriz_empleados,"E")
            print("Modificación realizada.")
            print("")
            empleado.modificar_datos_personales()
            
        elif rta == 8: 
            menu_administracion_personal(self)
        else:
            print("Gracias por utilizar nuestros servicios. Hasta pronto.")
            exit()
    
    def porcentaje_ocupacion(self,tipo):

        reservas = csvtomatriz("reservas.csv")
        habitaciones = csvtomatriz("habitaciones.csv")

        if tipo == None:
            total_habitaciones = len(habitaciones)
            habitaciones_ocupadas = 0
            for i in range(len(reservas)):
                if strtodatime(reservas[i][4]) <= dt.datetime.today() and strtodatime(reservas[i][5]) >= dt.datetime.today():
                    habitaciones_ocupadas += 1
            
            if total_habitaciones == 0:
                porcentaje = 0
            else:
                # Dos decimales
                porcentaje = str(round(habitaciones_ocupadas * 100 / total_habitaciones, 2))
                  
            print(f"El porcentaje de ocupación el día de hoy es del: {porcentaje}%. Están ocupadas {habitaciones_ocupadas} habitaciones de un total de {total_habitaciones}.")
            print("")
        else:
            total_habitaciones = 0
            habitaciones_ocupadas = 0
            for i in range(len(habitaciones)):
                if habitaciones[i][1] == tipo:
                    total_habitaciones += 1
            for i in range(len(reservas)):
                if strtodatime(reservas[i][4]) <= dt.datetime.today() and strtodatime(reservas[i][5]) >= dt.datetime.today() and reservas[i][3] == tipo:
                    habitaciones_ocupadas += 1
            
            if total_habitaciones == 0:
                porcentaje = 0
            else:
                porcentaje = str(round(habitaciones_ocupadas * 100 / total_habitaciones, 2))
            
            print(f"El porcentaje de ocupación de las habitaciones de tipo {tipo} el día de hoy es del: {porcentaje}%. Están ocupadas {habitaciones_ocupadas} habitaciones de un total de {total_habitaciones}.")
            print("")

    def cantidad_clientes(self,tipo):
        clientes = csvtomatriz("clientes.csv")
        total_clientes = len(clientes)
        total_tipo = 0
        for i in range(len(clientes)):
            if clientes[i][7] == tipo:
                total_tipo += 1
        
        if total_clientes == 0:
            porcentaje = 0
        else:
            porcentaje = str(round(total_tipo * 100 / total_clientes, 2))

        print(f"El porcentaje de clientes de tipo {tipo} es del: {porcentaje}%. Hay {total_tipo} clientes de un total de {total_clientes}.")
        print("")

    def recaudacion_diaria(self,fecha):
        # Se asume que la recaudación de las reservas se hace ese mismo día

        reservas = csvtomatriz("reservas.csv")
        consumos = csvtomatriz("consumos.csv")

        recaudacion = 0

        for i in range(len(reservas)):
            if strtodatime(reservas[i][4]) == fecha:
                recaudacion += int(reservas[i][11])
        
        for i in range(len(consumos)):
            if strtodatime(consumos[i][2]) == fecha:
                recaudacion += int(consumos[i][5])

        if fecha == dt.datetime.today().strftime("%d/%m/%Y"):
            print(f"La recaudación de hoy es de ${recaudacion}.")
        else:
            print(f"La recaudación del {fecha} es de ${recaudacion}.")

class Reserva():
    def __init__(self, numero_res, dni_cliente, habitacion, tipo, fecha_ing, fecha_egr, cant_personas,checkin,checkout,horario_checkin,horario_checkout,precio):
        self.dni_cliente = dni_cliente
        self.habitacion = habitacion
        self.tipo = tipo
        self.fecha_ing = fecha_ing
        self.fecha_egr = fecha_egr
        self.numero_res = numero_res
        self.cant_personas = cant_personas
        self.checkin = checkin
        self.checkout = checkout
        self.horario_checkin = horario_checkin
        self.horario_checkout = horario_checkout
        self.precio = precio

    def __str__(self) -> str:
        return f"Numero de reserva: {self.numero_res}\nDNI del cliente: {self.dni_cliente}\nHabitacion: {self.habitacion}\nTipo: {self.tipo}\nFecha de ingreso: {self.fecha_ing}\nFecha de egreso: {self.fecha_egr}\nCantidad de personas: {self.cant_personas}\nCheckin: {self.checkin}\nCheckout: {self.checkout}\nHorario de checkin: {self.horario_checkin}\nHorario de checkout: {self.horario_checkout}\nPrecio: ${self.precio}"   

class Consumo():
    def __init__(self, nro_pedido, cliente, fecha, item, cantidad,precio):
        self.numero_pedido = nro_pedido
        self.cliente = cliente
        self.fecha = fecha
        self.item = item
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self) -> str:
        return f"Numero de pedido: {self.numero_pedido}\nCliente: {self.cliente}\nFecha: {self.fecha}\nItem: {self.item}\nCantidad: {self.cantidad}\nPrecio: ${self.precio}"

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
