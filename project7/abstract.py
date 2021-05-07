# David Centeno
# 5001 Intensive Foundations
# Spring 2021
# Version 1

#Creates an abstract drawing of 3 different l-systems in 3 different places. 

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

# main function, create some simple shapes
def abstract(distance, angle):
    #Stops the tracing of the Turtle Program
    t.tracer(False)

    #Turtle inital direction
    #Drawing 1
    lsysA = ls.createLsystemFromFile('lsystemA.txt')
    lstringA = ls.buildString (lsysA,3)

    #Goes to coordinates
    goto(-200,-200)
    
    #Sets the angle of the inital drawing
    t.left(20)
    #Sets the color to orange
    t.color('Orange')
    #Sets the pen width to 3 
    t.width( 3 )
    
    #Initiates the drawing of an Abstract LSystem
    ti.drawString(lstringA, distance, angle )

    #Drawing 2
    #rule F [F++][FF--F+F--]
    lsysB = ls.createLsystemFromFile('lsystemB.txt')
    lstringB = ls.buildString (lsysB,3)

    #Sets the pen down at designated coordinates
    goto(150,-200)

    #Sets the angle of the inital direction
    t.right(140)
    #Sets the color of the pen
    t.color('red')
    #Sets the width of the pen
    t.width( 1 )

    #Calls the function to create the drawing of lsystemB.txt
    ti.drawString( lstringB, distance, angle)

    #Drawing 3
    #rule F [F++][FF--F+F--]
    lsysC = ls.createLsystemFromFile('lsystemC.txt')
    lstringC = ls.buildString (lsysC,3)

    #Sets the pen down at designated coordinates
    goto(200,-200)

    #Sets the angle of the inital direction
    t.right(80)
    #Sets the color of the pen
    t.color('Blue')
    #Sets the width of the pen
    t.width( 2 )
    #Calls the function to create the drawing of lsystemC.txt
    ti.drawString( lstringC, distance, angle)

    #Holds the drawing open.
    ti.hold()
    
    #Returns the values of the function
    return

def main(argv):
    #Error statement that catches any argument put in the command line that is less than 3 
    if len(argv)< 3 :
        print("Error: Pleas input the correct commands")
        exit()
    
    #Assigns the second position of the argv list to distance and sets the distance for the abstract L-Systems
    distance = float( argv[1] )
    #Assings the third postion of the argv list to angle and sets hte angle for the abstract L-Systems
    angle = float(argv[2])

    #Calls the abstract function
    abstract(distance, angle)

    

if __name__ == "__main__":
    main(sys.argv)


