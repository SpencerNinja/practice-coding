# ISBN Assignment
# Spencer Hurd
# CS1410-03

# The function createIndex does not receive any parameters. It must return an empty dictionary for the index.
def createIndex():
    index = {}
    return index
# The function recordBook receives three parameters, the index dictionary, the ISBN of a book, and the title of book. Both the ISBN and title are strings. It must assign the title to the ISBN in the index. It does not return anything. However, the dictionary will be modified as a result of this function’s work.
def recordBook(index, ISBN, title):
    index[ISBN] = title
# The function findBook receives two parameters, the index dictionary and the ISBN of a book. The ISBN is a string. The function returns the title of the book with the matching ISBN, if it exists. If the ISBN is not in the dictionary, then it returns the empty string.
def findBook(index, ISBN):
    if ISBN in index:
        return index[ISBN]
    else:
        return ""
# The function listBooks receives one parameter, the index dictionary. The function returns a list of strings. Each string in the list is a line that shows a sequence number, the ISBN and the title of a book. See the examples for the format of the lines. If there are no books in the index, this function returns an empty list.
def listBooks(index):
    string = ""
    lst = []
    seq = 1
    for i in index: # i = key in dictionary
        string = (str(seq) + ") " + i + ": " + index[i])
        lst.append(string)
        seq = seq + 1
    return lst
# The function formatMenu does not receive any parameters. It must return a list of strings that contains the lines of the menu.
def formatMenu():
    menu = ['What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit']
    return menu
# The function formatMenuPrompt does not receive any parameters. It must return a string that contains the prompt to ask the user which menu option they would like to select.
def formatMenuPrompt():
    string = ('Enter an option: ')
    return string
# The function getUserChoice receives one parameter, a string that contains a prompt for input. It must return a string that contains the text input by the user, with any leanding and trailing whitespace removed. If the user gives an empty string, prompt them again, until they give a non-empty string. Note that this function interacts with the user, so there will be output to the screen and input from the keyboard when it is called.
def getUserChoice(string):
    reply = input(string).strip()
    while len(reply) == 0:
        reply = input(string).strip()
    return reply
# The function getISBN does not receive any parameters. It must prompt the user for an ISBN, and return the ISBN input by the user. The user’s response must not have any leading or trailing whitespace. It must repeatedly ask the user for an ISBN, until the user gives a non-empty response. Note, you should probably call getUserChoice as part of this function.
def getISBN():
    isbn = getUserChoice("Enter an ISBN: ")
    return isbn
# The function getTitle does not receive any parameters. It must prompt the user for a book title, and return the title input by the user. The user’s response must not have any leading or trailing whitespace. It must repeatedly ask the user for a title, until the user gives a non-empty response. Note, you should probably call getUserChoice as part of this function.
def getTitle():
    title = getUserChoice("Enter an book title: ")
    return title
# The function recordBookAction receives the index dictionary as a parameter. It must ask the user for the ISBN and title of a book, and add it to the dictionary. This function does not return anything. However, it has the side effect of adding an entry to the dictionary. It also interacts with the user through input and output. Note you should be using some of the above functions to complete this function.
def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    index[isbn] = title
# The function findBookAction receives the index dictionary as a parameter. It must ask the user for the ISBN of a book. If the book exists in the dictionary, it will display the book. If the book does not exist in the dictionary, it will give the user a message to let them know. The function does not return anything, and should not change the index.
# HELP 
def findBookAction(index):
    isbn = getUserChoice("Enter the ISBN to find the title of the book: ")
    if isbn in index:
        print(index[isbn])
    else:
        print("No book exists with that ISBN.")
# The function listBooksAction receives the index dictionary as a parameter. It will display all of the books in the dictionary in the format shown in the examples. If there are no books in the dictionary, it must display a message to inform the user. The function does not return anything. The function must not change the dictionary.
def listBooksAction(index):
    list_of_books = listBooks(index)
    for line in list_of_books:
        print(line)
# The function quitAction receives the index dictionary as a parameter. This function will display a message to the user indicating the end of the program. It will then terminate the program using sys.exit( 0 ). Be sure to do the correct import statement. This function does not return anything.
def quitAction(index):
    import sys
    print("Goodbye. Thanks for using the library search system.")
    sys.exit( 0 )
# The function applyAction receives the index dictionary and a choice string as parameters. This function will call the appropriate action function based on the choice string. If the choice string does not match any accepted choices, it will display a message to the user. This function does not return anything. The dictionary may be changed as a result of the chosen action.
def applyAction(index, choice):
    if choice == "r":
        recordBookAction(index)
    elif choice == "f":
        findBookAction(index)
    elif choice == "l":
        listBooksAction(index)
    elif choice == "q":
        quitAction(index)
    else:
        print('Not a valid option, please try again')    
# The function main receives no parameters, and returns nothing. This function ties everything together. Creating an index, repeatedly asking the user their choice and taking action.
def main():
    index = {}
    choice = input("What would you like to do? ")
    while True:
        choice = getUserChoice("What would you like to do? ")
        applyAction(index, choice)
# Lastly add this snippet at the bottom of your file which will execute your main() function when you run isbn_index.py but will allow it to be imported into the unittest files without executing the main function.
if __name__ == '__main__':
   main()
