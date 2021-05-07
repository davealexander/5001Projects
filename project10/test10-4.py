# Bruce Maxwell
# CS 151
# Fall 2010
# Revised Spring 2013
# Revised Fall 2017 for Python 3
# Test function for parameterized L-systems and the parameterized interpreter
# 

import shapes
import lsystem
import turtle_interpreter
import sys

class Tree(shapes.Shape):
    """ Tree class, derived from Shape, contains an Lsystem """

    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        """new init parameters are angle, iterations, filename"""
        shapes.Shape.__init__(self, distance, angle, color)

        self.iterations = iterations
        self.lsystem = lsystem.Lsystem(filename)

    def read(self, filename):
        """ read the lsystem from the file """
        self.lsystem.read(filename)

    def setIterations(self, iter):
        """ mutator function """
        self.iterations = iter

    def draw(self, xpos, ypos, scale=1.0, orientation=90 ):
        """ build the string using the L-system, then draw it
            this gives you a different tree, potentially, each time """
        # create the string
        self.setString(self.lsystem.buildString( self.iterations ))
        
        # call the parent draw function
        shapes.Shape.draw(self, xpos, ypos, scale, orientation )

def main(argv):
    """ main function that draws 3 L-systems """

    if len(argv) < 4:
        print('Usage: tree.py <filename> <iterations> <distance> <angle>')
        exit()

    # create a tree object
    t1 = Tree( filename=argv[1], iterations=int(argv[2]), distance=float(argv[3]), angle=float(argv[4]) )

    # draw three of them in jitter style
    t1.setStyle( 'jitter' )
    t1.draw( 0, -200 )
    t1.draw( -150, -250, scale=0.7 )
    t1.draw( 150, -250, scale=0.4 )
    
    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == "__main__":
    main(sys.argv)
