def countingSort(arr,x):
    maxElemento=max(arr[-1])
    ##suponiendo que el maximo elemento esta en la ultima fila
    counting=[0]*(maxElemento+1) #incremento de los elementos
    ##contar las ocurrencias de cada elemento
    for fila in arr: ##para cada fila del arreglo
        for num in fila:
            counting[num]+=1
    
    print("Matriz: ")
    
    for fila in arr:
        print(fila)
    
    print(f"Numero x: {x}")
    print(f"Numero de ocurrencias de {x}: {counting[x]}")

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
arr = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        num = int(input(f"Ingrese el número en la posición ({i+1}, {j+1}): "))
        fila.append(num)
    arr.append(fila)

numeroX = int(input("Ingrese el número x que desea contar: "))

countingSort(arr, numeroX)
