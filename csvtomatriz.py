# Pasar un archivo csv a una matriz

import csv
import numpy as np
import random as rd

def csvtomatriz(archivo):
    with open(archivo) as f:
        reader = csv.reader(f)
        datos = list(reader)
    matriz = np.array(datos)
    return matriz

matriz = csvtomatriz("csvprueba.csv")
print(matriz)

# Modificar matriz. Asigna un nombre aleatorio a la primera fila a partir de una lista de nombres
nombres = ["Julián", "Jorge", "Marcos", "Manuel"]
matriz[0][0] = rd.choice(nombres)
print(matriz)

# Carga la matriz modificada en el csv
def matriztocsv(matriz, archivo):
    with open(archivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(matriz)

matriztocsv(matriz, "csvprueba.csv")
print("Archivo csvprueba.csv modificado")
