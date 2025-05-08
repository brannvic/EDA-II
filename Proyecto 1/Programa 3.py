def countingSort(A1,A2):
    counting={} ##diccionario para contar la frecuencia
   
    for num in A1:
        counting[num]=counting.get(num,0)+1##se recorre el arreglo y aumenta en el diccionario
    
    A1Sorted=[]##almacena los datos

    for num in A2:##verifica que el elemento este en el arreglo A_2
        if num in counting:
            A1Sorted.extend([num]*counting[num])
            del counting[num] ##se agrega tantas veces como el conteo diga
    elementos=sorted(counting.keys())##elementos restantes se orgenas -
    A1Sorted.extend(elementos)
    return A1Sorted

A1=list(map(int, input("ingrese los elementos del primer arreglo separados por espacios y sin comas: ").split()))
A2=list(map(int, input("ingrese los elementos del segundo arreglo separados por espacios y sin comas: ").split()))
resultado=countingSort(A1,A2)
print("El primer arreglo ordenado de acuerdo al segundo arreglo", resultado)
