# David Centeno
# 5001 Intensive Foundations
# Spring 2021

#imports the turtle commands
import turtle as t
#imports system arguments
import sys


def drawString(dstring, distance, angle):
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
    t.update()

def hold():
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







