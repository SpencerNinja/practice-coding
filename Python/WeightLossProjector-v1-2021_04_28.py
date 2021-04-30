# Challenge: Build a program that allows the user to find out how long it would take to reach their goal weight.
# Title: Weight Loss Projections
# Built: April 28, 2021 by Spencer Hurd

def weightLossProjector():
    startingWeight = int(input("What is your starting weight? "))
    updatedWeight = startingWeight
    goalWeight = int(input("What is your goal weight? "))
    poundsPerWeek = int(input("How many pounds do you plan on losing each week? "))
    numOfWeeks = 0
    totalWeightLost = 0
    numOfMonths = 0

    while updatedWeight >= goalWeight:
        updatedWeight -= poundsPerWeek
        totalWeightLost += poundsPerWeek
        numOfWeeks += 1
    numOfMonths = float(numOfWeeks) / 4.0

    return ("\nYour starting weight was: " + str(startingWeight) + "\nYour goal weight is: " + str(goalWeight) + "\nAt a rate of losing " + str(poundsPerWeek) + " per week, it will take you " + str(numOfWeeks) + " weeks or " + str(numOfMonths) + " months to reach your goal")

print(weightLossProjector())
