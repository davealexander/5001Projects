#David Centeno
#5001 Intensive Foundations 
#Spring 2021
#motion.py file

import time
import random
import graphicsPlus as gr

def draw( shapes, win ):
    # for each thing in shapes
    for shape in shapes:
        # call the draw method on thing with win as the argument
        shape.draw( win )
def move( shapes, dx, dy ):
    # for each item in shapes
    for shape in shapes:
        shape.move(dx,dy)
        # call the move method on item with dx and dy as arguments
def undraw( shapes ):
    # for each thing in shapes
    for shape in shapes:
        shape.undraw( shape )
        # call the undraw method on thing


def init_saucer(x, y, scale):
    light = gr.Circle(gr.Point(x , y - 20 * scale), 4 * scale )
    light.setFill(gr.color_rgb(220,100,110))

    body = gr.Oval(gr.Point(x - 30 * scale, y - 20 * scale), gr.Point(x + 30 * scale, y + 20 * scale))
    body.setFill(gr.color_rgb(220,210,220))
    
    saucer = gr.Oval(gr.Point(x - 60 * scale, y - 5 * scale), gr.Point(x + 60 * scale, y + 5 * scale))
    saucer.setFill(gr.color_rgb(240,230,190))

    saucer = [light, body, saucer]

    return saucer

def animate_saucer( shapes, frame_num, win):

    if frame_num < 50:
        if frame_num % 20 == 0:
            shapes[0].setFill('blue')
    elif frame_num % 20 == 10:
        shapes[0].setFill('red')


# Test code for the flying saucer
def main():
    # make a window, add a 4th argument False, which halts automatic updating
    win = gr.GraphWin( "Saucer", 400, 400, False )
    
    # create the saucer shape list
    saucer = init_saucer(200, 200, 2)

    draw(saucer, win)
    
    # animate saucer
    for thing in range(100):
            animate_saucer(saucer, thing, win)
            win.update()
            time.sleep(0.1)
    # update the window (draw things) and wait for a mouse click
    win.update()
    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()