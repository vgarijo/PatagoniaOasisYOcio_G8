'''
def menu_datos_personales(persona):
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

'''

# en la clase Persona, agregar el siguiente método
'''
def __str__(self):
    return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.DNI}\nMail: {self.mail}\nContraseña: {self.password}\nFecha de nacimiento: {self.fec_nac}"
'''
# en el menu_datos_personales donde dice "método para ver datos personales", pones un persona.__str__() para que se vean sus datos

# ___________________________________

# en el menu_datos_personales donde dice "método para modificar datos personales", pones un persona.modificar_datos_personales() para que se abra el menú para modificar sus datos

# ___________________________________

# en el menu_datos_personales donde dice "método para cambiar contraseña", pones un persona.cambiar_password() para que se abra el menú para cambiar su contraseña






'''
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
'''










































































































