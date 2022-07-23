def selectionSort(A):
    for i in range(len(A)):
        menor = i
        for j in range(i+1, len(A)):
            if A[menor] > A[j]:
                menor = j
        A[i], A[menor] = A[menor], A[i]
    return A

def main():
    A=list(map(int, input().split()))
    print(selectionSort(A))
main()