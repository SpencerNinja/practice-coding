# Yahtzee Simulation
# Spencer Hurd

# Instructions

# Write a function called Yahtzee_Simulation()
# Simulate rolling 6 dice 1 million times
# Keep track of the number of the computer rolls a yahtzee
# probability of getting yahtzee=6*5*4*3*2*1
# return the number of wins divided by the number of tries
# no print statements

# Write a function called main() w no parameters
# This function calls the Yahtzee_Simulation function 10 times and prints the result of each simulation
# Print the mathematical result: print(6/(6**5))

def Yahtzee_Simulation():
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    d=random.randint(1,6)
    e=random.randint(1,6)
    f=random.randint(1,6)
    for i in range():
        rollout=(a+b+c+d+e+f)*1,000,000
    return rollout

def main():
    min=1
    max=6

def test():
    count=numberOfRolls
    while numberOfRolls >= count and count >0:
        print(random.randint(min,max))
        count=count -1

def test2():
    total=0
    for i in range():
        total+=random.randint(1,6)
    return total
