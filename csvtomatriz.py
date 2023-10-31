'''
Pasar un archivo csv a una matriz del tipo:
nombre;apellido;DNI;mail;password;fec_nac;tipo
Franco;Rossi;43864072;frossi@gmail.com;FRossi123;24/07/2002;premium
Valentin;Garijo;43517955;vgarijo@gmail.com;VGarijo123;11/07/2001;medium
'''


import csv
import numpy as np
import random as rd

def csvtomatriz(archivo):
    with open(archivo) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        matriz = []
        for row in reader:
            matriz.append(row)
    return matriz[1:]

matriz = csvtomatriz('clientes.csv')
print(matriz)