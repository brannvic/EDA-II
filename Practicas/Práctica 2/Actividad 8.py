def heapify(arr, n, i):
    raiz=i
    izquierda=2*i+1
    derecha=2*i+2

    if izquierda<n and arr[izquierda]>arr[raiz]: #evalua lado izquierdo con la raiz
        raiz=izquierda

    if derecha<n and arr[derecha]>arr[raiz]: #evalua lado derecho con la raiz
        raiz=derecha

    if raiz !=i:
        arr[i],arr[raiz]=arr[raiz],arr[i]
        print("(%d, %d, %d)" % (arr[i],arr[izquierda],arr[derecha]))
        # Imprime la tena (raiz, izquierda, derecha)
        heapify(arr,n,raiz)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[841, 615, 771, 154, 913, 165, 346, 344, 976, 503, 957, 858, 104, 274, 294, 
     534, 830, 794, 628, 535, 768, 481, 99, 398, 599, 774, 258, 660, 433, 687, 949]

heapSort(arr)
n=len(arr)
print("\nSorted array is")

for i in range(n):
    print("%d" % arr[i], end=" ")
