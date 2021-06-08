import turtle

from random import *

from turtle import *

penup()

goto (-140,140) 

for sp in range(15): 

    speed(10)
    write(sp)
    right (90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left (90)
    forward(20) 

ayush = Turtle() 
ayush.color('green')
ayush.shape('turtle') 
ayush.penup()
ayush.goto(-160,100) 
ayush.pendown()

vijay = Turtle() 
vijay.color('red') 
vijay.shape('turtle') 
vijay.penup()
vijay.goto(-160,80)
vijay.pendown()

gaurav = Turtle() 
gaurav.color('blue') 
gaurav.shape('turtle') 
gaurav.penup() 
gaurav.goto(-160,60)
gaurav.pendown()

for turn in range(100):
     ayush. forward (randint(1,5))
     vijay. forward (randint (1,5)) 
     gaurav.forward(randint(1,5))

turtle.done()