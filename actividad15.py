#1. Crea un proyecto en Pycharm llamado actividad15
#2. Crea una archivo python que muestre 10 números aleatorios entre 1 y 100 y los muestre ordenados
import random
import pandas as pd
import matplotlib.pyplot as plt
def listaAleatorios(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(0, 100))
        lista.sort()
    return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n = int(input())

aleatorios = listaAleatorios(n)
print(aleatorios)
#3. Crea otro archivo python que pida una frase y responda cuántas veces está la letra que hayas elegido.
frase=input('Escribe la frase')
letra=input('Que letra quieres contar')

print(f'la frase tiene{frase.count(letra)}')
#4. Busca un archivo csv en internet y muestra un gráfico circular que muestre los datos.

#5. Este proyecto, sus archivos, lo subes a un repositorio Github.

