#David Centeno
#5001 Intensive Foundations Spring
#2/4/2021
#create a second scene for shape collection project. File draws a house thats either night or day 
#import turtle library
import turtle as t

#import random library
import random

#go to function defines where you will start your drawing
def goto(x,y):
    t.up()
    t.goto( x , y)
    t.down()

#### Basic Shapes #####

#Draws a triangle that will be colored in
def triangle(x,y,l,color):
    goto(x, y)
    t.color(color)
    t.begin_fill()
    for i in range (3):
        t.forward(l)
        t.left(120)
    t.end_fill()

#draws a block that will be colored in 
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

# draws a yellow star an x amount of times at random locations
def stars(x, y, l, n):
    t.color('yellow')
    for i in range(n):
        goto(x + random.randrange(-500,500), y + random.randrange(100,400))
        for i in range(5):
            t.left(145)
            t.forward(l) 
        t.setheading(0)   
#draws petals of a flower
def petals(x,y,r,color):
    goto(x,y)
    t.color(color)
    t.begin_fill()
    for i in range (6):
        t.circle(r)
        t.left(60)
    t.end_fill()
# Two large blocks that represent grass
def grass(x,y):
    block(x,y,-500,-300,'green')
    block(x,y, 500,-300,'green')

#Two large blocks that creates blue sky or night sky with stars
def sky(x,y,night = False):
    if night:
        block(x,y,-500,500, 'black')
        block(x,y, 500,500, 'black')
        stars(x,y,20, 50)
    else:
        block(x,y,-500,500, 'light blue')
        block(x,y, 500,500, 'light blue')
    
# Creates flower shape using the block and petals functions
def flowers(x,y, scale):
        block(x, y  , 1 * scale, 40 * scale, 'black')
        petals(x, y + 40 * scale, 5 * scale, 'pink')

# Creates multiple flowers in a random plot
def flowerGenerator(x,y,n, scale):
    goto(x,y)
    for i in range(n):
        flowers(random.randrange(-500,500),random.randrange(-300,0), scale)

# Creates a House ( or gnome? )
def house(x,y,scale):
    goto(x,y)
    block(x ,y , 200 * scale,150 * scale,'beige')
    block(x + 20 * scale, y + 75 * scale, 40 *scale, 40 * scale, 'blue')
    block(x+ 135 * scale, y + 75 * scale, 40 *scale, 40 * scale, 'blue')
    block(x+ 70 * scale, y * scale, 50 * scale, 75 * scale, 'brown')
    triangle(x,y + 150*scale, 200 * scale, 'brown')


#show drawing instantly
t.tracer(False)

#creates a scene with all the other complex shapes. Takes argument for night (True) or day (False)
def scene2(night):
    grass(0,0)
    sky(0,0,night)
    house(-100,0,1)
    flowerGenerator(0,-50,50,1)

#Calls scene2 with an argument of either True or False for Night( True ) or Day (False)
scene2(False)
#keeps drawing open
t.mainloop()