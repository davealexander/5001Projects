#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 2.0 ##

import sys
import turtle as t
import random

class TurtleInterpreter:
    def __init__(self, dx = 800 , dy = 800):
        t.setup(dx,dy)
        t.tracer(False)
    
    def drawString(self, dstring, distance, angle):
        """ The distance specifies how far the turtle should move forward for the F character, 
        and the angle specifies the number of degrees the turtle should turn for a + or - character."""
    
        # Character	Action
        # F	Move the turtle forward by distance
        # +	Turn the turtle left by angle
        # -	Turn the turtle right by angle
        # [	Append the turtle's heading and position to a list (e.g. stack)
        # ]	Pop the turtle's heading and position from the list (e.g. stack) and restore the turtle's state

        #Stack to store the L-System Instructions
        stack = []
        colorStack = []
        r = t.color(0.60, 0.35, 0.25)
        y = t.color(0.8, 0.8, 0.3)
        g = t.color(0.15, 0.5, 0.3)

        for c in dstring:
            if c == 'F':
                t.forward(distance)
            elif c == '-':
                t.right(angle)
            elif c == '+':
                t.left(angle)
            elif c == '[':
                stack.append(t.pos())
                stack.append(t.heading())
            elif c == ']':
                t.penup()
                t.setheading(stack.pop())
                t.goto(stack.pop())
                t.pendown()
            elif c =='<':
                colorStack.append( t.color()[0] )
            elif c =='>':
                colorStack.pop( t.color()[0] )

        t.update()
    
    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        t.hideturtle()
        t.update()

        # Close the window when users presses the 'q' key
        t.onkey(t.bye, 'q')

        # Listen for the q button press event
        t.listen()

        # Have the turtle listen for a click
        t.exitonclick()
    
    def place(self, xpos, ypos, angle=None):
        t.penup()
        t.goto(xpos,ypos)
        t.setheading(angle)
        t.pendown()
    
    def orient(self, angle):
        t.setheading(angle)
    
    def goto(self, xpos, ypos):
        t.penup()
        t.goto(xpos,ypos)
        t.pendown()
    
    def setColor(self, c):
        t.color(c)
    
    def setWidth(self, w):
        t.width(w)
    
