# This program opens a Unsorted Unique Container database,
# Inserts a bunch of students, and does more operations
# By the CS 2420 class
# October, 2020

from LLs1 import *
from student import *

gTotalAges = 0
def AddAges(s):
    global gTotalAges
    gTotalAges += int(s.GetAge())

def main():
    global gTotalAges
    studentList = UUC()

    ########## Inserting ##########
    print("\nInserting...")
    fin = open("InsertNamesTiny.txt")
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4])
        ok = studentList.Insert(s)
        if not ok:
            print("Error adding", words[1])
    fin.close()
    print("Students inserted into database:", studentList.Size())

    ########## Traversing ##########
    print("\nTraversing...")
    studentList.Traverse(AddAges)
    avg = gTotalAges / studentList.Size()
    print("The average age is", avg)

    ########## Deleting ##########
    print("\nDeleting...")

    ########## Retrieving ##########
    print("\nRetrieving...")
    fin =  open("RetrieveNamesTiny.txt","r")
    totalAge = 0
    count = 0
    for line in fin:
        ssn = line.strip()
        s = Student("", "", ssn, "", "")
        s2 = studentList.Retrieve(s)
        if s2 is None:
            print("Error finding", ssn)
        else:
            totalAge += int(s2.GetAge())
            count += 1
    fin.close()        
    print("Average of retrieved students is", totalAge / count )
    
    
    
main()
