#David Centeno
#5001 Intensive Foundations
#Spring 2021

#Creates 3 recursive shapes doughnut, double helix, and sphere

import shapes
import turtle_interpreter
import random

#recursive function that makes a spiral with the triangle shape
def spiral(tri,x,y,s,o,r,iteration):
    #base case
    if iteration < 1: 
        return 
    #initializes the shape with random colors and draws the shape
    tri.__init__(1)
    tri.setColor((random.uniform(0.5,0.9),random.uniform(0.5,0.9),random.uniform(0.8,0.9)))
    tri.draw(x,y,s,o,r)
    
    #recursive statement with parameters that lays shape flat
    spiral(tri ,x ,y + 5, s, o + 5, r, iteration *.9)


def doughnut(dough,x,y,s,o,r,iteration):
    if iteration < 1: 
        return 
    #initializes the shape with random colors and draws the shape
    dough.__init__(60)
    dough.setColor((random.uniform(0.5,0.9),random.uniform(0.5,0.9),random.uniform(0.8,0.9)))
    dough.draw(x,y,s,o,r)
    
    #recursive statement with parameters that rolls the shape in the z axis
    doughnut(dough,x ,y, s, o, r + 5, iteration *.93)

def main():
    #Brings in turtle interpreter
    ti = turtle_interpreter.TurtleInterpreter()
    #Brings in the the triangle shape
    tr = shapes.Triangle()
    #Bring in the circle shape
    cir =shapes.Circle()
    
    #Calls the recursive function spiral which makes a double helix
    spiral(tr,0,0,60,1,90,300)
    #spiral(tr,0,0,60,1,-90,300)

    #Calls doughnut recursive shape and draws a doughnut like shape <-- May slow down computer on call! -->
    doughnut(cir,200,0,1,0,1,300)
    
    #Calls the doughnut recursive shape and creates a sphere <-- May slow down computer on call! -->
    #doughnut(cir,-200,0,1,90,1,300)
    
    ti.hold()

if __name__ == "__main__":
    main()