def bubbleSort(A):
    for num in range(len(A)-1,0,-1):
        for i in range(num):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
    return A