def countingSort(arr): ##funcion del algoritmo de ordenamiento seleccionado
    maxValor=max(arr) ##determina el valor maximo
    frequenciaCounting=[0]*(maxValor+1) ##conteo de las frecuencias de cada valor
    for num in arr:
        frequenciaCounting[num]+=1 ##incremento en cada valor encontrado
    elementoFrecuenciaPares=[(elemento, frequenciaCounting[elemento]) for elemento in arr]
    ##genera tupas (valor, frecuencia)
    elementoFrecuenciaPares.sort(key=lambda x:(-x[1], arr.index(x[0])))
    ##ordena por frecuencia decreciente, si se repiten coloca primero el original
    sortedArr=[pares[0] for pares in elementoFrecuenciaPares]##crea la lista
    return sortedArr

inputStr = input("Ingrese una lista de números separados por comas: ")
arr = [int(x) for x in inputStr.split(',')]
sortedArr = countingSort(arr)
print("Lista ordenada:", sortedArr)
