import random

# create a list of random numbers based on size input in main()
def CreateRandomNumbersList(size):
    A = []
    for i in range(size):
        A.append(random.randrange(0, size))
    return A

# Bubble Sort
def BubbleSort(A):
    switched = True     # set flag to True
    while switched:     # while flag is set to True, enter while loop
        switched = False    # set flag to False
        for i in range(len(A)-1):   # loop through length of list
            if A[i] > A[i+1]:       # compare each value with the next value
                previous = A[i]     # remember former value
                A[i] = A[i+1]       # switch
                A[i + 1] = previous # switch part 2
                switched = True     # set flag back to True

# Shaker Sort
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

# Selection Sort
def SelectionSort(A):
    for i in range(len(A)):
        smallestIndex = i
        for j in range(i, len(A)):
            if A[smallestIndex] > A[j]:
                smallestIndex = j
        A[i], A[smallestIndex] = A[smallestIndex], A[i]

# Merge Sort
    # uses nested for loops to use index i in one list and index j in the other list to decide what goes into index k in original list
    # use while loops to catch what is left in each list
    # Big-O: Nlog2N
def MergeSort(A):
    if len(A) <= 1: # base case
        return A
    # split list into two halves
    # ALTERNATE: 
    #   half = len(A)//2
	#   LeftHalf = A[:half]
	#   RightHalf = A[half:]
    LeftHalf = A[0:len(A)//2]
    RightHalf = A[len(A)//2:]
    # magically/recursively sorting each half of the list
    MergeSort(LeftHalf)
    MergeSort(RightHalf)
    # merge the left and right halves back over list A, starting from least to greatest
    i = 0   # Left Half: set index to 0
    j = 0   # Right Half: set index to 0
    k = 0   # full list (A): set index to 0
    while i < len(LeftHalf) and j < len(RightHalf):
        if LeftHalf[i] <= RightHalf[j]:
            A[k] = LeftHalf[i]
            i += 1
            k += 1
        else:
            A[k] = RightHalf[j]
            j += 1
            k += 1
    while i < len(LeftHalf):
        A[k] = LeftHalf[i]
        i += 1
        k += 1
    while j < len(RightHalf):
        A[k] = RightHalf[j]
        j += 1
        k += 1

# Quick Sort
    # Big-0: log2N*2 or N**2 if mostly sorted
def QuickSort(A, low, high):
    # base case 
    if (high - low) <= 0:
        return A
    pivot = low
    lmgt = pivot + 1 # lmgt = least most greater than
    for i in range(low + 1, high + 1):
        # compare A[i] and A[pivot] then swap and increment
        if A[i] < A[pivot]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]    # switch the pivot with the left most greater than
    # recurse
    QuickSort(A, low, pivot - 1)    # sort left
    QuickSort(A, pivot + 1, high)   # sort right


# Modified Quick Sort
def ModifiedQuickSort(A, low, high):
    # base case
    if (high - low) <= 0:
        return A
    # modified quicksort
    mid = (low + high) // 2
    A[mid], A[low] = A[low], A[mid] # swap
    # do 1 pass of QuickSort
    pivot = low
    lmgt = pivot + 1 # lmgt = least most greater than
    for i in range(low + 1, high + 1):
        # compare A[i] and A[pivot] then swap and increment
        if A[i] < A[pivot]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt += 1
    pivot = lmgt - 1
    A[low], A[pivot] = A[pivot], A[low]    # swap
    # recurse from low to pivot -1
    ModifiedQuickSort(A, low, pivot - 1)    # sort left
    # recurse from pivot +1 through high
    ModifiedQuickSort(A, pivot + 1, high)   # sort right

# Counting Sort
    # Big-0: N
def CountingSort(A):
    # find the highest value
    highestValue = 0
    for i in range(len(A)):
        if A[i] > highestValue:
            highestValue = A[i]
    highestValue += 1 # if 9 big, we need 10 list items, 0 through 9
    # if highestValue < len(A):   # if highest value is < length of list 
    #    highestValue = len(A)       # reassign highest value to length of list
    # make Frequency list the size of the highest value in A list and fill it with only zeros
    freq = [0] * highestValue  # initialize Frequency values to zero
    for number in A:      # loop through A, counting how many of each value are in A list
        freq[number] += 1    # if i is equal to value, add a tally to that position in the Frequency list
    m = 0
    for j in range(len(freq)):        # loop through Frequency, overwriting A
        value = j
        count = freq[j]
        for k in range(count):
            A[m] = value    # for each value in Frequency, copy items back into A
            m += 1      # for each value x in A, increment Frequency(x)

def main():
    unsortedList = CreateRandomNumbersList(10)
    A = unsortedList[:]     # original unsorted list
    B = unsortedList[:]     # Python built-in sort list
    C = unsortedList[:]     # Bubble Sort list
    D = unsortedList[:]     # Shaker Sort list
    E = unsortedList[:]     # Selection Sort list
    F = unsortedList[:]     # Merge Sort list
    G = unsortedList[:]     # Quick Sort list
    H = unsortedList[:]     # Modified Quick Sort list
    I = unsortedList[:]     # Counting Sort list

    print("List before sort:               ", unsortedList)

    B.sort() # Python built-in sort
    print("List after built-in sort:       ", B)

    BubbleSort(C) # Bubble Sort
    print("List after Bubble Sort:         ", C)
    if C != B:
        print("The lists do NOT match!")

    ShakerSort(D) # Shaker Sort
    print("List after Shaker Sort:         ", D)
    if D != B:
        print("The lists do NOT match!")

    SelectionSort(E) # Selection Sort
    print("List after Selection Sort:      ", E)
    if E != B:
        print("The lists do NOT match!")

    MergeSort(F) # Merge Sort
    print("List after Merge Sort:          ", F)
    if F != B:
        print("The lists do NOT match!")

    QuickSort(G, 0, len(G) - 1) # Quick Sort
    print("List after Quick Sort:          ", G)
    if G != B:
        print("The lists do NOT match!")

    ModifiedQuickSort(H, 0, len(H) - 1) # Modified Quick Sort
    print("List after Modified Quick Sort: ", H)
    if H != B:
        print("The lists do NOT match!")

    CountingSort(I) # Counting Sort
    print("List after Counting Sort:       ", I)
    if I != B:
        print("The lists do NOT match!")

main()
