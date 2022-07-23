def heapify(A, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and A[i] < A[esq]:
        maior = esq
    if dir < n and A[maior] < A[dir]:
        maior = dir
    if maior != i:
        A[i],A[maior] = A[maior],A[i]
        heapify(A, n, maior)

def heapSort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    return A