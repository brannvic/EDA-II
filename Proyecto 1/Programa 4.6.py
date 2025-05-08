##bibliotecas
import time
from random import randint

tiempoInicial = time.time()

def countingSort(arr, exp1):
    n = len(arr)
    B = [0] * n
    C = [0] * 10

    for i in range(0, n):
        index = int(arr[i] / exp1) + 10
        C[int(index % 10)] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] / exp1) + 10
        B[C[int(index % 10)] - 1] = arr[i]
        C[int(index % 10)] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = B[i]
##ordenamos con radix sort
def radixSort(arr): 
    pos_values = [x for x in arr if x >= 0]
    neg_values = [-x for x in arr if x < 0]

    if pos_values:
        max_pos = max(pos_values)
        exp = 1
        while max_pos / exp > 0:
            countingSort(pos_values, exp)
            exp *= 10

    if neg_values:
        max_neg = max(neg_values)
        exp = 1
        while max_neg / exp > 0:
            countingSort(neg_values, exp)
            exp *= 10

    arr[:] = [-x for x in neg_values[::-1]] + pos_values

##la matriz de 1000 valores enteros con dígitos de hasta 10^6
A = [randint(0, 10**6) for k in range(0, 1000)]

radixSort(A)

print("El arreglo ordenado es:\n")

for i in range(len(A)):
    print(A[i], end=', ')

##tiempos
tiempoFinal = time.time()
tiempoTotal = tiempoFinal - tiempoInicial

print("\nTiempo de ejecución:", tiempoTotal, "segundos")
