# Caloric Balance - main.py
# Spencer Hurd
# CS 1410 TR 1:00 pm

# FILENAME: main.py

import caloric_balance
# Create the following functions in your main.py file. You will need to also import and use your CaloricBalance class from caloric_balance.py.

# Because of the user input and output, not all functions are easily tested with unit tests. Be sure to test these functions by running your program and observing the correct behavior.

def formatMenu():
    menu = ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']
    return menu
# The function formatMenu does not receive any parameters. It must return a list of strings that contains the lines of the menu.

def formatMenuPrompt():
    string = ('Enter an option: ')
    return string
# The function formatMenuPrompt does not receive any parameters. It must return a string that contains the prompt to ask the user which menu option they would like to select.

def formatActivityMenu(): 
    actMenu = ['Choose an activity to record:', '[b] Bicycling', '[j] Jump Rope', '[r] Running', '[s] Sitting', '[m] Swimming', '[w] Walking']
    return actMenu
# The function formatActivityMenu does not receive any parameters. It must return a list of strings that contains the lines of the activities menu. (Your activities can be different than the example below)

def getUserString(string):
    reply = input(string).strip()
    while len(reply) == 0:
        reply = input(string).strip()
    return reply
# The function getUserString receives one parameter, a string that contains a prompt for input. It must return a string that contains the text input by the user, with any leading and trailing whitespace removed. If the user gives an empty string, prompt them again, until they give a non-empty string. Note that this function interacts with the user, so there will be output to the screen and input from the keyboard when it is called.

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
# The function getUserFloat receives one parameter, a string that contains a prompt for input. It must return a float that contains the number input by the user. If the user enters a non-number or a number less than or equal to zero it should prompt them again. To accomplish this you might consider using a try/except clause  which allows you to try an execute some code(convert user’s input to a float) and recover if it fails.

def createCaloricBalance():
    gender = getUserString("What is your gender (f or m)? ")
    age = getUserFloat("What is your age? ")
    height = getUserFloat("What is your height in inches? ")
    weight = getUserFloat("What is your weight in pounds? ")
    return caloric_balance.CaloricBalance(gender,age,height,weight)
# This function receives no parameters. It will prompt the user for their gender(f or m), their age(float or int), their height in inches(float or int), and their weight in pounds(float or int). It will create an instance of CaloricBalance and return that instance.
# You will need to import your caloric_balance module.

def recordActivityAction(cb):
    for i in formatActivityMenu():
        print(i)
    activity = getUserString(formatMenuPrompt())
    if activity == 'b':
        b = 0.029
        minutes = getUserFloat("For how many minutes did you perform this activity? ")
        cb.recordActivity(b, minutes)
    elif activity == 'j':
        j = 0.074
        minutes=getUserFloat("For how many minutes did you perform this activity? ")
        cb.recordActivity(j, minutes)
    elif activity == 'r':
        r = 0.087
        minutes=getUserFloat("For how many minutes did you perform this activity? ")
        cb.recordActivity(r, minutes)
    elif activity == 's':
        s = 0.009
        minutes=getUserFloat("For how many minutes did you perform this activity? ")
        cb.recordActivity(s, minutes)
    elif activity == 'm':
        m = 0.058
        minutes=getUserFloat("For how many minutes did you perform this activity? ")
        cb.recordActivity(m, minutes)
    elif activity == 'w':
        w = 0.036
        minutes=getUserFloat("For how many minutes did you perform this activity? ")
        cb.recordActivity(w, minutes)
    else:
        print("Sorry, that option is invalid.")
        return
    print("Awesome! Your caloric balance is now ", str(cb.getBalance()))
# This function receives one parameter a CaloricBalance instance. It prints the activities menu and prompts the user to choose an activity. If the user enters a valid option it then prompts the user to enter the number of minutes of activity and then calls the recordActivity method on the instance(to do this you need to map the activity option to a value from the activities table linked above). Lastly it should print a success message to the user with their new caloric balance. If the user enters an invalid option it should print an error message, then return.

def eatFoodAction(cb):
    calories = getUserFloat("How many calories did you just eat? ")
    cb.eatFood(calories)
    print("Awesome! Your caloric balance is now ", str(cb.getBalance()))
# This function receives one parameter a CaloricBalance instance. It prompts the user to enter the number of calories consumed. It then calls the eatFood method on the instance. Lastly it should print a success message to the user with their new caloric balance.
import sys
def quitAction(cb):
    print("Leaving? You should do this again tomorrow. Stay healthy!")
    sys.exit(0)
# This function receives one parameter a CaloricBalance instance. This function will display a message to the user indicating the end of the program. It will then terminate the program using sys.exit(0). Be sure to do the correct import statement. This function does not return anything.

def applyAction(cb, choice):
    if choice == "f":
        eatFoodAction(cb)
    elif choice == "a":
        recordActivityAction(cb)
    elif choice == "q":
        quitAction(cb)
    else:
        print('Not a valid option, please try again ')
# This function receives two parameters a CaloricBalance instance, and choice a string. This function will call the appropriate action function based on the choice string. If the choice string does not match any accepted choices, it will display a message to the user. This function does not return anything.

def main():
    # print("This program calulates your calorie balance for the day.")
    # print("Before we can start, I need some information about you. Please be honest.")
    # print("Thanks! Now throughout the day, tell me each time you eat or move.")
    # print("your caloric balance is starting at ", balance, " (you need to eat something).")
    cb = createCaloricBalance()
    menu = formatMenu()
    while True:
        for i in menu:
            print(i)
        choice = getUserString(formatMenuPrompt())
        applyAction(cb, choice)
# The function main receives no parameters, and returns nothing. This function ties everything together. Creates an instance of CaloricBalance, repeatedly asking the user their choice and taking appropriate action. Note: everything you need to finish the main function should be contained in the functions above.

if __name__ == '__main__':
    main()
# Lastly add this snippet at the bottom of your file which will execute your main() function when you run main.py but will allow it to be imported into the unittest files without executing the main function.

