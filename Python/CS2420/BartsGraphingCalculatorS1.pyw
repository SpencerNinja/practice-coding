from graphics import *
import math

def PrintInstructions():
    print("If it says this, you don't pass off!")
    
def main():
    PrintInstructions()

    # Generate the points in the curve:
    points = []
    xlow = -10
    ylow = -10
    xhigh = 10
    yhigh = 10
    xinc = .1
    
    x = xlow
    epsilon = .00001
    while x <= xhigh+epsilon:
        y = x*.5 # replace this with Whatever the user enters
        points.append( [x,y] )
        x += xinc        

    # Draw the points in the curve
    win = GraphWin("My Circle", 500, 500)
    win.setCoords(xlow, ylow, xhigh,yhigh)
    for i in range(len(points)-1):
        l = Line( Point(points[i][0], points[i][1]), Point(points[i+1][0], points[i+1][1]) )
        l.draw(win)
#        c = Circle(Point(points[i][0], points[i][1]), .2)
#        c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
