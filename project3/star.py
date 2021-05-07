#David Centeno
#5001 Intensive foundations Spring 2021
#2/04/21

import turtle as turtle
import sys
    
# draw a star with the given number of rays of the given size
def star( rays, size, fill =False, color = 'black', width = 1):
    print('Drawing a star with', rays, 'rays of size', size )

    #
    turtle.color(color)
    if fill == False:
        turtle.begin_fill()
    # loop for the number of rays
    for i in range(rays):
        turtle.width(width)
        turtle.setheading( i * 360 / rays )
        turtle.forward( size )
        turtle.backward( size )
    if fill == False:
        turtle.end_fill()


# top level code, make drawing fast
turtle.tracer(False)

# assigns a default value
numrays = 10
# check for user input
if len( sys.argv ) > 1:
    # re-assign the value if the user provided one
    numrays = int( sys.argv[1] )

# assigns a default value
raysize = 50
if len( sys.argv ) >1:
    #re-assign the value if the user provided one
    raysize = int( sys.argv[2] )

#access to fill,color, and width values from sys.argv
fill = sys.argv[3]
color = sys.argv[4]
width = sys.argv[5]

# call the star function
star(numrays, raysize, fill, color, width)

# update and hold open the window
turtle.update()
turtle.mainloop()

#Worked with John Duffy and Kristina Lord on solutions