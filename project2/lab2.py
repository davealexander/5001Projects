#David Centeno
#5001 Intensive Foundations Spring
#1/28/2021
#Make a complex shape

#import turtle library
import turtle as t

#import random library
import random

#go to function defines where you will start your drawing
def goto(x,y):
    t.up()
    t.goto( x , y)
    t.down()

# defines a drawing of a block that parameters take arguments for
# location, width, and height
def block(x , y , w , h):
    goto( x , y)
    for i in range (2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

#draws a tower built with block function. Takes a location and scale argument
def tower(x , y, scale):
    block(x + 0 * scale, y + 60 * scale, 20 * scale, 40 * scale)
    block(x + -10 * scale, y + 0 * scale, 40 * scale, 60 * scale)
    block(x + -20 * scale, y + -80 * scale, 60 * scale, 80 * scale)

#random tower generator. Parameter (times) provides amount of times it creates a new tower
def randomTowers(times):
    for i in range (times):
        tower(random.randrange(-200, 200), random.randrange(-200,200), random.randrange(0,3))

#tracer set to false so drawing is created instantly
t.tracer(False)

#calls randomTowers function creating x towers
randomTowers(30)

t.mainloop()

