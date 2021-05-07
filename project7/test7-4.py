# Bruce Maxwell
# Fall 2020
# CS 5001
# test program for lsystem and interpreter
#

import turtle
import sys
import lsystem as ls
import turtle_interpreter as it

# draws two l-system strings given an (x,y) anchor, scale and angle
def pair( lstr, x, y, scale, angle ):
    oldheading = turtle.heading()

    turtle.up()
    turtle.goto(x, y )
    turtle.down()
    turtle.right(270)
    turtle.color( 0.5, 0.6, 0.8 )
    turtle.width( 2 )
    it.drawString( lstr, scale*0.75, angle )

    turtle.up()
    turtle.goto( x, y )
    turtle.down()

    turtle.color( 0.1, 0.2, 0.4 )
    turtle.width( 1 )
    turtle.left(135)
    it.drawString( lstr, scale*0.4, angle )


    turtle.setheading( oldheading )

    return


# takes in the list of strings from the command line
# reads in an lsystem file, generates the string and
# draws two copies of a pair of shapes
def main(argv):

    # check if there are enough arguments
    if len(argv) < 4:
        print('usage: %s <lsystem filename> <distance> <angle>' % (argv[0]))
        exit()

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile( argv[1] )

    # build the lsystem string with 3 iterations
    lstr = ls.buildString( lsys, 3 )

    dist = float( argv[2] )
    angle = float( argv[3] )

    # draw the two pairs
    turtle.tracer(False)
    pair( lstr, -100, 100, dist, angle )
    pair( lstr, 100, -100, dist*0.5, angle )
    
    # wait
    it.hold()


if __name__ == "__main__":
    main( sys.argv )


    
