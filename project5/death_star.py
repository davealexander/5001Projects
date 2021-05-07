# David Centeno
# 5001 Intensive Foundations 
# Spring 2021

import graphicsPlus as gr
import time

def draw( shapes, win ):
    for shape in shapes:
        shape.draw( win)

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


def init_deathstar(x,y,scale):
    
    #Creates the body of the deathstar and colors it gray not jedi proof yet. Takes parameters x & y for positions and hardcode radius
    body = gr.Circle(gr.Point(x + 50 * scale, y + 50 * scale), 80 * scale)
    body.setFill('light gray')
    print(body.getCenter())

    #Creates the dish on the deathstar. This is the business end. Takes parameters x & y. Math ensures it stays in position. No rebels can break that part
    dish = gr.Oval(gr.Point(x  + 40 * scale, y + 40 * scale), gr.Point(x - 15 * scale, y - 15 * scale))
    dish.setFill('dark gray')

    #Creats dark gray panels on the death star. Helps hide Imperial Turrets. Takes parameters x & y. Math ensures it stays in position
    panel1 = gr.Rectangle(gr.Point(x - 5 * scale , y + 65 * scale), gr.Point(x + 20 * scale, y + 100 * scale))
    panel1.setFill('dark gray')
    
    panel2 = gr.Rectangle(gr.Point(x + 30 * scale , y + 65 * scale), gr.Point(x + 40 * scale, y + 100 * scale))
    panel2.setFill('dark gray')
    
    panel3 = gr.Rectangle(gr.Point(x + 50 * scale , y + 70 * scale), gr.Point(x + 70 * scale, y + 115 * scale))
    panel3.setFill('dark gray')
    
    panel4 = gr.Rectangle(gr.Point(x + 80 * scale , y + 70 * scale), gr.Point(x + 100 * scale, y + 110 * scale))
    panel4.setFill('dark gray')

    panel5 = gr.Rectangle(gr.Point(x + 90 * scale , y + 10 * scale), gr.Point(x + 115 * scale, y + 40 * scale))
    panel5.setFill('dark gray')

    #Creates a  wide line straight through the center of the deathstar shape. Takes parameters X + Y. Math/hardcode keeps the object in place
    #...rather unfortunate design flaw may want to get that looked at before rebels attack. 
    blockade = gr.Line(gr.Point(x - 30 * scale, y + 50 * scale), gr.Point(x + 130 * scale, y + 50 * scale))
    blockade.setFill('black')
    blockade.setWidth(5)

    
    

    #Assembles the deathstar in an object 
    deathstar = [body, dish, panel1, panel2,panel3, panel4, panel5, blockade]
    #returns the deathstar as an object used for the draw method
    return deathstar

def main():
    # make a window, add a 4th argument False, which halts automatic updating
    win = gr.GraphWin( "deathstar", 400, 400, False )
    
    deathstar = init_deathstar(200, 100, 1)

    draw(deathstar, win)

    win.update()
    win.getMouse()
    win.close()
if __name__ == "__main__":
    main()