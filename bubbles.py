"""
   Use turtle graphics to draw the jester graphic

   author: Lindsay Martinescu
   revised: September 2014
"""
import turtle
import math
import random

def initialize():
    """
	Initialize the turtle so that it is facing North
	with the pen up and in the home position @ 0,0
	Setup the window to be 600,600
	Background color to Black, and window title
	Hide turtle and set up x,y
    """
    turtle.setup(600,600)
    wn = turtle.Screen()
    wn.bgcolor("Black")
    wn.title("Bubbles")
    turtle.colormode(255) # set color mode so red/green/blue is 0-255 each
    turtle.up()
    turtle.left( 90 )
    turtle.home()
    turtle.speed(200)
    turtle.hideturtle()
    (x,y)= turtle.position()

def boundBox():
    """
	Draw the bounding box in white using preset conditions
	Ends by going back to 0,0
    """
    turtle.pencolor("white")
    turtle.goto(MIN_X(),MIN_Y())
    turtle.left(90)
    turtle.down()
    turtle.forward(abs(MIN_X())+MAX_X())
    turtle.right(90)
    turtle.forward(abs(MIN_Y())+MAX_Y())
    turtle.right(90)
    turtle.forward(abs(MIN_X())+MAX_X())
    turtle.right(90)
    turtle.forward(abs(MIN_Y())+MAX_Y())
    turtle.up()
    turtle.goto(0,0)

def drawCircle(color,radius):
    """
	Draws a circle
	Fills with random colour at random radius
    """
    turtle.down()
    turtle.color(color,color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    
def pickRadius():
    """
	Random Range to pick a radius between a range of 1-20
    """
    radius = random.randint(MIN_RADIUS(),MAX_RADIUS())
    return radius

def pickColour(t):
    """
      Calculate an RGB color tuple that is smooth through a color wheel
      Returns an RGB tuple (r,g,b) where each value is in the range 0-255
      (Looked up various algorithms for colour)
    """
    phi = (1+5**0.5)/2
    h = t*phi + 0.5
    h *= -1
    r = int(255*math.sin(math.pi * h)**2)
    g = int(255*math.sin(math.pi * (h + 1/3))**2)
    b = int(255*math.sin(math.pi * (h + 2/3))**2)
    return (r,g,b)
    
def pickDirection():
    """
	Random Range to pick a turn direction -30,30 degrees
    """
    turtle.right(random.randrange(-1*MAX_ANGLE(),MAX_ANGLE()))

def moveTurtle(radius):
    """
	Checks turtle's heading in relation to bounding box
	Moves turtle to avoid hitting sides
    """
    distance = random.randrange(MIN_DISTANCE(),MAX_DISTANCE());
    pickDirection()
    heading = turtle.heading()
    turtle.forward(distance)
    x,y = turtle.position()
    if (x+radius > MAX_X() or x-radius < MIN_X() or y+radius > MAX_Y() or y-radius < MIN_Y()):
        turtle.backward(distance)
        turtle.right(180)
        moveTurtle(radius)

def bubblesRec(n):
    """
	Draws the bubbles recursively
	Takes in n - number of bubbles
	Returns sum
    """
    if n == 0:
        return 0
    radius = pickRadius()
    color = pickColour(n)
    moveTurtle(radius)
    drawCircle(color,radius)
    return radius + bubblesRec(n-1)
    
def bubblesIter(n):
    """
	Draws the bubbles using iterations
	Takes in n - number of bubbles
	Returns sum
    """
    sumRadius = 0
    for i in range(n):
        radius = pickRadius()
        sumRadius = sumRadius + radius
        color = pickColour(i)
        moveTurtle(radius)
        drawCircle(color,radius)
    return sumRadius

def MAX_BUBBLES():
    """
	Max number of bubbles
    """
    return 500

def MIN_BUBBLES():
    """
	Min number of bubbles
    """
    return 0

def MIN_X():
    """
	Min value for x coordinate 
    """
    return -200

def MIN_Y():
    """
	Min value for y coordinate
    """
    return -200

def MAX_X():
    """
	Max value for x coordinate 
    """
    return 200

def MAX_Y():
    """
	Max value for y coordinate
    """
    return 200

def MAX_DISTANCE():
    """
	Max distance
    """
    return 20

def MIN_DISTANCE():
    """
	Min distance
    """
    return 1

def MAX_ANGLE():
    """
	Max angle
    """
    return 30

def MIN_RADIUS():
    """
	Min value for radius
    """
    return 1

def MAX_RADIUS():
    """
	Max value for radius
    """
    return 20

def main():
    """
	Prompts user for number of bubbles and checks if in range
	Calls intialize function to set up window
	Draws bounding box
	Draws bubbles recursively and prints sum value
	User input, then clears window
	Resets up window and draws box
	Draws bubbles by iterations and prints sum value
	Waits for input and ends program
    """ 
    n = int(input("How many bubbles? "))
    if n < MIN_BUBBLES() or n > MAX_BUBBLES():
        input("Incorrect value for n!")
        turtle.bye()
    else:
        initialize()
        boundBox()
        sumRadius1 = bubblesRec(n)
        print ("Total radius for recursion: ",sumRadius1)
        input("Press enter for next drawing..")
        turtle.clear()
        initialize()
        boundBox()
        sumRadius2 = bubblesIter(n)
        print ("Total radius for loop: ",sumRadius2)
        input("Press enter to exit")
        turtle.bye()
   

main()

