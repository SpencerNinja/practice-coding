# Challenge: Build a program that will decide when and where to eat lunch.
# Title: When And Where To Eat Decision Maker
# Built: March 2021 by Spencer Hurd, improved with suggestions from Joshua Harwood

import random

def whenAndWhereToEat():
    locationChoices = ["Viva Chicken", "Angelica's", "Ernesto's"]
    location = random.randrange(len(locationChoices))

    timeChoices = ["12:00", "12:30", "1:00", "1:30", "2:00", "2:30", "3:00"]
    time = random.randrange(len(timeChoices))

    return ("Location: " + locationChoices[location] + ". " + "Leave at: " + timeChoices[time])

print(whenAndWhereToEat())
