# DNA Sequencing
# Spencer Hurd
# CS 1410-03

import os
def fileToList(filename):
    lines = []
    if os.path.isfile(filename):  # looks up a filename to see if the file exists
        f = open(filename)
        for line in f:
            line = line.strip()
            lines.append(line)
        f.close()
    return lines  # returns a list of the lines in the file
def returnFirstString(strings):
    xstr = ""
    for i in range(len(strings)):
        xstr = strings[0]
    return xstr  # returns the first string
def strandsAreNotEmpty(strand1, strand2):
    if len(strand1) > 0 and len(strand2) > 0:
        return True  # returns True if length both strands have a length greater than zero
    else:
        return False
def strandsAreEqualLengths(strand1, strand2):
    if len(strand1) == len(strand2):
        return True  # returns True if the length of both strands are equal
    else:
        return False
def candidateOverlapsTarget(target, candidate, overlap):
    # checks to see if the target and candidate strands have an overlap of overlap characters
    if target[-overlap:] == candidate[:overlap]:
        return True  # returns True if they overlap
    else:
        return False
# for i in range(len(newTarget)):
# for i in range(len(candidate)):
# if target[-overlap:] == candidate[:overlap]:
# return True
    # target =    "ABBBBBA"
    # candidate = "BABBBAA"
# def findLargestOverlap(target,candidate): #find the largest overlap and return the size of the overlap
# a = target[-overlap:]
# b = candidate[:overlap]
# list(range(1,len(a)+1))
def findLargestOverlap(target, candidate):
    largest = 0
    a = strandsAreNotEmpty(target, candidate)
    b = strandsAreEqualLengths(target, candidate)
    if a == True and b == True:
        for i in range(1, len(target)+1):
            if candidateOverlapsTarget(target, candidate, i) == True:
                largest = i
        return largest
    else:
        return -1
# examine each candiate in the candidates list and determine the candidate with the longest overlap
def findBestCandidate(target, candidates):
    largest = 0
    lgString = ""
    for i in range(len(candidates)):
        length = findLargestOverlap(target, candidates[i])
# length = len(candidates[i])
        if length > largest:
            largest = length
            lgString = candidates[i]
    return (lgString, largest)
# largest = findLargestOverlap(target,candidate)
# return(lgOvrCand,count) #returns a tuple containing the candidate string with the larget overlap and the overlap
# joins the target and candidte strands together merging them and returns the joined strand
def joinTwoStrands(target, candidate, overlap):
    joinStrands = target + candidate[overlap:]
    return joinStrands
    # 3 slices in the string
def main():
    # ask user for filename of the target strand file and candidate strands file
    targ = input("What is the filename of the target strand: ")
    cand = input("What is the filename of the candidate strands: ")
    targ1 = fileToList(targ)
    cand1 = fileToList(cand)
    targ2 = returnFirstString(targ1)
    best, overlap = findBestCandidate(targ2, cand1)
    print(joinTwoStrands(targ2, best, overlap))
if __name__ == '__main__':
    main()
