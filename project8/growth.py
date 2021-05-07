#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 2.0 ##

#Growth will draw a small sprig of a tree which eventually grows to a digital looking enso Tree
#Enso tree reference https://i.pinimg.com/originals/4d/79/d1/4d79d1c4b6f1eaf267555c158253f6d8.jpg

import sys
import turtle_interpreter
import lsystem

#draws an enso tree starting with iterations at 2. scene function is self contained and will run without sys arguments
def scene():
    ti = turtle_interpreter.TurtleInterpreter()
    #calls the Lsystem file with the arugment of arrangement1.txt
    lsys = lsystem.Lsystem('growth.txt')
    #Decides how many times the build string will repeat
    #Start iterations at 3. Enso tree is full at iterations 5 
    iterations = 5
    #Decides the distance of how far the turle will move
    distance = 20
    #Sets the angle of the turtle
    angle = 23
    #Sets the starting X position of the drawing
    x1 = 100
    #Sets the starting Y position of the drawing
    y1 = 0

    #builds the string for interpetation
    tstr= lsys.buildString(iterations)
    #sets the width of the line
    ti.setWidth(1)
    #sets the starting position of first plant
    ti.place(x1,y1,90)
    #draws the tree from the lsystem
    ti.drawString(tstr,distance,angle)


def main():
    #builds out 800x800 turtle canvas
    ti = turtle_interpreter.TurtleInterpreter()
    #initiates scene function
    scene()
    #holds the canvas open until window is clicked or the q button is pressed
    ti.hold()

if __name__ == "__main__":
    main()


