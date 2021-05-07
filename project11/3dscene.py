#David Centeno
#5001 Intensive Foundations
#Spring 2021

#Creates the 3D made shapes in shapes.py and makes a sunflower
import shapes
import turtle_interpreter
import random

#Creates a series of loops that creates petals 
def petals():
    #Defines the parralellogram shape from shapes.py and sets they style and colopr
    pa = shapes.parallelogram()
    pa.__init__(50)
    pa.setColor((0.9,0.7,0.3))
    pa.setStyle('jitter3')
    pa.setJitter(3)

    #sets the coordinates for the petals
    x= -15
    y= 10 
    s= 1
    o= 190

    #Series of loops that creates the petals
    # #Left half of the flower 1/3
    for i in range (5):
        pa.draw(x,y,s,o)
        x-=10
        y+=10
        o-=10
    print(x)
    # Left half of flower 2/3
    for i in range(5):
        x=-55
        pa.draw(x,y,s,o)
        y+=20
        o-=1
    # Left half of flower 3/3
    for i in range(5):
        pa.draw(x+10,y-10,s,o)
        x+=10
        y+=10
        o-=10
    # Top of flower 1/1
    for i in range(5):
        o=70
        y=180
        pa.draw(x,y,s,o)
        x+=20
   
    #Right half of flower 1/3
    for i in range(5):
        pa.draw(x,y,s,o)
        x+=10
        y-=15
        o-=15
    #Right half of flower 2/3
    for i in range(4):
        x=130
        pa.draw(x,y,s,o)
        y-=20
        o-=8
    #Right half of flower 3/3
    for i in range(4):
        pa.draw(x,y+20,s,o-20)
        x-=10
        y-=10
        o-=5

#recursive function that creates the center of the flower 
def flowerCenter( octa, x, y, scale):
    #Base case for recursion statement
    if scale < 20:
        return
    #initializes the drawing of the flower center, sets the color, and recursion parameters
    octa.__init__(0.75)
    octa.setColor((0.5,0.3,0.1))
    octa.draw(x,y,scale)
    
    #Recursive flowerCenter function
    flowerCenter(octa , x +4.5 , y + 15, scale * 0.79)

#Creates the stem of the flower 
def stem(st, x , y, iteration):
    #Base case for recursion statement
    if iteration < 50: 
        return
    
    #initializes the drawing of the stem, sets the color, and recursion parameters
    st.__init__(0.3)
    st.setColor((0.4,0.6,0.5))
    st.draw(x,y,iteration, roll=90)
    stem(st,x + 3 , y - iteration +10,iteration*0.8)

#main function that starts the program
def main():
    #calls in the turtle interpreter
    ti = turtle_interpreter.TurtleInterpreter()
    #calls the octagon shape from shapes.py
    oc = shapes.octagon()
    #initializes the octagon sizing
    oc.__init__(75)
    #draws an Octagon at the location
    oc.draw(0,0)

    #recursive function that creates smaller octagons within the initial octagon
    flowerCenter(oc, 0, 0 ,100)
    
    #Brings in the rectangle shape from shapes.py
    re = shapes.rectangle()
    #Initializes the rectangle shape with a certain size
    re.__init__(50)
    
    #Calls recursive function that creates the stem of the sunflower
    stem(re,25,0,100)
    #calls the petals function 
    petals()
    #holds the canvas open for viewing
    ti.hold()

if __name__ == "__main__":
    main()