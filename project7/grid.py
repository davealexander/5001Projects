# David Centeno
# 5001 Intensive Foundations
# Spring 2021
# Veriosn 1

#File that creates a 3x3 grid of trees unfurling

import turtle as t
import lsystem as ls
import turtle_interpreter as ti
import sys
import random

#Creates the go to method. Allows to draw at a certain position
def goto(x,y):
    #Picks the turtle pen up
    t.up()
    #Sets the turtle pen to the set coordinates
    t.goto(x,y)
    #Puts the pen down to enable drawing.
    t.down()

#Creates a 3x3 grid of trees using systemB.txt L-system
def trees(x,y,angle,scale):
    #Creates a canvas of 1000x1000 pixels
    t.setup(1000,1000)
    #Sets the tracer to false to draw instantly
    t.tracer(False)

    #opens the systemB text file
    lsys = ls.createLsystemFromFile( 'systemB.txt' )
    # build the lsystem string with 3 iterations
    lstring = ls.buildString( lsys, 3 )

    #Sets the initial direction at a right angle
    t.left(90)
    #makes the color of the drawing purple
    t.color('purple')
    #makes the width of the pen thin or wide
    t.width( 1 )

    #For loop that creates the 3x3 grid.
    for i in range(3):
        if i == 0:
            angle = 60
        elif i == 1:
            angle = 46
        elif i == 2:
            angle = 22
        # Creates the columns of trees
        for j in range(3):
            goto(x,y)
            ti.drawString(lstring, 5 *scale, angle)
            x+= 50
        #Takes X and resets to the original X position
        x = x-150 * scale
        #Sets up the rows of the trees
        y+=100*scale
    
    #Holds the canvas open. Will close on mouse click or close by pressing Q 
    ti.hold()

    return

def main():
    #calls the tree L-system function
    trees(-150,0,60,1)

if __name__ == "__main__":
    main()



