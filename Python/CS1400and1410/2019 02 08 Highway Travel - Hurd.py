# I-15 Highway Travel Advisor
# Spencer Hurd

print ("Highway Travel Advisor")
print ("This application will help you with your travels on I-15 in Utah")
print ("Please input the following information: ")

inputEnter=int(input("Enter at which mile marker you will enter the I-15 "))
inputExit=int(input("Enter which exit at which you wish to leave "))
inputHours=int(input("How many hours from now do you want to arrive? "))
inputMPH=int(input("Please enter your expected average speed in MPH "))

# calculate distance to travel
distance=inputExit-inputEnter
# calculate expected travel time given speed
travelTime=distance/inputMPH
print ("It will take ",travelTime, "hours to reach your destination")

##if going over 80MPH warn them that they are travelling dangerously & breaking law. If average speed is less than 60MPH, driver is causing problems on highway
if inputMPH > 80:
    print("You are driving too fast! It is dangerous and against the law!")
elif inputMPH < 60:
    print("You are driving too slow and causing problems on the highway!")
##if travel time is larger than the time when the user wants to arrive, tell user late they will be
    
##if none of conditions above, tell user how far they will travel and how long they have to leave in order to be on time  
travelDistance=inputMPH*travelTime
print ("You will travel ",travelDistance, "miles on your journey")

