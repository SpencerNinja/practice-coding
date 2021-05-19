# Inserting Students
import time

# Create a class called Student.
# The class should contain all the fields found in the list of students at cit.cs.dixie.edu/cs/2420/ssn/InsertNames.txt
class Student:
    def __init__(self, firstName, lastName, ssn, email, age):
        self.firstName = firstName
        self.lastName = lastName
        self.ssn = ssn
        self.email = email
        self.age = age

    def getSSN(self):
        return self.ssn


# Note of clarification: You should not be changing the input files, or making any output file, and you should have only 1 python list in memory.

# Write code to read all the data from InsertNames.txt into a python list of student objects.
def InsertNames():
    fin = open("InsertNames.txt", "r")  # open file in read mode
    lstStudents = []    # create an empty list to store student field items
    startTimer = time.time()    # start timer
    for line in fin: # searches per line in file
        words = line.split() # breaks up string by whitespace by default
        # check to see if new student has SSN as previous student (duplicate). Detect any duplicate objects. That is, if a student has the same SSN as a previous student, do not add that student. Instead, print an error message. 
        s = Student(words[0], words[1], words[2], words[3], words[4])
        duplicate = False   # set a flag up as False
        for i in lstStudents:   # for each item in student field
            if i.getSSN() == words[2]:  # compare the SSN numbers
                duplicate = True    # set flag to True if found
                break
        if duplicate == False:  # if not a duplicate, add student to list
            lstStudents.append(s)
        else:   # if duplicate is True
            # if so, print an error message naming student
            print("This SSN was a duplicate.", words[0], words[1])
    endTimer = time.time()
    # Time how long that takes, and have your code print that.
    totalTime = endTimer - startTimer   # calculate time it tooke to run the function
    print("It took ", totalTime, " seconds to search the list.")    # print time
    fin.close()
InsertNames()
