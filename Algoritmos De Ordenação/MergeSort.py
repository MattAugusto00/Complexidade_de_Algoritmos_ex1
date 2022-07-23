def mergeSort(A):
    if len(A) > 1:
        meio = len(A) // 2
        esq = A[:meio]
        dir = A[meio:]
        mergeSort(esq)
        mergeSort(dir)
        i = 0
        j = 0
        k = 0
        while i < len(esq) and j < len(dir):
            if esq[i] <= dir[j]:
              A[k] = esq[i]
              i += 1
            else:
                A[k] = dir[j]
                j += 1
            k += 1
        while i < len(esq):
            A[k] = esq[i]
            i += 1
            k += 1
        while j < len(dir):
            A[k]=dir[j]
            j += 1
            k += 1
    return A

def main():
    A=list(map(int, input().split()))
    print(mergeSort(A))
main()