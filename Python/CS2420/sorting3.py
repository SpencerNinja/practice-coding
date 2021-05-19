import random
import math
import sys

class Counts:
    def __init__(self):
        self.compares = 0
        self.swaps = 0

# create a list of random numbers based on size input in main()
def CreateRandomNumbersList(size):
    A = []
    for i in range(size):
        A.append(random.randrange(0, size))
    return A

# Bubble Sort
def Bubble(A, c):
    switched = True     # set flag to True
    while switched:     # while flag is set to True, enter while loop
        switched = False    # set flag to False
        for i in range(len(A)-1):   # loop through length of list
            c.compares += 1
            if A[i] > A[i+1]:       # compare each value with the next value
                c.swaps += 1
                previous = A[i]     # remember former value
                A[i] = A[i+1]       # switch
                A[i + 1] = previous # switch part 2
                switched = True     # set flag back to True

# Shaker Sort
def Shaker(A, c):
    switched = True                 # set flag to True
    while switched:                 # search list while True
        switched = False            # set flag to False
        for i in range(len(A)-1):   # search list
            c.compares += 1
            if A[i] > A[i + 1]:     # compare A[i] with the number following it
                c.swaps += 1
                A[i], A[i + 1] = A[i + 1], A[i]     # switch
                switched = True
        for i in range(len(A) - 2, -1, -1):     # search list starting at end
            c.compares += 1
            if A[i] > A[i + 1]:     # compare A[i] with following number
                c.swaps += 1
                A[i], A[i + 1] = A[i +1], A[i]      # switch
                switched = True             # set flag to True

# Selection Sort
def Selection(A, c):
    for i in range(len(A)):
        smallestIndex = i
        for j in range(i, len(A)):
            c.compares += 1
            if A[smallestIndex] > A[j]:         # compare
                smallestIndex = j
        c.swaps += 1
        A[i], A[smallestIndex] = A[smallestIndex], A[i]     #swap

# Merge Sort
    # uses nested for loops to use index i in one list and index j in the other list to decide what goes into index k in original list
    # use while loops to catch what is left in each list
    # Big-O: Nlog2N
def Merge(A, c):
    if len(A) <= 1: # base case
        return A
    # split list into two halves
    # ALTERNATE: 
    #   half = len(A)//2
	#   LeftHalf = A[:half]
	#   RightHalf = A[half:]
    LeftHalf = A[0:len(A)//2]
    RightHalf = A[len(A)//2:]
    c.swaps += len(A)
    # magically/recursively sorting each half of the list
    Merge(LeftHalf, c)
    Merge(RightHalf, c)
    # merge the left and right halves back over list A, starting from least to greatest
    i = 0   # Left Half: set index to 0
    j = 0   # Right Half: set index to 0
    k = 0   # full list (A): set index to 0
    while i < len(LeftHalf) and j < len(RightHalf):
        c.compares += 1
        if LeftHalf[i] <= RightHalf[j]:
            c.swaps += 1
            A[k] = LeftHalf[i]
            i += 1
            k += 1
        else:
            c.swaps += 1
            A[k] = RightHalf[j]
            j += 1
            k += 1
    while i < len(LeftHalf): # one of the lists should be empty by now, move the remaining numbers from the other list into list A
        c.swaps += 1
        A[k] = LeftHalf[i]
        i += 1
        k += 1
    while j < len(RightHalf):
        c.swaps += 1
        A[k] = RightHalf[j]
        j += 1
        k += 1

# Quick Sort
    # Big-0: log2N*2 or N**2 if mostly sorted
def Quick(A, low, high, c):
    # base case 
    if (high - low) <= 0:
        return A
    pivot = low
    lmgt = pivot + 1 # lmgt = least most greater than
    for i in range(low + 1, high + 1):
        # compare A[i] and A[pivot] then swap and increment
        c.compares += 1
        if A[i] < A[pivot]:         # compare
            c.swaps += 1
            A[i], A[lmgt] = A[lmgt], A[i]       # swap
            lmgt += 1
    pivot = lmgt - 1
    c.swaps += 1
    A[low], A[pivot] = A[pivot], A[low]    # swap
    # recurse
    Quick(A, low, pivot - 1, c)    # sort left
    Quick(A, pivot + 1, high, c)   # sort right

# Quick Sort adapted for compares & swaps
def QuickC(A, c):
    Quick(A, 0, len(A)-1, c)

# Modified Quick Sort
def MQuick(A, low, high, c):
    # base case
    if (high - low) <= 0:
        return A
    # modified Quick Sort
    mid = (low + high) // 2
    c.swaps += 1
    A[mid], A[low] = A[low], A[mid]     # swap
    # do 1 pass of Quick Sort
    pivot = low
    lmgt = pivot + 1 # lmgt = least most greater than
    for i in range(low + 1, high + 1):
        # compare A[i] and A[pivot] then swap and increment
        c.compares += 1
        if A[i] < A[pivot]:     # compare
            c.swaps += 1
            A[i], A[lmgt] = A[lmgt], A[i]       # swap
            lmgt += 1
    pivot = lmgt - 1
    c.swaps += 1
    A[low], A[pivot] = A[pivot], A[low]    # swap
    # recurse from low to pivot -1
    MQuick(A, low, pivot - 1, c)    # sort left
    # recurse from pivot +1 through high
    MQuick(A, pivot + 1, high, c)   # sort right

# Quick Sort adapted for compares & swaps
def MQuickC(A, c):
    MQuick(A, 0, len(A)-1, c)

# Counting Sort
    # Big-0: N
def Counting(A, c):
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
    c.compares = len(A)
    c.swaps = len(A)

def MostlySortedData(size):
    A = CreateRandomNumbersList(size)
    A.sort()
    previous = A[0]
    A[0] = A[-1]
    A[-1] = previous
    return A

# Attempt to call the class count values (compares & swaps) from each sort
# def countValues():
#     bubble = Counts()
#     shaker = Counts()
#     selection = Counts()
#     merge = Counts()
#     quick = Counts()
#     mquick = Counts()
#     counting = Counts()
#     sortsCount = [bubble, shaker, selection, merge, quick, mquick, counting]
#     return sortsCount

def main():
    # unsortedList = CreateRandomNumbersList(10)
    # A = unsortedList[:]     # original unsorted list
    # B = unsortedList[:]     # Python built-in sort list
    # C = unsortedList[:]     # Bubble Sort list
    # D = unsortedList[:]     # Shaker Sort list
    # E = unsortedList[:]     # Selection Sort list
    # F = unsortedList[:]     # Merge Sort list
    # G = unsortedList[:]     # Quick Sort list
    # H = unsortedList[:]     # Modified Quick Sort list
    # I = unsortedList[:]     # Counting Sort list

    # print("List before sort:               ", unsortedList)

    # B.sort() # Python built-in sort
    # print("List after built-in sort:       ", B)

    # Bubble(C) # Bubble Sort
    # print("List after Bubble Sort:         ", C)
    # if C != B:
    #     print("The lists do NOT match!")

    # Shaker(D) # Shaker Sort
    # print("List after Shaker Sort:         ", D)
    # if D != B:
    #     print("The lists do NOT match!")

    # Selection(E) # Selection Sort
    # print("List after Selection Sort:      ", E)
    # if E != B:
    #     print("The lists do NOT match!")

    # Merge(F) # Merge Sort
    # print("List after Merge Sort:          ", F)
    # if F != B:
    #     print("The lists do NOT match!")

    # Quick(G, 0, len(G) - 1) # Quick Sort
    # print("List after Quick Sort:          ", G)
    # if G != B:
    #     print("The lists do NOT match!")

    # MQuick(H, 0, len(H) - 1) # Modified Quick Sort
    # print("List after Modified Quick Sort: ", H)
    # if H != B:
    #     print("The lists do NOT match!")

    # Counting(I) # Counting Sort
    # print("List after Counting Sort:       ", I)
    # if I != B:
    #     print("The lists do NOT match!")

    sys.setrecursionlimit(5000)

    # print the names of the sorts
    sorts = [Bubble, Shaker, Selection, Merge, QuickC, MQuickC, Counting]

# The first data set and chart should plot Problem Size versus number of COMPARES when using RANDOM DATA.
    print("Compares - Random Data")
    print("    ", end="")   # print 4 space with no newline
    for sort in sorts:
        print("%11s" % (sort.__name__), end="") # string with 10 spaces
    print()
    # print the left labels and data
    for s in range(3, 13):
        size = 2 ** s  
        print("%4i" % (s), end="")      # %i = signed integer decimal with 4 spaces
        for eachSort in sorts:
            A = CreateRandomNumbersList(size)   # create a list of random numbers
            B = A[:]        # Python built in sort
            B.sort()        # create a copy of list A
            c = Counts()    # initialize a Counts object
            eachSort(A, c)  # call sort and pass in list and Counts object
            if A != B:
                print("Error!")
            value = 0
            if c.compares > 0:          # prevent against log0 errors
                value = math.log(c.compares, 2) # Call log function on Counts object (set to base 2S)
            print("%11.2f" % (value) , end="")   # %6.2f = floating point decimal format 6 spaces wide and 2 places after the decimal
        print()
    print("Numbers in output are: 2 to the power of __")

    print()

# The second data set and chart should plot Problem Size versus number of SWAPS when using RANDOM DATA.
    print("Swaps - Random Data")
    print("    ", end="")   # print 4 space with no newline
    for sort in sorts:
        print("%11s" % (sort.__name__), end="") # string with 10 spaces
    print()
    # print the left labels and data
    for s in range(3, 13):
        size = 2 ** s  
        print("%4i" % (s), end="")      # %i = signed integer decimal with 4 spaces
        for eachSort in sorts:
            A = CreateRandomNumbersList(size)   # create a list of random numbers
            B = A[:]        # Python built in sort
            B.sort()        # create a copy of list A
            c = Counts()    # initialize a Counts object
            eachSort(A, c)  # call sort and pass in list and Counts object
            if A != B:
                print("Error!")
            value = 0
            if c.swaps > 0:          # prevent against log0 errors
                value = math.log(c.swaps, 2) # Call log function on Counts object (set to base 2S)
            print("%11.2f" % (value) , end="")   # %6.2f = floating point decimal format 6 spaces wide and 2 places after the decimal
        print()
    print("Numbers in output are: 2 to the power of __")

    print()

# The third data set and chart should plot Problem Size versus number of COMPARES when using MOSTLY SORTED DATA instead of Random data.
    print("Compares - Mostly Sorted Data")
    print("    ", end="")   # print 4 space with no newline
    for sort in sorts:
        print("%11s" % (sort.__name__), end="") # string with 10 spaces
    print()
    # print the left labels and data
    for s in range(3, 13):
        size = 2 ** s  
        print("%4i" % (s), end="")      # %i = signed integer decimal with 4 spaces
        for eachSort in sorts:
            A = MostlySortedData(size)   # create a list of random numbers
            B = A[:]        # Python built in sort
            B.sort()        # create a copy of list A
            c = Counts()    # initialize a Counts object
            eachSort(A, c)  # call sort and pass in list and Counts object
            if A != B:
                print("Error!")
            value = 0
            if c.compares > 0:          # prevent against log0 errors
                value = math.log(c.compares, 2) # Call log function on Counts object (set to base 2S)
            print("%11.2f" % (value) , end="")   # %6.2f = floating point decimal format 6 spaces wide and 2 places after the decimal
        print()
    print("Numbers in output are: 2 to the power of __")


    # # Uses function countValues() to call Counts class and pull compares/swaps from each sort
    # display = []    # list to display in terminal
    # for s in range(3, 8):      # labels of numbers on left
    #     size = 2 ** s
    #     print("%4i" % (s), end="")      # %i = signed integer decimal
    #     sortCount = countValues()       # save list of sort's class counts
    #     A = CreateRandomNumbersList(size)   # create a random list
    #     Bubble(A[:], sortCount[0])      # Call Bubble Sort and pass in list and class count
    #     Shaker(A[:], sortCount[1])
    #     Selection(A[:], sortCount[2])
    #     Merge(A[:], sortCount[3])
    #     QuickC(A[:], sortCount[4])
    #     MQuickC(A[:], sortCount[5])
    #     Counting(A[:], sortCount[6])
    #     for sortClass in range(len(sortCount)):
    #         if sortClass == 0:
    #             display.append(s)      # append to this row/column  ???
    #             display.append(float(math.log(sortCount[sortClass].compares, 2)) # append the number of compares for that sort ???
    #     print()

main()
