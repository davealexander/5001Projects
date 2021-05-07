#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 2.0 ##

# Draws a scene of 3 large treess with small tree like bushes at the foot of the larger trees
import sys
import turtle_interpreter
import lsystem

def plant1():
    ti = turtle_interpreter.TurtleInterpreter()
    #calls the Lsystem file with the arugment of arrangement1.txt
    lsys = lsystem.Lsystem('arrangement1.txt')
    #Decides how many times the build string will repeat
    iterations = 5
    #Decides the distance of how far the turle will move
    distance = 5
    #Sets the angle of the turtle
    angle = 22
    #Sets the starting X position of the drawing
    x1 = -100
    #Sets the starting Y position of the drawing
    y1 = -100

    #builds the string for interpetation
    tstr= lsys.buildString(iterations)
    #sets the width of the line
    ti.setWidth(1)
    #sets the starting position of first plant
    ti.place(x1,y1,90)
    for i in range(3):
        ti.place(x1,y1,90)
        ti.drawString(tstr,distance,angle)
        x1+=120

def plant2():
    ti = turtle_interpreter.TurtleInterpreter()
    #calls the Lsystem file with the arugment of arrangement2.txt
    lsys = lsystem.Lsystem('arrangement2.txt')
    #Decides how many times the build string will repeat
    iterations = 7
    #Decides the distance of how far the turle will move
    distance = .3
    #Sets the angle of the turtle
    angle = 40
    #Sets the starting X position of the drawing
    x1 = -100
    #Sets the starting Y position of the drawing
    y1 = -100

    #builds the string for interpetation
    tstr= lsys.buildString(iterations)
    #sets the width of the line
    ti.setWidth(2)
    #sets the starting position of first plant
    ti.place(x1,y1,90)
    for i in range(6):
        ti.place(x1,y1,90)
        ti.drawString(tstr,distance,angle)
        x1+=60

def main():
    ti = turtle_interpreter.TurtleInterpreter()
    #Calls the function of plant1
    plant1()
    #Calls the function of plant2 
    plant2()


    ti.hold()

if __name__ == "__main__":
    main()


