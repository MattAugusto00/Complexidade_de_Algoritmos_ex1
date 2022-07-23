def quickSort(A):
   quickSortHelper(A,0,len(A)-1)
   return A

def quickSortHelper(A,primeiro,ultimo):
   if primeiro<ultimo:
       div = particao(A,primeiro,ultimo)
       quickSortHelper(A,primeiro,div-1)
       quickSortHelper(A,div+1,ultimo)

def particao(A,primeiro,ultimo):
   pivot = A[primeiro]
   marcaEsq = primeiro+1
   marcaDir = ultimo
   terminou = False

   while not terminou:
       while marcaEsq <= marcaDir and A[marcaEsq] <= pivot:
           marcaEsq = marcaEsq + 1
       while A[marcaDir] >= pivot and marcaDir >= marcaEsq:
           marcaDir = marcaDir -1
       if marcaDir < marcaEsq:
           terminou = True
       else:
           temp = A[marcaEsq]
           A[marcaEsq] = A[marcaDir]
           A[marcaDir] = temp
   temp = A[primeiro]
   A[primeiro] = A[marcaDir]
   A[marcaDir] = temp
   return marcaDir
#chamar quicksort(A) na main

def main():
    A=list(map(int, input().split()))
    print(quickSort(A))
main()