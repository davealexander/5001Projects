# Bruce Maxwell
# Revised for spring 2013
# Tested for Python 3 fall 2017
# test function 2 for lab 9

import turtle_interpreter
import shapes

# a simple test function that draws squares and triangles
def main():

    # create a square object and draw a bunch of them
    # s = shapes.Square()
    # s.setColor( (0.3, 0.2, 0.9) )
    # for i in range(36):
    #     s.draw(0, -100, scale=0.75, orientation=i*10)

    # # create a triangle object and draw a bunch of them
    # t = shapes.Triangle()
    # t.setColor( (0.8, 0.2, 0.3) )
    # for i in range(20):
    #     t.draw(0, 100, scale=0.8, orientation=i*18)
    
    # h = shapes.Hexagon()
    # h.setColor((0.7,0.6, 0.4))
    # h.draw(-100,100,scale=1.0,orientation=90)

    cr= shapes.Cross()
    cr.setColor((0.9,0.2, 0.2))
    cr.draw(-100,-100,scale=1.0,orientation=90)

    # # draw some more squares
    # scale = 0.8
    # offset = 0
    # s.setColor( (0.1, 0.8, 0.2) )
    # for i in range(20):
    #     s.draw(-300, -190 + offset, scale=scale, orientation=90)
    #     offset += scale * 100
    #     scale *= 0.8

    # # draw some more triangles
    # scale = 0.8
    # offset = 0
    # t.setColor( (0.1, 0.8, 0.2) )
    # for i in range(20):
    #     t.draw(300, -190 + offset, scale=scale, orientation=180)
    #     offset += scale * 87
    #     scale *= 0.83   
 

    # wait
    turtle_interpreter.TurtleInterpreter().hold()


if __name__ == '__main__':
    main()

