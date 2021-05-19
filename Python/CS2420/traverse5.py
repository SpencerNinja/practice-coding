# Enhance the last assignment.
# To pass off, show the instructor or a TA the results of running your code, including any error messages, the two average ages, and the 4 timing results.

# NOTE of clarification: You should not be changing the input files, or making any output file, and you should have only 1 python list in memory.

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

    def getAge(self):
        return self.age

# Write code to read all the data from InsertNames.txt into a python list of student objects.
# Big-0: N           
def InsertStudents():
    fin = open("InsertNames.txt", "r")  # open file in read mode
    students = []    # create an empty list to store student field items
    startTimer = time.time()    # start timer
    for line in fin: # searches per line in file
        words = line.split() # breaks up string by whitespace by default
        s = Student(words[0], words[1], words[2], words[3], words[4]) # create a student object
        # check to see if new student has SSN as previous student (duplicate). If a student has the same SSN as a previous student, do not add that student. Instead, print an error message. 
        duplicate = False   # set a flag up as False
        for i in students:   # for each item in student field
            if i.getSSN() == words[2]:  # compare the SSN numbers
                duplicate = True    # set flag to True if found
                break
        if duplicate == False:  # if not a duplicate, add student to list
            students.append(s)
        else:   # if duplicate is True
            # if so, print an error message naming student
            print("This SSN was a duplicate.", words[0], words[1])
    endTimer = time.time() # end timer
    totalTime = endTimer - startTimer   # calculate time it tooke to run the function
    print("It took ", totalTime, " seconds to create the list of students. (InsertStudents)")    # print time
    fin.close()
    return students

# Traverse all students in the pythonList, and print their average age (as a Float, not an Int). Print how many seconds that took.
def TraverseStudents(students):
    count = 0
    ageTotal = 0
    startTimer = time.time()    # start timer
    for stu in students:
        ageTotal += int(stu.getAge())
        count += 1
    aveAge = ageTotal / count
    endTimer = time.time()  # end timer
    totalTime = endTimer - startTimer   # calculate time it tooke to run the function
    print("The average age is", aveAge, ". It took", totalTime, "seconds to calculate. (TraverseStudents)")

# Delete all students in DeleteNames.txt, and print how long that took.
# Also, be sure to print any SSN numbers from the Retrieve and Delete lists that were not there.
# Big-0: N2
def DeleteStudents(students):
    fin = open("DeleteNames.txt", "r")  # open file in read mode
    startTimer = time.time()    # start timer
    for ssn in fin:
        ssn = ssn.strip()
        found = False
        for i in range(len(students)):
            s2 = students[i]
            if s2.getSSN() == ssn:
                found = True
                students.pop(i)     # delete student
                break
        if found == False:
            print("Error! Unable to delete SSN", ssn, "- not found in student list.")
    endTimer = time.time()  # end timer
    totalTime = endTimer - startTimer   # calculate time it tooke to run the function
    print("It took", totalTime, "seconds to delete all students with a SSN listed in DeleteNames.txt.")
    fin.close()

# Retrieve all students in RetrieveNames.txt, print their average age (again, with decimal accuracy), and how long that took.
# Also, be sure to print any SSN numbers from the Retrieve and Delete lists that were not there.
# Big-0: N2
def RetrieveStudents(students):
    fin = open("RetrieveNames.txt", "r")  # open file in read mode
    totalAge = 0
    count = 0
    aveAge = 0
    startTimer = time.time()    # start timer
    for ssn in fin:
        ssn = ssn.strip()
        found = False
        for i in range(len(students)):
            s2 = students[i]
            if s2.getSSN() == ssn:
                found = True
                totalAge += int(s2.getAge())
                count += 1
                break
        if found == False:
            print("Error! Unable to retrieve SSN", ssn, "- not found in student list.")
    aveAge = totalAge / count
    endTimer = time.time()  # end timer
    totalTime = endTimer - startTimer   # calculate time it tooke to run the function
    print("The average age is", aveAge, ". It took", totalTime, "seconds to retrieve all students with a SSN listed in RetrieveNames.txt.")


def main():
    students = InsertStudents()

    TraverseStudents(students)

    DeleteStudents(students)

    RetrieveStudents(students)

main()
