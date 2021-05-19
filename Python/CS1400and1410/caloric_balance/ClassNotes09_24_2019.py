# Class Notes 
# September 24, 2019
# Spencer Hurd

# WordZap assignment
    # outline of CHECKWORD method function
    # given a list of letters 
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # user picked letters "gag"
    # use a forLoop to check letters
        def checkWord(self,word):
            #1-deep copy letters
            #2-check each letter in word
                #if so, rename it
                #else:
                    return False
            #3-update letters
            #4-return True


# two types of copy: shallow & deep, shallow is just a reference to the original list, deep is an actual copy
copy = a  #shallow copy
import copy 
copy.deepcopy(a) #deep copy
# can also make a deep copy by:
copy = a[:]  # use slicing

#CAR Class example
import random
class Car:
    def __init__(self, color, wt, ms, acc, weight, powerup):
        self.color = color
        self.wheel_type = wt
        self.max_speed = ms
        self.acceleration = acc
        self.weight = weight
        self.powerup = powerup
        self.items = []
        self.speed = 0
        self.
    def accelerate(self, dt):
        if dt < 0:
            return
        self.speed += self.acceleration * dt
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        


