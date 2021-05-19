# Gas Mileage Assignment
# Spencer Hurd
# CS1410-03

# In order to calculate gas mileage, you should store the number of miles traveled and the number of gallons added as float values. Here is a simple way to convert a string or integer value to a float value:
#     gallons = float(gallons)

def milesPerGallon(miles, gallons):
    if gallons == 0:
        return 0
    else:
        mpg = miles / gallons
    return mpg
# The function milesPerGallon receives two parameters, miles and gallons, both numbers(floats or integers). It returns the float value from dividing miles by gallons. If the value of gallons equals zero the function should return 0.0. There is no need to round the returned values.

def createNotebook():
    notebook = []
    return notebook
# The function createNotebook does not receive any parameters.It must return an empty list to use as a “notebook” to track your trip data.

def recordTrip(notebook, date, miles, gallons):
    record = {'date':date, 'miles':miles, 'gallons':gallons}
    notebook.append(record)
# The function recordTrip takes four parameters, the notebook list, the date of the trip(a string), the miles traveled(a float), and the gallons of gas pumped(a float). It creates a new dictionary for the trip and adds it to the notebook list. The function does not return anything, but it will update the notebook list. Note: the order of the pairs in the trip dictionary does not matter.

def listTrips(notebook):
    string = ""
    lst = []
    for trip in notebook: # each trip is a dictionary key and value inside the list notebook
        miles = str(trip["miles"])
        gallons = str(trip["gallons"])
        mpg = milesPerGallon(float(miles), float(gallons))
        string = "On "
        string += trip["date"]
        string += ": "
        string += miles
        string += " miles traveled using "
        string += gallons
        string += " gallons. Gas mileage: "
        string += str(mpg)
        string += " MPG"
        lst.append(string)
    return lst
# The function listTrips take one parameter, the notebook list. The function returns a list of strings. Each string in the list is a line that contains the date of the trip, the miles travel, the gallons pumped, and the miles per gallon(mpg) for that trip. Consider using the milesPerGallon function from above. See the example from above for an example on how to format the line. If there are no trips in the notebook, the function returns an empty list. The function should not modify the notebook. You may round your float numbers to 2 decimal places, but it is not required.

def calculateMPG(notebook):
    averageMPG = 0
    miles = 0.0
    gallons = 0.0
    for dictionary in notebook:
        miles = miles + dictionary["miles"]
        gallons = gallons + dictionary["gallons"]
    if gallons == 0:
        return 0.0
    else:
        averageMPG = miles / gallons
    return averageMPG
# The function calculateMPG takes one parameter, the notebook list.The function calculates the Average MPG(calculated from total miles and total gallons) for all trips recorded and returns it as a float. You should not round the values. If there are no trips in the notebook the function returns 0.0. Do not use milesPerGallon function from above. You should sum all the miles and sum all the gallons. Using those sums, calculate the average.The function should not modify the notebook.

def formatMenu():
    menu = ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']
    return menu
# The function formatMenu does not receive any parameters.It must return a list of strings that contains the lines of the menu.

def formatMenuPrompt():
    string = ('Enter an option: ')
    return string
# The function formatMenuPrompt does not receive any parameters.It must return a string that contains the prompt to ask the user which menu option they would like to select.

def getUserString(string):
    reply = input(string).strip()
    while len(reply) == 0:
        reply = input(string).strip()
    return reply
# The function getUserString receives one parameter, a string that contains a prompt for input.It must return a string that contains the text input by the user, with any leading and trailing whitespace removed.If the user gives an empty string, prompt them again, until they give a non - empty string.Note that this function interacts with the user, so there will be output to the screen and input from the keyboard when it is called.

def getUserFloat(string):
    inputFloat = -1
    while inputFloat <= 0:
        try:
            inputFloat = float(input(string))
            if inputFloat <= 0:
                print("Please enter a number greater than zero.")
        except:
            print("Please enter a number.")
    return inputFloat
# The function getUserFloat receives one parameter, a string that contains a prompt for input. It must return a float that contains the number input by the user.If the user enters a non - number or a number less than or equal to zero it should prompt them again.To accomplish this you might consider using a try / except clause which allows you to try an execute some code(convert user’s input to a float) and recover if it fails.

def getDate():
    date = getUserString("Please enter the date (MM/DD/YYYY): ").strip()
    return date
# The function getDate does not receive any parameters. It must prompt the user for a date and return the date input by the user.The user’s response should not contain leading or trailing whitespace. The function should continue to ask the user for input until the user gives a valid response.Consider calling getUserString.

def getMiles():
    miles = getUserFloat("How many miles did you drive since last filling up? ")
    return miles
# The function getMiles does not receive any parameters. It must prompt the user to input a number and return the float value of that number. The function should continue to prompt the user until their input is valid(float or integer greater than zero).Consider calling getUserFloat.

def getGallons():
    gallons = getUserFloat("How many gallons of gas did you add to your tank? ")
    return gallons
# The function getGallons does not receive any parameters. It must prompt the user to input a number and return the float value of that number.The function should continue to prompt the user until their input is valid(float or integer greater than zero).Consider calling getUserFloat.

def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print("Trip saved.")
# The function recordTripAction receives one parameter, the notebook list. It must prompt the user for the date, miles traveled, and gallons pumped and record it in the notebook. All inputs must be valid. Consider using functions from above. Print a message to the user so they know the trip was saved.

def listTripsAction(notebook):
    trips = listTrips(notebook)
    list_of_trips = ""
    if len(trips) == 0:
        print("There are no trips to list.")
    else:
        list_of_trips = listTrips(notebook)
        for line in list_of_trips:
            print(line)
# The function listTripsAction receives one parameter, the notebook list. It will display all of the trips in the format shown in the examples. If there are no trips in the notebook, it must display a message to inform the user. The function does not return anything.The function must not change the notebook.

def calculateMPGAction(notebook):
    trips = listTrips(notebook)
    if len(trips) == 0:
        print("There is no trip data.")
    else:
        mpg = calculateMPG(notebook)
        print("Average gas mileage: " + str(mpg) + " MPG")
# The function calculateMPGAction receives one parameter, the notebook list. It should print the average MPG to the user. If there are no trips in the notebook it should display a message notifying the user there is no trip data. The function must not change the notebook. You may round your float number to 2 decimal places, but it is not required.

def quitAction(notebook):
    import sys
    print("Goodbye. Thanks for using the library search system.")
    sys.exit(0)
# The function quitAction receives the notebook list as a parameter. This function will display a message to the user indicating the end of the program.It will then terminate the program using sys.exit(0). Be sure to do the correct import statement. This function does not return anything.

def applyAction(notebook, choice):
    if choice == "r":
        recordTripAction(notebook)
    elif choice == "l":
        listTripsAction(notebook)
    elif choice == "c":
        calculateMPGAction(notebook)
    elif choice == "q":
        quitAction(notebook)
    else:
        print('Not a valid option, please try again')
# The function applyAction receives the notebook list and a choice string as parameters. This function will call the appropriate action function based on the choice string. If the choice string does not match any accepted choices, it will display a message to the user. This function does not return anything. The notebook may be changed as a result of the chosen action.

def main():
    notebook = []
    choice = ""
    while True:
        choice = getUserString("What would you like to do? ")
        applyAction(notebook, choice)
# The function main receives no parameters, and returns nothing. This function ties everything together. Create a notebook, repeatedly asking the user their choice and taking appropriate action. Note: everything you need to finish the main function should be contained in the functions above.

# Lastly add this snippet at the bottom of your file which will execute your main() function when you run gas_mileage.py but will allow it to be imported into the unittest files without executing the main function.
if __name__ == '__main__':
    main()
