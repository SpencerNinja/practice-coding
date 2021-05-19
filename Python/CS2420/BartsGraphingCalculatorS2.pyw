from graphics import *
import math

def PrintDirections():
    print("This program does this and that.")
    print("It works like this...")
    print("If I can see this, you do not pass off!")
    
def main():
    PrintDirections()
    equation = input("Enter your equation to draw: ")

    # Generate Data:
    xlow = 0
    ylow = -1
    xhigh = 2*math.pi
    yhigh = 1
    xinc = .1
    
    points = []
    x = xlow
    while x <= xhigh:
        y = math.sin(x) ############### <- Put your equation here!
        points.append( [x,y] )
        x += xinc

    # Draw Data:
    win = GraphWin("My Graphing Calculator", 500, 500)
    win.setCoords(xlow, ylow, xhigh, yhigh)
    for i in range(0, len(points)-1):
        l = Line( Point(points[i][0], points[i][1]), Point(points[i+1][0], points[i+1][1]))
        l.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
