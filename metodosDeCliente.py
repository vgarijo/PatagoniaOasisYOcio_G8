from navegandomenus import*
from datetime import*

def nueva_reserva(self, cant_personas, habitacion, lista_reservas): #cliente, habitacion, fecha_reserva (datetime. now()), fecha_ing, fecha_egr, numero_res, cant_personas
    cliente=self.dni
    hab=habitacion
    fech_res=datetime.now()
    fech_ing=datetime(input("Ingrese el día que vendrá al hotel (AA/MM/DD): "))
    fech_egr=datetime(input("Ingrese el día que se retirará al hotel (AA/MM/DD): "))
    num_res=len(lista_reservas)
    reservaNueva=Reserva(cliente,hab,fech_res,fech_ing,fech_egr,num_res,cant_personas)
    lista_reservas.append(reservaNueva)


def modificar_reserva(self):
    print("¿Qué desea modificar?","\n"+"1. Habitacion"+"\n"+"2. Cantidad de Personas"+"\n"+"3. Fecha de Inicio de la Reserva"+"\n"+"4. Fecha de Fin de la Reserva"+"\n"+"5. Volver")
    rta = validar_respuesta_menu(5)
    

    


def checkIn(self):
    pass
def checkOut(self):
    pass