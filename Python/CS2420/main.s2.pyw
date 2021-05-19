# This program makes a UUC (implemented as a Linked List).
# It Inserts several student object into it, followed by Traversing, Deleting and Retrieving
# By The CS 2420 class
# October, 2020

from LLs2 import *
from student import *

gTotalAges = 0
def AddAges(s):
    global gTotalAges
    gTotalAges += int(s.GetAge())
    
def main():
    global gTotalAges
    studentList = UUC()

    ########## Inserting ##########
    fin = open("InsertNamesTiny.txt","r")
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4])
        ok = studentList.Insert(s)
        if not ok:
            print("Error inserting", words[1])
    fin.close()
    print("Students inserted:", studentList.Size())

    ########## Traversing ##########
    studentList.Traverse(AddAges)
    ave = gTotalAges / studentList.Size()
    print("The average age is",ave)

    ########## Deleting ##########
    

    ########## Retrieving ##########
    fin = open("RetrieveNamesTiny.txt","r")
    totalAge = 0
    count = 0
    for line in fin:
        ssn = line.strip()
        s1 = Student("", "", ssn, "", "")
        s2 = studentList.Retrieve(s1)
        if s2 is None:
            print("Error retrieving student with ssn of", ssn)
        else:
            totalAge += int(s2.GetAge())
            count += 1
    print("Average age of retrieved student is", totalAge / count)
main()

        
