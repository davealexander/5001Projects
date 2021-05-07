# Bruce Maxwell
# Spring 2010
# Revised spring 2013
# Revised fall 2017 for Python 3
# second test function for lab 10

import turtle_interpreter
import shapes

def main():
    """ test function for the new jitter style
        creates a 3x3 array with jitter increasing right to left
    """

    # create a Square and a Triangle object
    s = shapes.Square()
    s.setStyle( 'jitter' )

    t = shapes.Triangle()
    t.setStyle( 'jitter' )

    g = 0.2

    # Put them together in a 3x3 grid
    for i in range(3):
        r = 0.2 + 0.3*i
        for j in [0, 1, 2]:
            b = 0.8 - 0.3*i
            t.setColor( (b, g, r) )
            t.setJitter(j*3)
            t.draw( -180 + 150*j, 180 - 150*i, scale = 0.4, orientation = 0 )

            s.setColor( (r, g, b) )
            s.setJitter(j*3)
            s.draw( -200 + 150*j, 200 - 150*i, scale = 0.8, orientation = 0 )


    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main()
