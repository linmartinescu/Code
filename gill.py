import turtle
import random
 
def Poly(n,x):
    angle = 360/n
    for i in range(n):
        turtle.forward(x)
        turtle.left(angle)
 
def makeFlower(p):
    for i in range(12):
        Poly(9,p)
        turtle.left(30)
 
def makeTriple():
    turtle.speed(44)
    for i in range(3):
        i = (i+1)*5
        turtle.color(random.random(),random.random(),random.random())
        makeFlower(i)
 
xa = -255  
y = -244
numberColumns = 5
numberRows = 5
turtle.penup()
turtle.setpos(xa,y)
 
for i in range(numberRows):
    for c in range(numberColumns):
        c=(c+1)*100
        makeTriple()
        turtle.penup()
        turtle.sety(y+c)
        turtle.pendown()
    i=(i+1)*100
    turtle.penup()
    turtle.setpos(xa+i,y)
    turtle.pendown()
