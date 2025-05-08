##bibliotecas
import time
import random

##ordenamos con merge sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def imprimir(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# la matriz de 1000 números enteros aleatorios con dígitos de hasta 10^6
arr = [random.randint(1, 10**6) for _ in range(1000)]

print("Arreglo dado:", end="\n")
imprimir(arr)
mergeSort(arr)
print("\nArreglo ordenado:", end="\n")
imprimir(arr)

#tiempo de ejecución
tiempoInicial = time.time()
tiempoFinal = time.time()
tiempoTotal = tiempoFinal - tiempoInicial

print("\nTiempo de ejecución:", tiempoTotal, "segundos")
