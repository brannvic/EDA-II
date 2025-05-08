def countingSort(arr, k):
    maxElemento=max(arr)
    counting=[0]*(maxElemento+1)
##cuantas veces aparece un elemento
    for num in arr:
        counting[num]+=1
        ##contar la frecuencia de cada elemento en el arreglo
    paresCounting=0
    for i in range(len(counting)):
        ##contar las diferencias de los pares usando k como diferencia
        if i+k<len(counting):
            ##verifica que el valor este dentro del arr y evitar desorden
            paresCounting+=counting[i]*counting[i+k]
            ## si cumple el if calcula la cantidad de pares con diferencia
    return paresCounting

inputArr1=input("Ingrese los elementos del primer arreglo separados por espacios: ")
arr1=[int(x) for x in inputArr1.split()]
inputArr2=input("Ingrese los elementos del segundo arreglo separados por espacios: ")
arr2=[int(x) for x in inputArr2.split()]
k1=int(input("Ingrese el valor de k1: "))
k2=int(input("Ingrese el valor de k2: "))
resultado1 = countingSort(arr1, k1)
resultado2 = countingSort(arr2, k2)
print("El número de pares con diferencia de", k1, "en el primer arreglo es:", resultado1)
print("El número de pares con diferencia de", k2, "en el segundo arreglo es:", resultado2)
