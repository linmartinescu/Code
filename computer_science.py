"""
   Use turtle graphics to write Computer Science.

   author: Lindsay Martinescu
   revised: September 2014
"""

import turtle

def initialize():
    """
	Initialize the turtle so that it is facing North
	with the pen up and in the home position @ 0,0
	Setup the window to be 800,600
	Background color to light green, and window title
    """
    turtle.setup(800,600)
    wn = turtle.Screen()
    wn.bgcolor("light green")
    wn.title("Computer Science")
    turtle.up()
    turtle.left( 90 )
    turtle.home()

def setUp(x,y):
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()

def drawC(x,y):
    """
	Draws the letter C
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()

def draw0(x,y):
    """
	Draws the letter O
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()

def drawM(x,y):
    """
	Draws the letter M
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(135)
    turtle.forward(20)

def drawP(x,y):
    """
	Draws the letter P
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.right(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()

def drawU(x,y):
    """
	Draws the letter U
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.up()

def drawT(x,y):
    """
	Draws the letter T
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(20)
    turtle.up()

def drawE(x,y):
    """
	Draws the letter E
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()

def drawR(x,y):
    """
	Draws the letter R
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(135)
    turtle.forward(17)
    turtle.up()

def drawS(x,y):
    """
	Draws the letter S
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.right(135)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.up()

def drawI(x,y):
    """
	Draws the letter I
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(180)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(180)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.forward(20)
    turtle.up()

def drawN(x,y):
    """
	Draws the letter N
	Starting at point x,y.
    """
    setUp(x,y)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(135)
    turtle.forward(27)
    turtle.left(135)
    turtle.forward(20)
    turtle.up()

def main():
    """
        Creates window and gets turtle ready
	Draws each letter using x,y points
	Waits for user to end program
    """
    initialize()
    drawC(-220,0)
    draw0(-190,0)
    drawM(-180,0)
    drawP(-150,0)
    drawU(-120,20)
    drawT(-80,0)
    drawE(-40,0)
    drawR(-30,0)
    drawS(50,20)
    turtle.left(180)
    drawC(80,0)
    drawI(100,0)
    drawE(140,0)
    drawN(150,0)
    turtle.left(270)
    drawC(200,0)
    drawE(230,0)
    wn = turtle.Screen()
    input("Hit ENTER")
    turtle.bye()
	
# now call the main function to run the code

main()

