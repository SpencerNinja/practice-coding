# Challenge: Build a program that will decide when and where to eat lunch.
# Title: When And Where To Eat Decision Maker
# Built: March 2021 by Spencer Hurd, improved with suggestions from Joshua Harwood

import random

def whenAndWhereToEat_v1():
    locationChoices = ["Viva Chicken", "Angelica's", "Ernesto's"]
    location = random.randrange(len(locationChoices))

    timeChoices = ["12:00", "12:30", "1:00", "1:30", "2:00", "2:30", "3:00"]
    time = random.randrange(len(timeChoices))

    return ("Location: " + locationChoices[location] + ". " + "Leave at: " + timeChoices[time])

# print(whenAndWhereToEat_v1())



# VERSION 2

def whenAndWhereToEat_v2():
    print("Welcome to the Lunch Decision Maker.")

    print("Please enter the name of restaurants you want to add as choices. Please enter them one at a time and hit 'Enter' after each one. When you are finished, please type 'Done' to move to the next step.")
    restInput = ""
    restautrants = []
    while restInput != 'Done' or restInput != 'done':
        restInput = input("Please enter the name of a restaurant, then press 'Enter'. ")
        restautrants.append(restInput)

    earlyInput = input("Please enter the earliest time you would like to leave for lunch (24 hour format: e.g. 10:55): ")
    startTime = ""
    for char in earlyInput: 
        if char != ":":
            startTime.append(char)
        continue
    startTime = int(startTime)

    lateInput = input("Please enter the lastest time you would be willing to leave for lunch (e.g. 14:00): ")
    lateTime = ""
    for char in lateInput: 
        if char != ":":
            lateTime.append(char)
        continue
    lateTime = int(lateTime)

    chosenRestaurant = random.randrange(len(restautrants))

    chosenTime = random.randrange(startTime, lateTime, 15)

    return("Location: " + restautrants[chosenRestaurant] + ". Time: " + chosenTime)



print(whenAndWhereToEat_v2())
