# Bruce Maxwell
# Spring 2010
# Revised Spring 2013
# Revised Fall 2017 for Python 3
# test function 1 for lab 10

import turtle_interpreter
import random

def main():
    """ draw two normal shapes and two jittered versions
        a test of the jitter drawing method
    """
    
    # define two strings
    square = 'F-F-F-F-'
    triangle = 'F-F-F-'

    terp = turtle_interpreter.TurtleInterpreter()

    # draw normal and jittered versions of each shape
    terp.place(-200, -100)
    terp.setStyle( 'normal' )
    terp.setColor("blue")
    terp.drawString(square, 100, 90)

    terp.place(-200, 100)
    terp.setStyle( 'jitter3' )
    terp.setColor('red')
    terp.drawString(square, 150, 90)

    terp.place(100, -100)
    terp.setStyle( 'normal' )
    terp.setColor("green")
    terp.drawString(triangle, 100, 120)
    
    terp.place(100, 100)
    terp.setStyle( 'jitter' )
    terp.setColor("purple")
    terp.drawString(triangle, 100, 120)

    terp.hold()

if __name__ == "__main__":
    main()

