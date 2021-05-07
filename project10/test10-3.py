# Bruce Maxwell
# Spring 2010
# revised spring 2013
# revised fall 2017 for Python 3
# test function 3 for lab 10

import turtle_interpreter
import random

def main():
    """ draws a bunch of trapezoids; tests the interpreter's ability to handle parameters
    """

    terp = turtle_interpreter.TurtleInterpreter()

    # defines a trapezoid using a parameterized string
    trap = 'FF(120)+F(60)+F(60)+F(120)+'

    # draw a bunch of them
    for i in range(20):
        terp.place( random.randint(-300, 100), random.randint(-300, 200) )
        terp.setColor( (random.random(), random.random(), random.random() ) )
        terp.drawString( trap, random.randint(20, 100), 90 )

    terp.hold()


if __name__ == "__main__":
    main()
