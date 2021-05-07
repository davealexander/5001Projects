# Bruce Maxwell
# Spring 2013
# test function 2 for lab 10

import turtle_interpreter as it
import shapes

# draws four squares at different orientations and locations
def main():

    x = it.TurtleInterpreter()

    s = shapes.Square( distance=300, color=(0.1, 0.6, 0.3) )
    s.draw( -150, -150, zpos=-150, roll=-90)
    

    s.setColor( (0.2, 0.1, 0.7)  )
    s.draw( -150, -150, zpos=-150, orientation=90 )

    s.setColor( (0.8, 0.2, 0.3) )
    s.setStyle( 'jitter' )
    s.draw( -150, 0, zpos=-150, roll=-90)

    s.setColor( (0.7, 0.7, 0.1) )
    s.setStyle( 'jitter' )
    s.draw( -150, 150, zpos=-150, roll=-90)

    x.hold()

if __name__ == '__main__':
    main()
