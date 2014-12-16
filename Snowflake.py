"""
    Author:Lindsay Martinescu
"""

import turtle
import math

def intialize():
    turtle.setup(800,700)
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Snowflake")
    turtle.speed(0)
    turtle.colormode(255)

def drawCircle(color,r):
    turtle.color(color,color)
    turtle.begin_fill()
    turtle.circle(r,120)
    turtle.circle(r,120)
    turtle.circle(r,120)
    turtle.end_fill()

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
    
def circlesRec(r,depth,skip=False):
    color = pickColour(r)
    if (depth==0):
        pass
    elif (depth== 1):
        turtle.color(color,color)
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()
    elif(1< depth <5):
        drawCircle(color,r)
        turtle.color(color,color)
        turtle.begin_fill()
        turtle.circle(r,120)
        turtle.left(180)
        circlesRec(r/((1+math.sqrt(5))/2),depth-1,skip)
        turtle.right(180)
        turtle.circle(r,120)
        turtle.right(180)
        circlesRec(r/((1+math.sqrt(5))/2),depth-1,skip)
        turtle.left(180)
        turtle.circle(r,120)
        turtle.end_fill()
    else:
        drawCircle(color,r)
        turtle.color(color,color)
        turtle.begin_fill()
        turtle.circle(r,120)
        turtle.left(180)
        circlesRec(r/((1+math.sqrt(5))/2),depth-1,True)
        turtle.right(180)
        turtle.circle(r,120)
        turtle.right(180)
        circlesRec(r/((1+math.sqrt(5))/2),depth-1,True)
        turtle.left(180)
        turtle.circle(r,120)
        if not skip:
          turtle.right(180)
          circlesRec(r/((1+math.sqrt(5))/2),depth-1,True)
          turtle.left(180)
        turtle.end_fill()
    
def main():
    intialize()
    r = int(input("Size of Radius"))
    depth = int(input("Depth"))
    circlesRec(r,depth)

main()
