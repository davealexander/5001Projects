# David Centeno
# 1/22/20221
# CS5001/5003 Intensive Foundations Recitation
# Make a Scene Project File 3 of 3
# File will create a scene with 3 basic shapes using the scene function. Test function shows three shapes independently as well as 1 complex shape

# import the turtle library to use to create drawings
from turtle import *

# Function that tests shapes created and resets to angle 0 and position 0,0 when completed
def test(length, scale):
    speed(0)
    triangle(length)
    penup()
    backward(100)
    pendown()
    square(length)
    penup()
    backward(100)
    pendown()
    hexagon(length)
    penup()
    setposition(0,0)
    setheading(0)
    pendown()
    cShape(length * scale)
    penup()
    setposition(0,0)
    setheading(0)
    pendown()

#Creates a Scene using all shapes and complex shape
def scene(length, scale):
    speed(0)
    forward(100)
    cShape(length * scale)
    setposition(0,0)
    backward(100)
    cShape(length * scale)
    setposition(0,0)
    right(90)
    forward(150)
    cShape(length * scale)
    setposition(0,0)
    left(180)
    forward(150)
    cShape(length * scale)

# Complex shape using the three existing shape
# extension: for loop to reduce code length
def cShape(length): #Complex shape using the below three shapes
    square(length)
    triangle(length)
    for i in range (6): 
        hexagon(length)
        triangle(length)
        square(length)

# Draws an equilateral triangle 
# extension: Included for loop to reduce repeated code
def triangle(length):   #length argument determines how long the legs of the triangle is
    color("orange")
    for i in range (3):
        left(120)
        forward(length)

# Draws a square
# extension: Included for loop to reduce repeated code
def square(length):     #length argument determines the size of the square
    color("blue")
    for i in range (4):
        right(90)
        forward(length)

#Draws a hexagon
# extension: Included for loop to reduce repeated code
def hexagon(length):  #length argument determines the size of the hexagon
    color("purple")
    for i in range (5):
        forward(length)
        left(60)
    forward(length)

###### Extension 2 person #####

# Defines the shape of a person using the functions below
def person():
    speed(0)
    face()
    penup()
    setposition(-50,-170)
    pendown()
    seth(0)
    shirt()
    pants()    

# Defines the shape of a shirt 
def shirt():
    forward(100)
    left(90)
    forward(100)
    right(120)
    forward(50)
    left(100)
    forward(50)
    left(80)
    forward(100)
    left(30)
    forward(60)
    left(30)
    forward(100)
    left(90)
    forward(50)
    left(80)
    forward(50)
    right(110)
    forward(100)

#Definies the shape of pants
def pants():
    right(20)
    forward(150)
    left(110)
    forward(75)
    left(70)
    forward(100)
    right(140)
    forward(100)
    left(70)
    forward(75)
    left(115)
    forward(170)

#Defines a face
def face():
    circle(100)
    penup()
    setposition(60,100)
    pendown()
    circle(25)
    penup()
    setposition(-60,100)
    pendown()
    circle(25)
    penup()
    setposition(-60,70)
    pendown()
    right(90)
    for x in range(180): #credit to stack overflowpost https://stackoverflow.com/questions/29441237/how-to-draw-a-semicircle-in-python-turtle-only
        forward(1)
        left(1)

######

#Comment all functuions but one to see shapes
#Calls the function test
#test(60, 0.5)
#Calls the function test with 1.5x scale
#test(100, 1.5)
#Calls the scene function at 0.5x scale
#scene(100,0.5)
#Calls the person function with no arguments
person()

########

#keeps turtle drawing pad open
mainloop()