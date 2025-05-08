#Actividad 4
def bubbleSort(A):
    for i in range (1,len(A)):
        print('Pasada',i)
        for j in range(len(A)-1):
            if A[j][0]>A[j+1][0]: #se implementa una tupla para determinar los indices
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
            print(A)
A=[(5,0),(4,1),(6,2),(8,3),(5,4)] #imprime valor e indice
bubbleSort(A)
print("\n")
print(A)