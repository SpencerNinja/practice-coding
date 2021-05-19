# Caloric Balance - main.py
# Spencer Hurd
# CS 1410 TR 1:00 pm

# FILENAME: caloric_balance.py

# REFERENCE regarding calorie intake and calories burned
#     if calorieIntake == caloriesBurned:
#         no weight lost or gained
#     if calorieIntake > caloriesBurned:
#         weight gained
#     if calorieIntake == caloriesBurned:
#         weight lost

# Create a new class CaloricBalance
# Data Member: weight
# Keeps track of the user’s entered weight. This is used for calculating caloric burn of activities.
# Data Member: balance
# Keeps track of the user’s caloric balance throughout the day.
class CaloricBalance:
    def __init__(self, gender, age, height, weight):
        self.weight = weight  #pounds
        self.balance = -self.getBMR(gender, age, height, weight)
    # This constructor takes 4 additional parameters gender a string('f' or 'm'), age a float, height a float, and weight a float. It should store weight as a datamember and initialize balance as the negative value of the getBMR method. You can’t fully test this method until you complete the getBMR method. The unittests have been created to test appropriately.

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
    # This method receives 4 additional parameters gender a string('f' or 'm'), age a float, height a float, and weight a float. It should calculate and return the BMR using the calculations above. If the gender is not equal to 'm' or 'f' then the method returns 0.0

    def getBalance(self):
        return self.balance
    # This method receives no additional parameters and returns the value of the balance datamember.

    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        caloriesBPM = caloric_burn_per_pound_per_minute * self.weight  #BPM = Burned Per Minute
        totalCaloricBurn = caloriesBPM * minutes
        self.balance = self.balance - totalCaloricBurn
    # This method receives 2 additional parameters caloric_burn_per_pound_per_minute and minutes, both numbers(integer or float). It calculates the number of calories burned per minute by multiplying caloric_burn_per_pound_per_minute and the weight datamember then calculates the total caloric burn by multiplying the previous calculation by the minutes. It should subtract the total caloric burn from the balance datamember.
    
    def eatFood(self, calories):
        self.balance = self.balance + calories
    # This method takes 1 additional parameter calories a number(integer or float). It adds the calories to the current balance datamemeber.

