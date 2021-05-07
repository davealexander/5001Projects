#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 4.0 ##

# A demo file that shows the different types of line styles that can be used. 

import turtle_interpreter
import shapes

def main():
    #Brings in the turtle interperter class
    ti = turtle_interpreter.TurtleInterpreter()

    #Creates a Square
    sq = shapes.Square()
    #Sets the coordinates and linewidth variables for sqaure drawing
    x0= 0
    y0= 100
    lw= 1
    #loop that will draw two sqaures with different widths
    for i in range(2):
        sq.setLineWidth(lw)
        sq.setColor((0.5,0.5,0.5))
        sq.draw(x0, y0, scale=1, orientation=90)
        x0+= 100
        lw+=5
    #Resotres X and line width
    x0=0
    lw=1

    #<--Creates Jittered Cross1-->
    cr = shapes.Cross()
    #Sets the size of the cross
    cr.__init__(distance=25)
    #Sets the line width of the cross
    cr.setLineWidth(5)
    #Sets the style of the cross
    cr.setStyle('jitter')
    #Sets the jitter of the cross
    cr.setJitter(2)
    #Draws the cross shape
    cr.draw(100,100,scale=1,orientation=0)
    
    #<--Creates Jittered cross2-->
    #Sets the size of the cross
    cr.__init__(distance=25)
    #Sets the lind width of the cross
    cr.setLineWidth(2)
    #sets the style of the cross
    cr.setStyle('jitter3')
    #sets the jitter of the cross
    cr.setJitter(5)
    #Draws the second cross
    cr.draw(-200,100,scale=1,orientation=90)

    #<--Creates a hexagon shape -->
    hx = shapes.Hexagon()
    #Sets the size of the hexagon
    hx.__init__(50)
    #sets the jitter of the hexagon
    hx.setJitter(2)
    #sets the line width of the hexagon
    hx.setLineWidth(1)
    #sets the style of the hexagon
    hx.setStyle('dotted')
    #sets the dot size of the hexagon
    hx.setdotSize(2)
    #draws the hexagon shape
    hx.draw(-100,-200,scale=1,orientation=0)

    #<-- Creates the triangle shape -->
    tr = shapes.Triangle()
    #sets the size of the triangle
    tr.__init__(150)
    #sets the jitter of the triangle
    tr.setJitter(5)
    #sets the line width of the triangle
    tr.setLineWidth(1)
    #sets the style triangle
    tr.setStyle('dotted')
    #sets the dot size of the triangle
    tr.setdotSize(10)
    #draws the triangle
    tr.draw(200,-200,scale=1,orientation=0)
    
    #holds the turtle canvas open
    ti.hold()

if __name__ == "__main__":
    main()



