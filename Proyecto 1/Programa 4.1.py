##bibliotecas
import random
import time

##matriz de 1000 valores aleatorios en el rango de 0 a 10^6
A = [random.randint(0, 10**6) for _ in range(1000)]

##ordenamos usando bubble sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# medición el tiempo
Ti = time.time()
bubbleSort(A)
Tf = time.time()

#arreglo ordenado y el tiempo de ejecución
print("\nArreglo ordenado:\n", A)
print("Tiempo de ordenación: {:.6f} segundos".format(Tf - Ti))
