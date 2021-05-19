# Spencer Hurd
# CS 1410-03
# Tuesdays & Thursdays 1:00pm
# Word Zap!
# player.py

# Create a new class Player
# Data Members:
#     name - A string containing the user’s entered name.
#     letters - A list containing the letters in the player’s hand.
import random
class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()
    # The constructor takes 1 parameter: name - a string. It should store the name and initialize a data member letters a list to store the users letters.

    def getName(self):
        return self.name
    # This method receives no additional parameters and returns the value of the name data member.

    def getLetters(self):
        return self.letters
    # This method receives no additional parameters and returns the value of the letters data member.This should currently return an empty list until the next method is created.
    
    def drawLetter(self):
        ltrList = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        chosen = random.randrange(len(ltrList))
        self.letters.append(ltrList[chosen])
        return ltrList[chosen]
    # This method adds a randomly chosen letter and adds it to the player’s list of letters, it returns the letter the player drew.You might consider using the code below to choose your letter from (it is the character frequency of letters in a popular anagram game).
    # After you finish this method, update your constructor to call it 7 times so a player will start out with 7 random letters in their hand. Note: because the letters are chosen at random your output will be different than the examples.

    def printLetters(self):
        lineup = ""
        for i in range(len(self.letters)):
            lineup = lineup + self.letters[i] + " "
            # if i < len(self.letters)-1:     
            #     lineup = lineup + self.letters[i] + " "
            # else:
            #     lineup = lineup + self.letters[i]  
        lineup = lineup.strip()
        return lineup
    # This method takes the user’s letters and formats them into a pretty printed form. It should return a string of the letters separated by a single space. There should be no trailing space.

    def checkWord(self, word):
        original = self.letters.copy()
        for letter in word:
            ok = False
            for char in self.letters:
                if letter == char:
                    self.letters.remove(char)
                    ok = True
                    break
            if not ok:
                self.letters = original
                return False
        return True
    # This method takes 1 additional parameter: word - a string. If the word contains a letter that the player does not have, or the player does not have enough copies of the letter it should return False. Otherwise, update the player’s current letters removing the letters used to play the word and then return True.

        
