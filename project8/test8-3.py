# Bruce Maxwell
# spring 2013
# lsystem and turtle interpreter class test function

import sys
import random
import turtle_interpreter
import lsystem

def main(argv):
    """ Draw a single tree, using an Lsystem and the TurtleInterpeter
    This progarm expects the name of an L-system file, the number of iterations
    to use to generate the tree string, the distance associated with F, and
    the angle.
    """

    if len(argv) < 5:
        print( 'usage: %s <lsystem file 1> <iterations> <distance> <angle>' % (argv[0]) )
        exit()

    tree = lsystem.Lsystem( argv[1] )
    iterations = int( argv[2] )
    distance = float( argv[3] )
    angle = float( argv[4] )

    sx = 600
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    x0 = 0
    y0 = -250

    tstr = tree.buildString( iterations )

    terp.setWidth( 2 )
    terp.setColor( (0.5, 0.4, 0.3 ) )
    terp.place( x0, y0, 90 )
    terp.drawString( tstr, distance, angle )


    terp.hold()


if __name__ == "__main__":
    main( sys.argv )
