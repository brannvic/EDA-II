def countingSort(arr):
    maxValor=max(max(fila) for fila in arr) ##valor maximo
    minValor=min(min(fila) for fila in arr) ##valor minimo
    rangoValor=maxValor-minValor+1 #determina el rango
    counting=[0]*rangoValor
    sortedArr=[[0]*len(arr[0])for _ in range(len(arr))]

    for fila in arr:
        for valor in fila:
            counting[valor-minValor] += 1##contador

    idx=0
    for i in range(rangoValor):##recorrer el arreglo para ordenarlo
        while counting[i]>0:
            sortedArr[idx//len(arr[0])][idx%len(arr[0])]=i+minValor##incrementa para luego ordenar
            counting[i] -= 1
            idx += 1

    return sortedArr

def encontrarElementos(arr1, arr2):
    sortedArr1 = countingSort(arr1)
    sortedArr2 = countingSort(arr2)
    elementos = []##almacena elementos

    for fila1, fila2 in zip(sortedArr1, sortedArr2):##recorre y ordena los elementos no repetidos
        for elemento1, elemento2 in zip(fila1, fila2):
            if elemento1 == elemento2:
                elementos.append(elemento1)##si son iguales los almacena

    return elementos

filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))

arr1 = []
arr2 = []
print("Ingrese los valores del primer arreglo: ")
for i in range(filas):##determina las filas
    fila = []
    for j in range(columnas):##determina las columnas
        value = int(input(f"Valor en la posicion ({i+1}, {j+1}): "))##posiciones de elementos a ordenar
        fila.append(value)
    arr1.append(fila)

print("Ingrese los valores del segundo arreglo: ")
for i in range(filas):
    fila = []
    for j in range(columnas):
        value = int(input(f"Valor en la posicion ({i+1}, {j+1}): "))
        fila.append(value)
    arr2.append(fila)

elementos = encontrarElementos(arr1, arr2)
print("Elementos comunes en ambas matrices ordenadas: ")
for elemento in elementos:
    print(elemento)