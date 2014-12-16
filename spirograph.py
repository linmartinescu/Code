"""
   Use turtle graphics to draw a spirogrpah 

   author: Lindsay Martinescu
   revised: September 2014
"""
import turtle
import math

def initialize():
    """
	Initialize the turtle so that it is facing North
	with the pen up and in the home position @ 0,0
	Setup the window to be 800,600
	Background color to black, and window title
    """
    turtle.setup(800,600)
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Spirogrpah")
    turtle.colormode(255) # set color mode so red/green/blue is 0-255 each
    turtle.up()
    turtle.left( 90 )
    turtle.home()
    turtle.speed(200)
    
def formulaX(R, r, p, t):
    """
    Calculate X point based on inputs
    """
    return (R-r)*math.cos(t) - (r+p)*math.cos((R-r)/r*t)

def formulaY(R, r, p, t):
    """
    Calculate Y point based on inputs
    """
    return (R-r)*math.sin(t) - (r+p)*math.sin((R-r)/r*t)

def pickColor(t):
    """
      Calculate an RGB color tuple that is smooth through a color wheel
      Returns an RGB tuple (r,g,b) where each value is in the range 0-25
      (Looked up various algorithms for colour)
    """
    h = t + 0.5
    h *= -1
    r = int(255*math.sin(math.pi * h)**2)
    g = int(255*math.sin(math.pi * (h + 1/3))**2)
    b = int(255*math.sin(math.pi * (h + 2/3))**2)
    return (r,g,b)

def drawZero(R,r,p):
    """
    precondition: none
    Draw to origin point
    postcondition: turtle orientation is unchanged, new location is x,y calculated for value of 0
    """
    x = formulaX(R,r,p,0)
    y = formulaY(R,r,p,0)
    turtle.goto(x,y)

def drawRecursive(R,r,p,t):
    """
     precondition: none
     Draw to point for current value of t, then recurse for t-0.01. Exit when we hit 0
     inputs: 
           R = raidus of fixed circle
           r = radius of moving circle
           p = offset of pen in moving circle
           t = values from 0 to 2**PI
     postcondition: turtle orientation is unchanged, pen up/down is unchanged
    """
    if (t <= 0.0):
        return
    x = formulaX(R,r,p,t)
    y = formulaY(R,r,p,t)
    color = pickColor(t)
    turtle.pencolor(color)
    turtle.goto(x,y)
    drawRecursive(R,r,p,t-0.01)
    

def drawSpirograph(R,r,p):
    """
       Draw the spirograph.  First move to x/y for value of 0, then invoke draw routine, starting @ 2**PI
    """
    turtle.up()
    # move to origin with out drawing
    drawZero(R,r,p)
    # start drawing
    turtle.down()
    drawRecursive(R,r,p,2*math.pi)
    # connect back to origin
    drawZero(R,r,p)

def main():
    """
        Creates window and gets turtle ready
	Defines terms and checks if in range, if not prints statement
        Hides the turtle
        Draws the spirograph
	Waits for user to end program
    """
    R = 100.0
    r = 4.0
    p = int(input("The offset of the pen point, between <10 - 100>: "))

    if p < 10 or p > 100:
        input("Incorrect value for p!")

    initialize()
    turtle.hideturtle()
    drawSpirograph(R,r,p*1.0)
    input("Hit enter to close...")
    turtle.bye()

main()

