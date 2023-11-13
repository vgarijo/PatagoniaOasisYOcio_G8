from navegandomenus import*


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
    matriz_empleados=csvtomatriz("empleados.csv")
    lista_empleados=stringAempleado(matriz_empleados)
    if rta == 1:
        # método para ver empleados
        pass
    if rta == 2:
        # método para agregar empleado

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

# hago una función para pasar todos los empleados de la matriz a que sean de clase empleado
'''
def stringAempleado(matriz):
    lista_empleados=[]
    for i in range(len(matriz)):
        lista_empleados.append(Empleado(matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3],matriz[i][4],matriz[i][5],matriz[i][6],matriz[i][7]))
    return lista_empleados
'''

# método para ver a los empleados

'''
for i in range(lista_empleados):
    print(lista_empleados[i])
    print('\n')
'''

# método para agregar empleado

'''
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
matriz_empleados.
'''

# método para modificar empleado
'''
dni_requerido=validar_dni()
for empleado in lista_empleados:
    if empleado.DNI==dni_requerido:
        empleado.modificar_datos_personales()
        for i in range(len(matriz_empleados)):
            if dni_requerido==matriz_empleados[i][2]:
                matriz_empleados[i]=[empleado.nombre,empleado.apellido,empleado.DNI,empleado.mail,empleado.password,empleado.fec_nac,empleado.area,empleado.activo]


'''































































































