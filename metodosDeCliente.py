from navegandomenus import*
from datetime import*

###### IMPORTANTE ###### hacer una funcion para validar que las fechas de inicio de nuevas reservas sean posteriores a la fecha actual
def validar_reserva(lista_reservas):
    dNi=int(input("Ingrese su DNI (solo numeros, sin puntos): "))
    numero_reserva=int(input("Ingrese el numero de reserva que desee modificar: "))
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0]==dNi and lista_reservas[i][4]==numero_reserva:
            return numero_reserva
    return "No existe dicha reserva."  ## buscar una forma de volver al menu de reservas




def nueva_reserva(self, cant_personas, habitacion, lista_reservas): #cliente, habitacion, fecha_reserva (datetime. now()), fecha_ing, fecha_egr, numero_res, cant_personas
    cliente=self.dni
    hab=habitacion
    fech_res=datetime.now()
    fech_ing=validar_fec()
    fech_egr=validar_fec()
    num_res=len(lista_reservas)
    reservaNueva=Reserva(cliente,hab,fech_res,fech_ing,fech_egr,num_res,cant_personas)
    lista_reservas.append(reservaNueva)


def modificar(self, numero): ### este es el metodo de reservas, después hago el de cliente
    if self.numero==numero:
        print("¿Qué desea modificar?","\n"+"1. Habitacion"+"\n"+"2. Cantidad de Personas"+"\n"+"3. Fecha de Inicio de la Reserva"+"\n"+"4. Fecha de Fin de la Reserva"+"\n"+"5. Volver")
        rta = validar_respuesta_menu(5)
        if rta == 1: #modificar habitacion
            self.habitacion=int(input("Ingrese el nuevo número de habitacion: "))
        elif rta == 2: #modificar cant de personas
            self.cant_personas=int(input("Ingrese el nuevo número de habitacion: ")) # falta checkear que no exceda la cantidad de personas permitidas en la habitación
        elif rta == 3: #modificar fecha de comienzo de reserva
            self.fecha_ing=validar_fec()
        elif rta == 4: #modificar fecha de salida
            self.fecha_egr=validar_fec()
        else:
            menu_reservas()

    
def modificar_reserva(self, lista_reservas):
    numero_deReserva=validar_reserva(lista_reservas)
    






def checkIn(self):
    pass
def checkOut(self):
    pass