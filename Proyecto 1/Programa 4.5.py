##bibliotecas
import random
import time

def generarNumeroLargo():
    return random.randint(0, 10**6)

def intercambia(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def particionar(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            intercambia(A, i, j)
    intercambia(A, i + 1, r)
    return i + 1
 ##ordenamos con quick sort
def Quicksort(A, p, r):
    if p < r:
        q = particionar(A, p, r)
        Quicksort(A, p, q - 1)
        Quicksort(A, q + 1, r)

# la matriz de 1000 números enteros largos aleatorios
A = [generarNumeroLargo() for _ in range(1000)]

print("Arreglo generado:")
print(A)

T1 = time.time()
Quicksort(A, 0, len(A) - 1)
T2 = time.time()

print("\nArreglo ordenado:")
print(A)

print("\nTiempo de ejecución:", T2 - T1, "segundos")
