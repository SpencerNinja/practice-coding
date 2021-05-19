from graphics import *
import math


class Stack:

    def __init__(self):
        self.lst = []           # create the stack in the form of a list

    def pop(self):              # pulls item off the stack
        return self.lst.pop()

    def push(self, item):             # puts item on the stack
        return self.lst.append(item)

    def top(self):              # checks what is on top of stack
        return self.lst[-1]

    def empty(self):  # checks if stack is empty
        return len(self.lst) == 0


def InfixToPostfix(infix):
	postfix = ""		# create an empty string to store Post Fix expression
	s = Stack()			# assign class to shortcut variable
	for c in infix: 			# c = character
		if c >= '0' and c <= '9':		# if character is 0 - 9
			postfix += c				# add to postfix string
		elif c == "x":
			postfix += c
		elif c in "+-*/":			# otherwise, if character is an operator
			while not s.empty() and s.top() in "+-*/": 	# if stack is not empty and an operator is not on stack
				postfix += s.pop()	# pop the number from the stack and put it in postfix string
			s.push(c)  # put character on the stack
		elif c == "(":
			s.push(c)		# puts left parenthesis on stack
		elif c == ")":
			while s.top() != "(":	# checks if top of stack is "("
				postfix = postfix + s.pop()		# stores in postfix string
			s.pop()  # removes left parenthesis from stack
	while not s.empty():
		postfix += s.pop()
	return postfix

def EvaluatePostFix(postfix, x):  # postfix = 3 4 x * +, x = -10
	s = Stack()
	result = 0
	# for character c in postfix, convert number to float
	for c in postfix:
		if c >= '0' and c <= '9':			# if character is 0-9
			first = s.push(float(c))	# push onto stack
		elif c == "x":						# if character is "x"
			s.push(float(x))			# push onto stack
		elif c == "+":						# addition
			r = s.pop()					# pop number
			l = s.pop()					# pop number
			result = l + r					# execute operator
			s.push(float(result))		# push the result
		elif c == "-":						# subtraction
			r = s.pop()
			l = s.pop()
			result = l - r
			s.push(float(result))
		elif c == "*":						# multiplication
			r = s.pop()
			l = s.pop()
			result = l * r
			s.push(float(result))
		elif c == "/":						# division
			r = s.pop()
			l = s.pop()
			result = l / r
	return float(result)					# return as a float

def main():
	print("Welcome to the graphing calculator.") 			# print instructions
	print("You can use any number from 0 - 9, and the operators: + - * / ( )")
	print("Do not type any spaces!")
	print("Example: (x+1)*4/x")
	infixExpression = input("Enter your formula: ")	# input statement
	postFixExpression = InfixToPostfix(infixExpression)				# convert infix to postfix
	print(postFixExpression)
	# parse string
	points = []			
    # generate data
	xlow = -10			# left edge of screen
	ylow = -10			# bottom edge of screen
	xhigh = 10			# right edge of screen
	yhigh = 10			# top edge of screen
	xinc = .1			# increment value
	x = xlow			# starting point
	# for x in range(-10, +10, .1):	(alternate display, display is more jagged)
	while x < xhigh:		# smoother display
		y = EvaluatePostFix(postFixExpression, x)		# function goes here
		points.append([x, y])		# add value to points list in form of ordered pair (tuple)
		x = x + xinc  				# add increment to x
	win = GraphWin(postFixExpression, 700, 700) 	
	# set bottom left corner to -10 -10 and top right corner to +10
	win.setCoords(-10, -10, +10, +10)  # and +10 and write between those
	ln = Line(Point(-10, 0), Point(10, 0)) # x axis
	ln.draw(win)
	ln = Line(Point(0, -10), Point(0, 10)) # y-axis
	ln.draw(win)
	for i in range(len(points)-1):  # plot line using points
		p1 = points[i]		# first point
		p2 = points[i+1]  # second point
		# form a line from point 1 to point 2
		ln = Line(Point(p1[0], p1[1]), Point(p2[0], p2[1]))
		# Circle(Point(p[0], p[1]), .1)
		ln.draw(win)		# Draw graph
	win.getMouse() 			# Pause to view result
	win.close()				# Close window when done
main()
