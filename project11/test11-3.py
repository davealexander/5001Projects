# Bruce Maxwell
# Spring 2013
# lab 10 test function 3
# draws a single tree

import tree
import turtle_interpreter as it
import shapes
import random
import sys

# draw a single tree
def main( argv ):

    if len(argv) < 2:
        print('usage: %s <l-system file> <opt: iterations>' % (argv[0]))
        exit()

    iterations = 4
    if len(argv) > 2:
        iterations = int(argv[2])

    x = it.TurtleInterpreter()

    ld = tree.Tree(distance=20,filename = argv[1])
    print(argv[1])

    #ld.setColor( (0.5, 0.4, 0.2) )
    #ld.setStyle( 'jitter' )
    ld.setLineWidth(3)
    ld.setIterations( iterations )
    ld.draw( 0, -200, scale=1.0, zpos=0)

    x.hold()

if __name__ == '__main__':
    main(sys.argv)
