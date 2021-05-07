# David Centeno
# 5001 Intensive Foundations
# Spring 2021
import turtle as t
import lsystem as ls
import turtle_interpreter as ti
import sys
import random

def goto(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def trees(x,y,angle):
    t.setup(1000,1000)
    t.tracer(False)

    lsys = ls.createLsystemFromFile( 'systemB.txt' )
    # build the lsystem string with 3 iterations
    lstring = ls.buildString( lsys, 3 )

    t.left(90)
    t.color('purple')
    t.width( 2 )
    for i in range(3):
        for j in range(3):
            if j == 0:
                x+= 100
                angle = 22
            elif
            
            goto(x,y)
            ti.drawString(lstring, 5, angle)


    
    ti.hold()

    return

def main():

    trees(0,0,22)

if __name__ == "__main__":
    main()



