"""
   Use turtle graphics to draw the jester graphic

   author: Lindsay Martinescu
   revised: September 2014
"""
import turtle
import math

def initialize():
    """
	Initialize the turtle so that it is facing North
	with the pen up and in the home position @ 0,0
	Setup the window to be 600,600
	Background color to light blue, and window title
    """
    turtle.setup(600,600)
    turtle.setworldcoordinates(-300,-50,300,550)
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    wn.title("Jester")
    turtle.up()
    turtle.left( 90 )
    turtle.home()
    turtle.speed(100)

def colourSetUp(depth):
    """
        precondition: none
        Will set pen color based on odd or even depth
        postcondition: turtle pen is up, orientation and poisition are the same as upon entry, color is set based on depth
    """
    if (depth%2 == 0):
        turtle.pencolor("orange")
    else:
        turtle.pencolor("green")

   
def drawSquares(size):
    """
        precondition: none
        Draws small squares
        postcondition: turtle pen is up, orientation and position are the same as upon entry
    """
    turtle.down()
    turtle.forward(size/2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size/2)
    turtle.up()
    
def drawCircle(size):
    """
        precondition: none
        Draws a circle
        Size is input as radius of circle
        postcondition: turtle pen is up, orientation and position are the same as upon entry
    """
    turtle.down()
    turtle.circle(size)
    turtle.up()
    
def jesterRec(depth,size,maxdepth):
    """
    main drawing function, called recursively with increasing depth
    precondition: none
    postcondition: pen is up and orientation/position is same as upon entry
    """
    colourSetUp(depth)
    if (depth == maxdepth):
        drawCircle(size/2)
        return
    else:
        drawSquares(size)
        turtle.back(size/2)
        turtle.left(90)
        turtle.forward(size)
        turtle.right(45)
        jesterRec(depth+1,size/2,maxdepth)
        turtle.right(45)
        turtle.forward(size)
        turtle.right(45)
        jesterRec(depth+1,size/2,maxdepth)
        turtle.left(45)
        turtle.back(size)
        turtle.left(90)
        turtle.back(size)
        turtle.right(90)
        turtle.forward(size/2)

    
    
    
def main(): 
    initialize()
    depth = int(input("Enter depth: "))
    size=100
    jesterRec(0,size,depth)
    input("Press enter to exit")
   

main()
