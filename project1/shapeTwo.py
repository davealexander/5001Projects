# David Centeno
# 1/22/20221
# CS5001/5003 Intensive Foundations Recitation
# Make a Scene Project File 2 of 3
# Program makes a pyramid that will change size when the scale variable is changed

# import the turtle library to use to create drawings
from turtle import *

#variable that is being used as a multiplier for the size of a shape/object
scale = 0.5

#Draw a pyramid
def pyramid():
    right(60)
    forward(75 * scale)
    left(60)
    backward(75 * scale)
    left(60)
    forward(75 * scale)
    right(100)
    forward(75 * scale)
    right(100)
    forward(30 * scale)

#Invokes the hexagon function 
pyramid()

#Keeps Turtle drawing open
mainloop()