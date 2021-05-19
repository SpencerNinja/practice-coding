import random

def CreateRandomNumbersList(size):
    A = []
    for i in range(size):
        A.append(random.randrange(0, size))
    return A

def BubbleSort(A):
    switched = True
    while switched:
        switched = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                previous = A[i]
                A[i] = A[i+1]
                A[i + 1] = previous
                switched = True

def ShakerSort(A):
    switched = True
    while switched:
        switched = False
        for i in range(len(A)-1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                switched = True
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i +1], A[i]
                switched = True

def SelectionSort(A):
    for i in range(len(A)):
        smallestIndex = i
        for j in range(i, len(A)):
            if A[smallestIndex] > A[j]:
                smallestIndex = j
        A[i], A[smallestIndex] = A[smallestIndex], A[i]

def main():
    unsortedList = CreateRandomNumbersList(10)
    A = unsortedList[:]
    B = unsortedList[:]
    C = unsortedList[:]
    D = unsortedList[:]
    E = unsortedList[:]
    print("List before sort:          ", unsortedList)
    B.sort() # Python built-in sort
    print("List after built-in sort:  ", B)
    BubbleSort(C) # Bubble Sort
    print("List after Bubble Sort:    ", C)
    if C != B:
        print("The lists do NOT match!")
    ShakerSort(D) # Shaker Sort
    print("List after Shaker Sort:    ", D)
    if D != B:
        print("The lists do NOT match!")
    SelectionSort(E)
    print("List after Selection Sort: ", E)
    if E != B:
        print("The lists do NOT match!")
main()
