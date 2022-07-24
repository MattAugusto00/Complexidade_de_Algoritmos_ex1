# EFC1_CPA
Alunos: Mateus Augusto da Silveira Pinto-201810241 & Rafael de Souza Garcia-201820003
Turma: 14A

Link do Colab: https://colab.research.google.com/drive/1CiN1C6Mu9Rj-vW1NSBGDnUBq4dZfwsXZ?usp=sharing

1.
Insertion Sort: pior caso = O(n^2), caso medio = O(n^2), melhor caso = O(n).
Selection Sort: O(n^2) para pior, melhor e caso medio.
Bubble Sort: O(n^2) para pior e medio caso. Melhor caso = O(n).
Merge Sort: Θ(n∗logn) para pior, melhor e caso medio
QuickSort: pior caso=O(n^2), caso medio=O(n log n), melhor caso = O(n log n).
HeapSort: Θ(n∗logn) para pior, melhor e caso medio.

As implementações, comparações e gráficos estão no Colab

2.QuickSort: pior caso=O(n^2), caso medio=O(n log n), melhor caso = O(n log n).
Usando o pivotamento aleatório, melhoramos a complexidade de tempo esperada ou média para O (N log N). A complexidade do pior caso ainda é O (N ^ 2).



Insertion Sort
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
Melhor e Pior Caso
import random as ran
import matplotlib.pyplot as plt

def insertionSort(arranjo):
    comparacoes = 0
    for j in range(1, len(arranjo)):
        chave=arranjo[j]
        i=j-1
        while i>=0 and arranjo[i]>chave:
            aux=arranjo[i]
            arranjo[i]=chave
            arranjo[i+1]=aux
            i-=1
            comparacoes += 1
    return comparacoes

def testeAleatorio():
    comparacoes = []
    for i in range(5):
        v = []
        for i in range(5, 1001, 5):
            v.append(ran.randrange(5, 1000, 5))
        comparacoes.append(insertionSort(v))
    return comparacoes

def main():
    x = ["best", "rdm1", "rdm2", "rdm3", "rdm4", "rdm5", "worst"]
    y = []
    
    #melhor caso
    v=[]
    for i in range(5, 1001, 5):
        v.append(i)
    y.append(insertionSort(v))

    #caso aleatorio
    aleatorios = testeAleatorio()
    for i in aleatorios: y.append(i)

    #pior caso
    v=[]
    for i in range(1000, 4, -5):
        v.append(i)
    y.append(insertionSort(v))

    plt.plot(x, y)
main()

Merge Sort
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
Melhor e Pior caso
import random as ran
import matplotlib.pyplot as plt

def mergeSort(A):
    comparacoes = 0
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
            comparacoes += 1
        while i < len(esq):
            A[k] = esq[i]
            i += 1
            k += 1
        while j < len(dir):
            A[k]=dir[j]
            j += 1
            k += 1
    return comparacoes

def testeAleatorio():
    comparacoes = []
    for i in range(5):
        v = []
        for i in range(5, 1001, 5):
            v.append(ran.randrange(5, 1000, 5))
        comparacoes.append(mergeSort(v))
    return comparacoes

def main():
    x = ["best", "rdm1", "rdm2", "rdm3", "rdm4", "rdm5", "worst"]
    y = []

    #melhor caso
    v=[]
    for i in range(5, 1001, 5):
        v.append(i)
    y.append(mergeSort(v))

    #caso aleatorio
    aleatorios = testeAleatorio()
    for i in aleatorios: y.append(i)

    #pior caso
    v=[]
    for i in range(1001, 5, -5):
        v.append(i)
    y.append(mergeSort(v))

    plt.plot(x,y)
main()

Selection Sort
def selectionSort(A):
    for i in range(len(A)):
        menor = i
        for j in range(i+1, len(A)):
            if A[menor] > A[j]:
                menor = j
        A[i], A[menor] = A[menor], A[i]
    return A
Melhor e Pior Caso
import random as ran
import matplotlib.pyplot as plt

def selectionSort(A):
    comparacoes = 0
    for i in range(len(A)):
        menor = i
        for j in range(i+1, len(A)):
            if A[menor] > A[j]:
                menor = j
                comparacoes += 1
        A[i], A[menor] = A[menor], A[i]
    return comparacoes

def testeAleatorio():
    comparacoes = []
    for i in range(5):
        v = []
        for i in range(5, 1001, 5):
            v.append(ran.randrange(5, 1000, 5))
        comparacoes.append(selectionSort(v))
    return comparacoes

def main():
    x = ["best", "rdm1", "rdm2", "rdm3", "rdm4", "rdm5", "worst"]
    y = []

    #melhor caso
    v=[]
    for i in range(5, 1001, 5):
        v.append(i)
    y.append(selectionSort(v))

    #caso aleatorio
    aleatorios = testeAleatorio()
    for i in aleatorios: y.append(i)

    #pior caso
    v=[]
    for i in range(1000, 4, -5):
        v.append(i)
    y.append(selectionSort(v))

    plt.plot(x, y)
    
main()

Bubble Sort
def bubbleSort(A):
    for num in range(len(A)-1,0,-1):
        for i in range(num):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
    return A
Melhor e Pior Caso
import random as ran
import matplotlib.pyplot as plt

def bubbleSort(A):
    comparacoes = 0
    for num in range(len(A)-1,0,-1):
        for i in range(num):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                comparacoes += 1
    return comparacoes

def testeAleatorio():
    comparacoes = []
    for i in range(5):
        v = []
        for i in range(5, 1001, 5):
            v.append(ran.randrange(5, 1000, 5))
        comparacoes.append(bubbleSort(v))
    return comparacoes

def main():
    x = ["best", "rdm1", "rdm2", "rdm3", "rdm4", "rdm5", "worst"]
    y = []
    
    #melhor caso
    v=[]
    for i in range(5, 1001, 5):
        v.append(i)
    y.append(bubbleSort(v))

    #caso aleatorio
    aleatorios = testeAleatorio()
    for i in aleatorios: y.append(i)

    #pior caso
    v=[]
    for i in range(1000, 4, -5):
        v.append(i)
    y.append(bubbleSort(v))

    plt.plot(x, y)

main()

Heap Sort
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
Melhor e Pior Caso
import random as ran
import matplotlib.pyplot as plt

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
    comparacoes=0
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
        comparacoes+=1
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
        comparacoes+=1
    return comparacoes

def testeAleatorio():
    comparacoes = []
    for i in range(5):
        v = []
        for i in range(5, 1001, 5):
            v.append(ran.randrange(5, 1000, 5))
        comparacoes.append(heapSort(v))
    return comparacoes

def main():
    x = ["best", "rdm1", "rdm2", "rdm3", "rdm4", "rdm5", "worst"]
    y = []
    
    #melhor caso
    v=[]
    for i in range(5, 1001, 5):
        v.append(i)
    y.append(heapSort(v))

    #caso aleatorio
    aleatorios = testeAleatorio()
    for i in aleatorios: y.append(i)

    #pior caso
    v=[]
    for i in range(1000, 4, -5):
        v.append(i)
    y.append(heapSort(v))

    plt.plot(x, y)

main()

Quick Sort
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
Melhor e Pior Caso
def quickSort(A):
   return(quickSortHelper(A,0,len(A)-1))

def quickSortHelper(A,primeiro,ultimo):
    comparacoes = 0
    if primeiro<ultimo:
        div, compparcial = particao(A,primeiro,ultimo)
        quickSortHelper(A,primeiro,div-1)
        quickSortHelper(A,div+1,ultimo)
        comparacoes += compparcial + 1
    return comparacoes

def particao(A,primeiro,ultimo):
    pivot = A[primeiro]
    marcaEsq = primeiro+1
    marcaDir = ultimo
    terminou = False
    comparacoes = 0
    while not terminou:
        while marcaEsq <= marcaDir and A[marcaEsq] <= pivot:
            marcaEsq = marcaEsq + 1
            comparacoes += 1
        while A[marcaDir] >= pivot and marcaDir >= marcaEsq:
            marcaDir = marcaDir -1
            comparacoes += 1
        if marcaDir < marcaEsq:
            terminou = True
        else:
            temp = A[marcaEsq]
            A[marcaEsq] = A[marcaDir]
            A[marcaDir] = temp
        comparacoes += 1
    temp = A[primeiro]
    A[primeiro] = A[marcaDir]
    A[marcaDir] = temp
    return marcaDir, comparacoes

def testeAleatorio():
    comparacoes = []
    for i in range(5):
        v = []
        for i in range(5, 1001, 5):
            v.append(ran.randrange(5, 1000, 5))
        comparacoes.append(quickSort(v))
    return comparacoes

def main():
    x = ["best", "rdm1", "rdm2", "rdm3", "rdm4", "rdm5", "worst"]
    y = []
    
    #melhor caso
    v=[]
    for i in range(5, 1001, 5):
        v.append(i)
    y.append(quickSort(v))

    #caso aleatorio
    aleatorios = testeAleatorio()
    for i in aleatorios: y.append(i)

    #pior caso
    v=[]
    for i in range(1000, 4, -5):
        v.append(i)
    y.append(quickSort(v))

    plt.plot(x, y)

main()

Qual é o comportamento assintótico para cada um dos algorítmos acima (melhor caso e pior caso, se puder, analise também em casos aleatórios)
Insertion Sort: pior caso = O(n^2), caso medio = O(n^2), melhor caso = O(n).
Selection Sort: O(n^2) para pior, melhor e caso medio.
Bubble Sort: O(n^2) para pior e medio caso. Melhor caso = O(n).
Merge Sort: Θ(n∗logn) para pior, melhor e caso medio
QuickSort: pior caso=O(n^2), caso medio=O(n log n), melhor caso = O(n log n).
HeapSort: Θ(n∗logn) para pior, melhor e caso medio.

Quicksort Aleatorizado
import random as ran

def quicksort(vet, inicio, fim):
    if(inicio < fim):
        i = particaoAleatoria(vet, inicio, fim)
        quicksort(vet , inicio , i)
        quicksort(vet, i + 1, fim)

def particaoAleatoria(vet , inicio, fim):
    pivoAleat = ran.randrange(inicio, fim)
    vet[inicio], vet[pivoAleat] =\
        vet[pivoAleat], vet[inicio]
    return particao(vet, inicio, fim)

def particao(vet, inicio, fim):
    pivot = inicio
    i = inicio - 1
    j = fim + 1
    while True:
        while True:
            i = i + 1
            if vet[i] >= vet[pivot]:
                break
        while True:
            j = j - 1
            if vet[j] <= vet[pivot]:
                break
        if i >= j:
            return j
        vet[i] , vet[j] = vet[j] , vet[i]

def main():
    vet = [4, 3 , 2, 7, 1, 5, 6, 10]
    quicksort(vet, 0, len(vet) - 1)
    print(vet)
main()
[1, 2, 3, 4, 5, 6, 7, 10]
QuickSort: pior caso=O(n^2), caso medio=O(n log n), melhor caso = O(n log n). Usando o pivotamento aleatório, melhoramos a complexidade de tempo esperada ou média para O (N log N). A complexidade do pior caso ainda é O (N ^ 2).
