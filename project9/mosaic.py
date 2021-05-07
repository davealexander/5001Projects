#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 3.0 ##

#Draws a mosaic using tiles, trees, and shapes. 

import shapes
import tree
import turtle_interpreter

#Creates a square tile that creates an lsystem at the 
def tile(x, y, scale):
    #Create the square object
    sq = shapes.Square()
    #Set the distance and scale of the squares using init function
    sq.__init__(distance=100*scale)
    #Draw the tile
    sq.draw(x,y,orientation=90)
    
    #Creates the star object
    st = shapes.Star()
    #Sets the distance and color of the star shape
    st.__init__(distance=95*scale, color=(0.8,0.8,0.6))
    #Draw the star object 
    st.draw(x + 75 *scale, y + 10 * scale,orientation=108)
    
    #Create the tree object 
    t = tree.Tree()
    #Set the distance, color, and filename using the init function
    t.__init__(distance= 5 * scale, color=(0.3,0.6,0.5), filename="mosaic.txt")
    #Draws the L-System Tree
    for i in range (3):
        for j in range(2):
            t.draw(x,y,orientation=90)
            x+=100*scale
        x = x-200*scale
        y+=50*scale
    
#Draws the mosaic
def mosaic(x,y,scale, nx, ny):
    #For loop that controls the iteration on the y axis ny=iterations
    for i in range(ny):
        #For loop that controls the iteration on the x axis nx=iterations
        for j in range(nx):
            #calls the tile function
            tile(x,y,scale)
            #Adds 100 to the x value every time through the loop
            x+=100*scale
        #Resets x back to the original x * scale value
        x = x-500*scale
        #Adds 100*scale to the original value of y
        y += 100*scale

def main():
    mosaic(-200,-200,1, 5, 4)

    ti = turtle_interpreter.TurtleInterpreter()

    ti.hold()

if __name__ == '__main__':
    main()