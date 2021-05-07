#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 3.0 ##

#Draws a simplistic image of Mt.Fuji using L-Systems and shapes that use Lsystem strings from the shapes.py file 
import tree
import shapes
import turtle_interpreter

#Make a tree line and two large trees on the side of the canvas 
def treeline():
    # creates the tree object
    t = tree.Tree()
    #Provides the lsystem text file for tree object to use
    t.__init__(filename='systemH.txt')
    #sets the x position for the t.draw method
    xt=-200
    #set the y position for the t.draw method
    yt=-100
    #for loop that draws a line of trees across Mt.Fuji
    for i in range(18):
        #Draws the trees out a specific position
        t.draw(xt,yt,1.3,orientation=90)
        #increments the x position 25 every iteration
        xt+=25

def main():
    #Creates the turtle interpreter object 
    ti= turtle_interpreter.TurtleInterpreter()
    
    #Create Triangle object from shapes
    tr = shapes.Triangle()
    #Create larger Triangle
    #Light lavendar color
    tr.setColor((0.6,0.6,0.9))
    #Draws Mount Fuji Triangle 
    tr.draw(-180,-100,scale=4.0,orientation=60)
    #Sets the color of the second triangle to fill as white
    tr.setColor((1.0,1.0,1.0))
    #Draws a smaller triangle as the white cap of the mountain
    tr.draw(-30,150,1.0,60)
    
    #Make a moon in the top right sector
    cir = shapes.Circle()
    #Sets the circle to a orangeish color
    cir.setColor((0.8,0.4,0.2)) 
    #draws the circle to represetn the moon
    cir.draw(200,200,1.0,0)

    #calls in the treeline function to draw a line of trees
    treeline()

    t = tree.Tree()
    #add two large trees
    t.__init__(color=((0,0,0)),filename='placeTree.txt')
    #Draws a large tree 
    t.draw(250,-100,2.5,90)
    #Draws a large tree
    t.draw(-225,-100,2.5,90)

    #Holds the canvas open
    ti.hold()

if __name__ == '__main__':
    main()