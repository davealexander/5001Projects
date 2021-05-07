#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 3.0 ##

# A turtle interperter that has been updated to make use of classes. Assigns certain characters to turtle functions
import sys
import turtle as t
import random

class TurtleInterpreter:
    initialized = False

    def __init__(self, dx = 800 , dy = 800):
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
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

        for c in dstring:
            #symbol sets F to move turtle forward
            if c == 'F':
                t.forward(distance)
            elif c == 'L':
                t.color(colorStack[0])
                t.begin_fill()
                t.circle(2)
                t.end_fill()
            #symbol sets - to change turtle direction to the right by a certain angle
            elif c == '-':
                t.right(angle)
            #symbol sets + to change turtle direction to the right by a certain angle
            elif c == '+':
                t.left(angle)
            #Appends the turtle postion and heading to the stack list
            elif c == '[':
                stack.append(t.pos())
                stack.append(t.heading())
            #sets the heading and position from popping values from the stack list
            elif c == ']':
                t.penup()
                t.setheading(stack.pop())
                t.goto(stack.pop())
                t.pendown()
            #Appends t.color to the colorstack at the 0 position
            elif c =='<':
                colorStack.append( t.color()[0] )
            #Sets the color 
            elif c =='>':
                currentColor = colorStack.pop(0)
                t.color(currentColor)
            #Sets r to the color red
            elif c == 'r':
                t.color((0.7, 0.4, 0.5))
            #Sets y tp the color yellow
            elif c == 'y':
                t.color((0.8, 0.8, 0.3))
            #Sets g to the color green
            elif c == 'g':
                t.color((0.1, 0.5, 0.2))
           #sets b to the color blue
            elif c == 'b':
                t.color((0.1, 0.5, 0.8))
            #sets p to the color light pink
            elif c == 'p':
                t.color((0.9,0.6,0.6))
            #sets 0 to a specific position used for project 8
            elif c == '0':
                self.place(-120,150,270)
            #sets the width of the branch of a tree
            elif c == 'w':
                t.width(4)
            #Starts the begin fill for coloring an object
            elif c == '{':
                t.begin_fill()
            #Ends the fill ofr coloring an object
            elif c == '}':
                t.end_fill()
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
    
