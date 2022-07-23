# EFC1_CPA
# EFC1 GCC253 - Complexidade e Projeto de Algoritmos


> **Prof.: Douglas H. S. Abreu**


**Alunos**: Mateus Augusto da Silveira Pinto & Rafael de Souza Garcia

**Matricula**: 201810241 & ...

**Turma**: 10A, 14A

Link do repositório GitHub: 

● O trabalho deve ser feito em grupos de no máximo 2 componentes (todos devem enviar a atividade no Campus Virtual)

● Trabalhos entregues após a data limite não serão aceitos

● Data limite de entrega: 24 de Julho de 2022 : 23h55m

● Enviar o trabalho para o campus virtual, do seguinte modo: link do repositório GitHub e do Colab para acesso ao Notebook. A Documentação deve estar no readme

● O trabalho deve ser desenvolvido no modelo Notebook utilizando a linguagem Python
# Importações e Variáveis globais
import numpy as np

global_1=0
# Funções de Ordenação

> Utilize este espaço para definir as funções de ordenação vista em sala de aula


##  Insertion Sort
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
##  Merge Sort

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
##  Selection Sort

def selectionSort(A):
    for i in range(len(A)):
        menor = i
        for j in range(i+1, len(A)):
            if A[menor] > A[j]:
                menor = j
        A[i], A[menor] = A[menor], A[i]
    return A
##  Bubble Sort

def bubbleSort(A):
    for num in range(len(A)-1,0,-1):
        for i in range(num):
            if A[i]>A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
    return A
## Heap Sort
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
## Quick Sort

> pivo = *A[A-comprimento]*
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

# Questões


1.   Dado um conjunto de arranjos ***A[5,...,1000, passo=5]***

> a) Defina o melhor e pior caso para cada um dos algoritmos definidos acima, crie vetores ***A*** para estes casos e faça a comparação gráficamente também com casos aleatórios (plote um gráfico para cada algoritmo). Conte o numero de comparações realzizadas para cada uma das execuções.

> b) Repita o procedimento acima. Porém compare os algoritmos para pior e melhor caso e também casos aleatórios.

> c) Qual é o comportamento assintótico para cada um dos algorítmos acima (melhor caso e pior caso, se puder, analise também em casos aleatórios)



**Obs.:** para os algoritmos QuickSort e Merge Sort mostre apenas um melhor e um pior caso. faça a comparação com os demais métodos com o conjunto ***A*** apenas em casos aleatórios.




2.   Desenvolda uma versão aleatorizada do QUICKSORT (pivo aleatório) e compare com a versão apresentada em sala de aula e definida acima.


print("Boa sorte!!!")
