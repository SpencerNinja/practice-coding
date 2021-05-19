# Name Guesser 2/15/2019
# Spencer Hurd

# Instructions
## print the introduction challenge
## input 1st guess and return result
## input 2nd guess and return result
## input 3rd guess and return result

# Challenge Instructions
print("Hello, can you guess my name?")
print("If you can guess it, I will give you a pizza.")
print("You have three attempts.")
print("If you fail, you have to give me a pizza!")

# Input Guesses
name=""
name = input("What is my name? ")
while name != "Spencer":
    print ("Nice try, but that is not my name.")
    print ("What is my name?")
    name=input()
while name == "Spencer":
    if name == "Spencer":
        print ("You guessed my name! The pizza is yours.")
    break
