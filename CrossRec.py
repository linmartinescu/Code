"""
    Aurthor: Lindsay Martinescu
"""

import turtle
def crossRec(n,s):
    turtle.forward(s)
    if n >1:
        turtle.left(90)
        crossRec(n-1,s/2)
        turtle.back(s/2)
        turtle.right(180)
        crossRec(n-1,s/2)
        turtle.back(s/2)
        turtle.left(90)
        crossRec(n-1,s/2)
        turtle.back(s/2)
        
crossRec(6,100)
