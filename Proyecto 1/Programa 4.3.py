##bibliotecas
import random
import time
##ordenamos con heap sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#la matriz de 1000 valores en el rango de 1 a 106
arr = [random.randint(1, 10**6) for k in range(1000)]

##tiempos
print("\nEl arreglo inicial es:\n", arr)
T1 = time.time()
heapSort(arr)
T2 = time.time()
print("\nEl arreglo ordenado es:\n", arr)
print("Tiempo: ", (T2 - T1))
