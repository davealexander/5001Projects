# David Centeno
# 5001 Intensive Foundations
# Spring 2021
# Version 1 

#Scene file will make a drawing with 2 lystems with an outcome of a plant in a vase
import turtle as t
import lsystem as ls
import turtle_interpreter as ti
import sys


#Creates the go to method. Allows to draw at a certain position
def goto(x,y):
    #Picks the turtle pen up
    t.up()
    #Sets the turtle pen to the set coordinates
    t.goto(x,y)
    #Puts the pen down to enable drawing.
    t.down()

#Draws a plant with an L-system
def plant(x,y,scale):
    #Drawing 1

    #Opens and reads from the L-System text file and repeats the the line 3 times
    lsysPlant = ls.createLsystemFromFile('scenePlant.txt')
    lstrPlant = ls.buildString (lsysPlant,3)

    #Starts the drawing to head left by 90 degrees
    t.left(90)
    #Sets the pen color green
    t.color('green')
    #Sets the width to 2
    t.width( 2 )
    
    #Draws the plant from the L-System File
    for i in range(5):
     #Starts the drawing at -200 X and -200 Y
        goto(x,y)
        ti.drawString(lstrPlant,scale *10, 22.7 )
        x+= scale * 40
        y+= 0

    #Returns the value of plant
    t.setheading(0)
    return

def vase(x,y,scale):
    #Opens the sceneVase.txt file
    lsysVase = ls.createLsystemFromFile('sceneVase.txt')
    #Reads from the above file and repeats the L-System once
    lstrVase = ls.buildString (lsysVase,1)

    #Draws at X & Y coordinates
    goto(x,y)

    #Starts the drawing at a 90 degree angle
    t.left(90)
    #Fills the vase with a gray color
    t.color('gray')
    #Sets the width of the pen to two
    t.width( 2 )
    #Begins the fill process
    t.begin_fill()
    #Calls the L-System and draws using the interperter. Drawing will also scale
    ti.drawString(lstrVase, scale*50, 30 )
    #Ends the fill process
    t.end_fill()
    #Sets the heading to 0 in the case if anything else is called after this function
    t.setheading(0)
    #returns thee value of vase
    return

def main(scale):
    
    #System argument for scale
    scale = int(sys.argv[1])

    #Sets the tracer as false
    t.tracer(False)
    #Sets up the drawing canvas
    t.setup(700, 700)
    #Calls the plant L-system
    plant(-50,-50,scale)
    #Calls the vase L-System
    vase(-50,-100,scale)
    #Holds the canvas open until a button click or the q button is clicked
    ti.hold()
if __name__ == "__main__":
    main(sys.argv)
