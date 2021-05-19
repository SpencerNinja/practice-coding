# Spencer Hurd
# CS 1410-03
# Tuesdays & Thursdays 1:00pm
# Word Zap!
# main.py

# We are not providing unittests for main.py because it is too difficult to test a program this dynamic, we will have to rely on Acceptance Testing to verify it works as expected. It is up to you to figure out how to finish the game using the player class. Here is a list of functions that might be useful to you. You are not required to create any of them. As you work on this if you see any other functions that might be useful to other students feel free to suggest them.
import player
def getUserInt(number):
    inputInt = -1
    while inputInt <= 0:
        try:
            inputInt = int(input(number))
            if inputInt <= 0:
                print("Please enter a number greater than zero.")
        except:
            print("Please enter a number.")
    return inputInt
# getUserInt - Similar to getUserFloat from the previous 2 assignments but instead of casting the user input to a float, cast it to an int

def getUserString(string):
    reply = input(string).strip()
    # while len(reply) == 0:
        # reply = input(string).strip()
    return reply
# getUserString - Similar to getUserString from previous assignments, except an empty string should be ok(so a user can skip their turn)

def getPlayers():
    name = ""
    playerNames = []
    numPlayers = getUserInt("How many players will be playing? ")
    for i in range(numPlayers):
        name = getUserString("Enter the name for player " + str(i+1) + ": ")
        playerNames.append(player.Player(name))
    return playerNames
# getPlayers - Ask the user how many players will be playing(consider using getUserInt). Ask the user for a name and create an instance of Player for the number of entered players. Return a list of the Player instances.

def convertToLower(word):
    lowerWord = ""
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    for letter in word:
        for char in range(len(upper)):
            if letter == upper[char]:
                lowerWord = lowerWord + lower[char]
            elif letter == lower[char]:
                lowerWord = lowerWord + letter
    return lowerWord
# convertToLower - Convert a user’s entered word to lowercase. So if they type in an A it counts as a.

def gameNotOver(players):
    for p in players:
        if len(p.getLetters()) == 0:
            return False
    return True

def main():
    print("Welcome! Time to play! Try to use all of your letters.")
    print("The first player that uses all of their letters wins!")
    print("")
    players = getPlayers()
    print("Great! Now we can play!")
    print("")
    while gameNotOver(players) == True:  # while each player has letters
        for p in players: # for each player(turn)  -- start of each round
            print(p.getName(), ", it is your turn!")  # display player name
            print("Your letters are: ", p.getLetters())  # print letters
            word = getUserString("Enter a word made up from the letters you have: ")  # Enter a word to play(or press enter to pass)
            if len(word) == 0:
                p.drawLetter()
            check = p.checkWord(word)
            while check != True: # while the input does not match the letters the player has
                word = getUserString("Check your letters and try again: ")
                check = p.checkWord(word)
            print("Great job!")
            print("")
        print("Okay! Next round!")
        print("")
    for p in players:
        if len(p.getLetters()) == 0:
            print(p.getName(), " wins!")  # print winner
            # break   <- input this break if you want to print the winner that ran out first
main()
# Your file should consist of of main() function which is called to execute your program.

# Pass-off instructions
# To pass off this assignment you need to show your completed program to the lab assistants.
# Show them your player.py and main.py code
# Run test_all.py - All tests MUST pass!
# Run main.py
# The lab assistants may have additional tests they want you to run.
# Upload your player.py and main.py files to canvas(you may zip them), please add a comment to the top of the files with your name and time your class meets.
