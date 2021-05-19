# REFERENCE from Caloric Balance

# FROM caloric_balance.py
class CaloricBalance:
    def __init__(self, gender, age, height, weight):
        self.weight = weight  # pounds
        self.balance = -self.getBMR(gender, age, height, weight)
    def getBMR(self, gender, age, height, weight):
        bmr = 0.0
        if gender == 'm':
            bmr = 66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
            return bmr
        elif gender == 'f':
            bmr = 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
            return bmr
        else:
            return 0.0
    def getBalance(self):
        return self.balance
    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        caloriesBPM = caloric_burn_per_pound_per_minute * \
            self.weight  # BPM = Burned Per Minute
        totalCaloricBurn = caloriesBPM * minutes
        self.balance = self.balance - totalCaloricBurn
    def eatFood(self, calories):
        self.balance = self.balance + calories

# FROM CB_main.py
import caloric_balance
def formatMenu():
    menu = ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']
    return menu
def formatMenuPrompt():
    string = ('Enter an option: ')
    return string
def formatActivityMenu(): 
    actMenu = ['Choose an activity to record:', '[b] Bicycling', '[j] Jump Rope', '[r] Running', '[s] Sitting', '[m] Swimming', '[w] Walking']
    return actMenu
def getUserString(string):
    reply = input(string).strip()
    while len(reply) == 0:
        reply = input(string).strip()
    return reply
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
def createCaloricBalance():
    gender = getUserString("What is your gender (f or m)? ")
    age = getUserFloat("What is your age? ")
    height = getUserFloat("What is your height in inches? ")
    weight = getUserFloat("What is your weight in pounds? ")
    return caloric_balance.CaloricBalance(gender,age,height,weight)
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
def eatFoodAction(cb):
    calories = getUserFloat("How many calories did you just eat? ")
    cb.eatFood(calories)
    print("Awesome! Your caloric balance is now ", str(cb.getBalance()))
import sys
def quitAction(cb):
    print("Leaving? You should do this again tomorrow. Stay healthy!")
    sys.exit(0)
def applyAction(cb, choice):
    if choice == "f":
        eatFoodAction(cb)
    elif choice == "a":
        recordActivityAction(cb)
    elif choice == "q":
        quitAction(cb)
    else:
        print('Not a valid option, please try again ')
def main():
    cb = createCaloricBalance()
    menu = formatMenu()
    while True:
        for i in menu:
            print(i)
        choice = getUserString(formatMenuPrompt())
        applyAction(cb, choice)
if __name__ == '__main__':
    main()



# from LEET TRANSLATOR
def get_index(char, alphabet):
    for char in alphabet:           # 1. for each index in alphabet
        if char == alphabet[i]:     # 2. if char == alphabet[i]
            return char             # 3. return index
def translate_char(char):
    leet_letters = "48CD3FGHIJK1MN0PQR57UVWXYZ@bcd3fghijk1mn0pqr57uvwxyz"
    eng_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    # 1. get the index in leet_letters of char
    g_index = get_index(char, alphabet)
    if char == None:                    # 2. if index is None
        return char                     # 2a. don't translate char, return char
    else:                               # 3. return letter in eng_letters with same index
        return eng_letters[char]
def translate_line(line):
    # 1. set up a new string for the translated line
    newstring = ""
    for char in line:                       # 2. for ever character in the line
        # 3. translate character, append to new string
        newstring = translate_char(line)
    return newstring
