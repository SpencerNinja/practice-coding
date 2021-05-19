def main():
# instructions
    print("This program calculates the size of tank to use for catching rainwater")

#get height
    height=input("How many inches of rain fall in a storm?")
    height=int(height)

#get length
    length=input("Enter the length in feet of the catchment area")
    length=int(length)

#get width
    width=input("Enter the width in feet of the catchment area")
    width=int(width)

# calculate area
    tankVol=length*width*(height/12)
    Vol=Vol*7.65

#print results
    print("You need a tank with a",Vol,"gallons capacity to capture that much rain at one time.")

main()
