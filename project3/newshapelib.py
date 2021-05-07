#David Centeno
#5001 Intensenive Foundations Spring 2021
#February 12th 2021
#File is a shape library that will be used for importing into other files in the project folder

# imports the turtle library and can be referenced with t. 
import turtle as t
# imports the random library and can be referenced with r. 
import random as r

#imports sys which allows functions to take command line arguments
import sys

# Creates a function that allows drawing at a specific coordinate
def goto(x,y):
    t.up()
    t.goto( x , y)
    t.down()
    t.color('black')

#### Simple Shapes ####

#Creates a sqaure that takes the parameters of x, y ,length, height, fill, color, width
def square( x, y, w, h, fill = False, color ='black', width =1):
    goto(x,y)
    t.width(width)
    if fill:
        t.color(color)
        t.begin_fill()
        for i in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)
        t.end_fill()
    else:
        for i in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)

#defines an equilateral triangle used for the head shape
def triangle(x, y, l, fill = False, color = 'black', width=1):
    goto( x, y )
    if fill:
        t.color(color)
        t.begin_fill()
        t.left(90)
        for i in range (3):
            t.forward(l)
            t.right(120)
        t.end_fill()
    else:
        for i in range (3):
            t.forward(l)
            t.left(120)

#defines a paralelogram used for the tail shape. Reverse conditional will create the paralelogram in the reverse direction
def pgram(x,y, w, h, fill = False, color = 'black', width=1, reverse = False):
    goto( x , y )
    if fill:
        t.color(color)
        t.begin_fill()
        if reverse:
            for i in range (2):
                t.forward(w)
                t.right(70)
                t.forward(h)
                t.right(110)
        else:
            for i in range (2):
                t.forward(w)
                t.left(70)
                t.forward(h)
                t.left(110)
        t.end_fill()
    else: 
        if reverse:
            for i in range (2):
                t.forward(w)
                t.right(70)
                t.forward(h)
                t.right(110)
        else:
            for i in range (2):
                t.forward(w)
                t.left(70)
                t.forward(h)
                t.left(110)

#defines a circle that is used for the of the fish shape
def eye(x,y,r, fill = False, color = 'black', width=1):
    goto(x,y)
    if fill:
        t.color(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()
    else:
        t.circle(r)

# Makes waves Use the color parameter to match the background color to make the waves visible
def waves(x,y, n, fill= False, color='black',width=1):
    goto(x,y)
    t.color(color)
    if fill:
        t.begin_fill()
        t.right(90)
        t.circle(20,180)
        for i in range (n):
            t.left (180)
            t.circle(20,180)
        t.end_fill()
    else:
        t.right(90)
        t.circle(20,180)
        for i in range (20):
            t.left (180)
            t.circle(20,180)

#Makes stars set out in a random location
def stars(x, y, l, n):
    for i in range(n):
        goto(x + r.randrange(-400,400), y + r.randrange(-400,400))
        for i in range(5):
            t.color('white')
            t.left(145)
            t.forward(l) 
        t.setheading(0)   

#defines a planet used for scene 2
def planet(x,y,rad, fill = False,r=0,g=0,b=0, width=1):
    goto(x,y)
    t.colormode(255)
    if fill:
        t.color(r,g,b)
        t.begin_fill()
        t.circle(rad)
        t.end_fill()
    else:
        t.circle(rad)

#Creates an ellipses. r controls the radius/size and r2 controls the angle. 90 will make a complete ring. 
#If < or > than 90 ellipses will pass the original axis and leave a tail
def ring(x,y,r,r2, width):
    goto(x,y)
    t.width(width)
    for i in range(2):
        t.color('white')
        t.circle(r,r2)
        t.circle(r/10,r2)
    
#### End Simple Shapes ####

### Aggregate Shapes ####

##Fish Aggregate Shapes ##
# function that draws a fish tail paramater. defaults will draw the shape without color 
def tail(x,y,scale,fill = False, color = 'black', width =1):
    pgram(x - 50 * scale, y + 50 * scale, 50 * scale,38 * scale, True, color , width,True)
    pgram(x - 50 * scale, y -20 * scale, 50 * scale,38 * scale, True, color ,width,False)

# function that draws the body of the fish. Color parameter will set the color of the body of the fish
def body(x,y,scale,fill = False, color = 'black', width =1):
    goto(x,y)
    square(x , y , 25 * scale , 38 * scale , True , 'black' ,width)
    square(x + 25 * scale , y , 25 * scale ,38 * scale , True, color, width)
    square(x + 50 * scale  , y , 25 * scale , 38 * scale , True , 'black' ,width)

# function that draws the head of the fish function. Defaults will draw the shape without color
def head(x,y,scale,fill = False, color = 'black', width =1):
    triangle(x + 70 * scale, y - 5 * scale, 50 * scale, True , color, width)
    eye(x + 90 * scale, y + 23 * scale, 5 * scale, True, 'black', width)

## End Fish Aggregate Shapes ##

##Ocean Aggregate Shapes ##

#Draws two large blocks of a chosen color.  
def water(x, y, scale, fill = False, color = 'black', width=1):
    goto(x,y)
    square(x , y  , -250 * scale , 250 * scale , True, color ,width)
    square(x , y  , 250 * scale, 250 * scale, True, color ,width)

## End Ocean Aggregate Shapes ##

## Planet Aggregate Shapes ##
#Draws a planet with ring around it. If ring is listed last ring will draw over the planet
def fullPlanet(x,y,scale, fill= False, r=0, g=0,b=0, width=1):
    ring(x -70, y - 30 , 300 * scale, 90, 1)
    planet(x , y , 100 * scale, True, r, g, b, 1)
        
    
### Final Shapes #####

# Draws a fish using aggregate shapes and will default to a black and white fish when set to false. 
def fish(x,y, scale,fill= False, color ='black', width =1):
    goto(x,y)
    tail(x , y , scale , fill , color, width)
    body(x , y , scale , fill , color, width)
    head(x , y , scale , fill , color, width)
    t.setheading(0)

# Draws an ocean. w argument sets the amount of waves/crescents in the ocean
def ocean(x,y,scale, w, fill = False, color='black', wcolor='blue', width=1):
    goto(x,y)
    water(x , y , scale, fill, color, width)
    waves(x - 250 * scale, y + 250 * scale, w  , fill, wcolor , width)
    t.setheading(0)

## Scenes ##

#Draws fish inside of an ocean. N controls the amount of fish created in for loop
def scene1(x,y,n,w,scale):
    ocean(x,y,scale,w,True,'blue','white',1)
    for i in range(n):
        fish(x -30 , y + 20 ,scale,True,'orange',2)
        #Creates new fish in a different controlled position
        x+=180 * scale
        y+=10 * scale

#Draws a space scene with two planets using scene 1 with controlled parameters. 
#n will take an argument that is an int or from command line and iterate the requested amount of times
def scene2(n):
    t.bgcolor('black')
    stars(r.randint(0,10),r.randint(0,10),15,50)
    ## static image
    fullPlanet(200,-200, .7, True, 0, 0, 255, 1)
    fullPlanet(-200,200, .7, True, 0, 0, 255, 1)
    scene1(200,-175,2,2,.2)
    scene1(-200,225,2,2,.2)
    fish(-200,-300,.5,True,'purple',1)
    fish(200,200,.7,True,'turquoise',1)
    ##Dynamic image
    for i in range(n):
       fullPlanet(r.randint(-300,300),r.randint(-300,300),.5,True,r.randint(0,255),r.randint(0,255),r.randint(0,255),1)




#### Shape Testing #####
#.tracer(False)

#square(0,0,100,100,True,'blue',2)
#triangle(300,300, 150,True,'purple', 5)
#pgram(-200,-200,100,75,True,'orange',3,True)
#planet(0,0,100,True,'brown',3)
#ring(-30,-25,150,90)
#stars(r.randint(0,10),r.randint(0,10),50,25)

# waves(-400,0, False,'blue',2)

#### Aggregate Shapes Testing ######
#tail(0,0,.3,True,'orange',2)
#water(0,-300,.5,True,'blue',1)

#### Final Shape Testing ####
#ocean(0,0,1,15,True,'blue',1)
#fish(0,0,1,True,'orange',1)
#fullPlanet(0,0,1,True,2)

#### Scene Testing ####
#scene1(0,0,2,10,1)
#scene2(2)

#t.mainloop()


#extension?
#added new logic for a reverse of the shape using a conditional statement