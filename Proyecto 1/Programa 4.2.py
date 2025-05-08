##bibliotecas
import time
from random import randint

tiempoInicial = time.time()

##ordenamos con counting sort
def CountingSort(A):
    min_val = min(A)
    max_val = max(A)
 
    C = [0] * (max_val - min_val + 1)

    for num in A:
        C[num - min_val] += 1

    B = []
    for i in range(len(C)):
        B.extend([i + min_val] * C[i])

    return B

A = [randint(1, 10**6) for _ in range(1000)]  
##la matriz de 1000 valores aleatorios entre 1 y 10^6
sorted_list = CountingSort(A)
print("\nLista Ordenada:\n", sorted_list)
print("\nLista Original:\n", A)

##tiempos
tiempoFinal = time.time()
tiempoTotal = tiempoFinal - tiempoInicial

print("\nTiempo de ejecución:", tiempoTotal, "segundos")
