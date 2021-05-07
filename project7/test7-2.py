# Bruce Maxwell
# Fall 2020
# CS 5001 Project 7
# First L-system project
# Some test code

import turtle
import turtle_interpreter as ti

# useful goto function
def goto(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

# main function that makes a small tree in a pot
def makeTree():

    # set up the window and turn off tracing
    turtle.setup(500, 500)
    turtle.tracer(False)

    # draw a small symmetric tree
    turtle.setheading(90)
    goto(0,0)
    s = 'F[+F[+F][-F]][-F[+F][-F]]'
    turtle.width(3)
    ti.drawString( s, 50, 30 )
    turtle.width(1)

    # draw the pot and legs
    turtle.setheading(0)
    goto(-50, -100)
    turtle.color('brown')
    turtle.begin_fill()
    ti.drawString( 'F+'*4, 100, 90 )
    turtle.end_fill()
    
    goto(-50, -100)
    turtle.color('dark red')
    turtle.begin_fill()
    ti.drawString( 'F'*10+'+F+'+'F'*10+'+F+', 10, 90 )
    turtle.end_fill()

    goto(-60, -120)
    turtle.begin_fill()
    ti.drawString( 'F+'+'F'*12+'+F+'+'F'*12+'+', 10, 90 )
    turtle.end_fill()

    goto(50, -120)
    turtle.begin_fill()
    ti.drawString( 'F+'+'F'*12+'+F+'+'F'*12+'+', 10, 90 )
    turtle.end_fill()

    # update and hold
    ti.hold()

    return
    

if __name__ == "__main__":
    makeTree()
    
