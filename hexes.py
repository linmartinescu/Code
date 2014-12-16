"""
   Use turtle graphics to draw a hexagon.

   author: Lindsay Martinescu
   revised: August 2014
"""

import turtle
import math

def initialize():
    """
	Initialize the turtle so that it is facing North
	with the pen up and in the home position @ 0,0
	Setup the window to be 800,600
	Background color to violet, and window title
    """
    turtle.setup(800,600)
    wn = turtle.Screen()
    wn.bgcolor("violet")
    wn.title("Lindsay's Hexagons")
    turtle.up()
    turtle.left( 90 )
    turtle.home()

def drawHexagonSide(size):
    """
	Draw one hexagon side and turn turtle to get ready for next side
    """
    turtle.down()
    turtle.forward( size )
    turtle.right( 60 )
    turtle.up()

def drawHex (x,y):
    """
	Draw a hexagon
	Starting at point x,y.
	Loop and draw 6 sides
    """
    turtle.up()
    turtle.setposition(x,y)
    for _ in range(6):
        drawHexagonSide(50)


def main():
    """
        Creates window and gets turtle rerady
	Draws each Hexagon using x,y points
	Waits for user to end program
    """
    initialize()
    drawHex(0,0)
    drawHex(-75, 25*math.sqrt(3))
    drawHex(75, 25*math.sqrt(3))
    drawHex(75, 130)
    drawHex(-75, 130)
    drawHex(0 , 174)
    wn = turtle.Screen()
    input("Hit ENTER")
    turtle.bye()
	
# now call the main function to run the code

main()
