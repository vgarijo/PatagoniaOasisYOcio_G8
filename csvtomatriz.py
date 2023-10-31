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