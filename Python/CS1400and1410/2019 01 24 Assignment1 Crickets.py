#Dipper's Cricket Thermometer
#Spencer Hurd

#instructions
def main(crickets):
    print("This program estimates the temperature based")
    print("on the number of cricket chrips in a 13 second")
    print("interval plus 40")

# formula to get temperature
# temperature = number of cricket chirps in 13 seconds + 40
    strCrktChrp=input("Please input the number of cricket chrips within a 13 second interval")
        print(input)
    fltCrktChrp = float (strCrktChrp)

#calculation
    fltCrktTemp = (fltCrktChrp +40)


# tell if it is too cold
    if temp >= 55:
        print ("It is", fltCrktTemp, "degrees")
    else:
        print ("It is too cold for crickets")

