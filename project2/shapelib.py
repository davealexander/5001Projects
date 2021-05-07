#David Centeno
#5001 Intensive Foundations Spring 2021
#2/4/2021
#Shape library for Shape collection project. This file creates scene1 and other tests required of the project

#import turtle library
import turtle as t

#import random library
import random

#go to function defines where you will start your drawing
def goto(x,y):
    t.up()
    t.goto( x , y)
    t.down()

### Basic Shapes #####

# defines a drawing of a block that parameters take arguments for
# location, width, and height
def block(x , y , w , h, color):
    goto( x , y)
    t.color(color)
    t.begin_fill()
    for i in range (2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
#defines an equilateral triangle and fills with the color gray
def triangle(x, y, l):
    goto( x, y )
    t.color('gray') 
    t.begin_fill()
    for i in range (3):
        t.forward(l)
        t.left(120)
    t.end_fill()

#defines a parralelogram  for test1
def pgram(x,y, w, h):
    goto( x , y )
    for i in range (2):
        t.forward(w)
        t.left(70)
        t.forward(h)
        t.left(110)



#### Complex shapes for Scene1 Drawing #######

#Creates the base pillar of the lighthouse function. Fills with the color Gray
def base(x,y,l,h):
    goto(x,y)
    t.color('gray')
    t.begin_fill()
    t.forward(l)
    t.left(100)
    t.forward(h)
    t.left(80)
    t.forward(l)
    t.left(80)
    t.forward(h)
    t.left(100)
    t.forward(l*1.25)
    t.end_fill()  


#Creates a circle that represents a ball of light for the lighthouse function
def ballLight(x,y,r):
    goto(x,y)
    t.circle(r)

#creates birds using two semicircles
def birds(x,y,n):
    for i in range(n):
        t.color('black')
        goto(x + random.randrange(-400,400),y + random.randrange(0,400) )
        t.left(90)
        t.circle(10,180)
        t.circle(-10,-180)
        t.setheading(0)

#def lighthouse triangle where vertex points to the light(circle)
def lightTriangle(x,y,l):
    goto( x, y )
    t.left(30)
    for i in range(2):
        t.forward(l)
        t.right(120)
    t.forward(l*2)
    for i in range (2):
        t.left(120)
        t.forward(l)
    

#### Combined complex shapes #####

#Combines balllight and triangles
def headLamp(x,y,r, l):
    goto(x,y)
    t.color('yellow')
    t.begin_fill()
    ballLight(x,y,r)
    lightTriangle(x, y + r, l)    
    t.end_fill()
    t.setheading(0)

# Combines block, triangle, base, and head lamp to create a lighthouse shape
def lighthouse(x, y, scale):
    goto(x,y)
    base(x+ 0 , y + 0 , 50 * scale, 175 * scale )
    headLamp(x-3 * scale, y + 175 * scale , 25 * scale, 100 * scale)
    t.setheading(0)
    block(x - 10 * scale, y + 90 * scale, 10 * scale, 40 * scale, 'black')
    triangle(x-30 * scale, y + 220 * scale, 50*scale )

#creates two blocks of blue water below 0 Y axis
def water(x,y):
    goto(x,y)
    block(0,0,-500,-500, 'blue')
    block(0,0,500,-500, 'blue')        

#### testing for earlier part of project #####

#draws a tower built with block function. Takes a location and scale argument
def tower(x , y, scale):
    block(x + 0 * scale, y + 60 * scale, 20 * scale, 40 * scale)
    block(x + -10 * scale, y + 0 * scale, 40 * scale, 60 * scale)
    block(x + -20 * scale, y + -80 * scale, 60 * scale, 80 * scale)

#random tower generator. Parameter (times) provides amount of times it creates a new tower
def randomTowers(times):
    for i in range (times):
        tower(random.randrange(-200, 200), random.randrange(-200,200), random.randrange(0,3))

#Test function that uses triangle and paralellogram shapes with random plot points and sizes to confirm it draws the same shapes no matter what spot you put it in.
# n parameter takes an integer argument to loop the requested amount of times
def test1(n):
    for i in range(n):
        triangle(random.randrange(-200,0),random.randrange(-200,0),random.randrange(20,150))
        pgram(random.randrange(0,200),random.randrange(0,200),random.randrange(50,150),random.randrange(20,100))

def test2(x,y,scale):
    base(x+ 0 , y + 0 , 50 * scale, 175 * scale )
    base(x-300 , y + 0 , 50 * scale, 175 * scale )
    headLamp(x-3 * scale, y + 175 * scale , 25 * scale, 100 * scale)
    headLamp(x-203 * scale, y +175 * scale , 25 * scale, 100 * scale)
    triangle(100,75,100*scale)
    triangle(100,200,100*scale)

#### end of testing section #####

#calls lighthouse and water function to create a scene
def scene1():
    lighthouse(0,0,1)
    water(0,0)
    birds(0,0,10)

#tracer disables tracing and draws the function instantly
t.tracer(False)

#calls scene1 function no parameters
scene1()

#keeps drawing pad open
t.mainloop()