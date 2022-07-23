def insertionSort(A):
  for j in range(1, len(A)):
    chave=A[j]
    i=j-1
    while i>=0 and A[i]>chave:
      aux=A[i]
      A[i]=chave
      A[i+1]=aux
      i-=1
  return A