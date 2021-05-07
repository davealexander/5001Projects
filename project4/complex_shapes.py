#David Centeno
#February 15 2021
#5001 Intensive foundations
#Spring 2021
#complex_shapes creates a number of simple and complex shapes to create a scene and is imported into the realism.py file

# imports the graphic plus library
import graphicsPlus as gr
import time

# function that draws all the shapes in the current file. Takes a parameter for the graphicsPlus window
def draw( shapes, win ):
    for shape in shapes:
        shape.draw( win)

# defines the sun function. Uses parameters x,y,and scale to set position of where the circle/sun would be
def init_sun(x,y,scale):
    #creates a circle
    circle = gr.Circle(gr.Point(x + 10 * scale, y+ 10 * scale), 50 * scale)
    #fills the circle with the color orange
    circle.setFill('orange')

    #puts circle in a list to be used in the draw function
    sun =[circle]

    #returns sun as a list object
    return sun

# Creates a 4 towers with windows. Takes x,y as a parameter to determine location and scale int for size
def init_city(x,y,scale):
    #creates the first tower with windows. Tower one is gray and has yellow windows
    tower1 = gr.Rectangle( gr.Point( x + 30 * scale, y + 75 * scale),
              gr.Point( x + 100 * scale, y + 150 * scale) )
    tower1.setFill('gray')
    
    t1Windows = gr.Rectangle( gr.Point( x + 40 * scale, y + 85 * scale),
                     gr.Point( x + 50 * scale, y + 100 * scale) )
    t1Windows.setFill('Yellow')

    t1Windows2 = gr.Rectangle( gr.Point( x + 75 * scale, y + 105 * scale),
                     gr.Point( x + 85 * scale, y + 120 * scale) )
    t1Windows2.setFill('Yellow')

    t1Windows3 = gr.Rectangle( gr.Point( x + 40 * scale, y + 125 * scale),
                     gr.Point( x + 50 * scale, y + 140 * scale) )
    t1Windows3.setFill('Yellow')
    
    #creates the second tower with windows. Tower one is black and has white windows
    tower2 = gr.Rectangle( gr.Point( x + 105 * scale, y + 0 * scale),
                            gr.Point(x + 175 * scale, y + 150 * scale))
    tower2.setFill('black')
    
    t2Windows = gr.Rectangle( gr.Point( x + 110 * scale, y + 10 * scale),
                     gr.Point( x + 130 * scale, y + 40 * scale) )
    t2Windows.setFill('White')

    t2Windows2 = gr.Rectangle( gr.Point( x + 150 * scale, y + 50 * scale),
                     gr.Point( x + 170 * scale, y + 80 * scale) )
    t2Windows2.setFill('White')

    t2Windows3 = gr.Rectangle( gr.Point( x + 110 * scale, y + 100 * scale),
                     gr.Point( x + 130 * scale, y + 130 * scale) )
    t2Windows3.setFill('White')
    
    #creates the third tower with windows. Tower one is Gray and has White windows
    tower3 = gr.Rectangle( gr.Point( x + 185 * scale, y + 10 * scale),
                           gr.Point(x + 250 * scale, y + 150 * scale))
    tower3.setFill('gray')

    t3Windows = gr.Rectangle( gr.Point( x + 230 * scale, y + 20 * scale),
                     gr.Point( x + 245 * scale, y + 40 * scale) )
    t3Windows.setFill('Yellow')

    t3Windows2 = gr.Rectangle( gr.Point( x + 195 * scale, y + 50 * scale),
                     gr.Point( x + 210 * scale, y + 80 * scale) )
    t3Windows2.setFill('Yellow')

    t3Windows3 = gr.Rectangle( gr.Point( x + 230 * scale, y + 100 * scale),
                     gr.Point( x + 245 * scale, y + 135 * scale) )
    t3Windows3.setFill('Yellow')
    
    #creates the fourth tower with windows. Tower one is black and has yellow windows
    tower4 = gr.Rectangle( gr.Point( x + 260 * scale, y + 40 * scale),
                           gr.Point(x + 325 * scale, y + 150 * scale))
    tower4.setFill('Black')

    t4Windows = gr.Rectangle( gr.Point( x + 285 * scale, y + 50 * scale),
                     gr.Point( x + 300 * scale, y + 60 * scale) )
    t4Windows.setFill('white')

    t4Windows2 = gr.Rectangle( gr.Point( x + 285 * scale, y + 100 * scale),
                     gr.Point( x + 300 * scale, y + 140 * scale) )
    t4Windows2.setFill('white')

    #creates a list of the objectes created                       
    city = [tower1,t1Windows,t1Windows2,t1Windows3,
            tower2,t2Windows,t2Windows2,t2Windows3,
            tower3,t3Windows,t3Windows2,t3Windows3,
            tower4,t4Windows,t4Windows2]
    
    #returns city as a list to be used in the draw function 
    return city

#creates a test for the city function. Creates a city in three different positions
def test_city():
    win = gr.GraphWin("Complex Shapes", 700, 700)
    #Calls city in 3 different positions
    city1 = init_city(50,150,1)
    city2 = init_city(400,100,.5)
    city3 = init_city(200,200,1.5)

    #draws cities on the canvas
    for shape in city1:
        shape.draw( win )
    for shape in city2:
        shape.draw( win )
    for shape in city3:
        shape.draw( win )
    
    win.getMouse()
    win.close()
# definies a polygon airplane. Uses x, y , and scale to select position of plane     
def init_airplane(x, y, scale):
    #polygon points that create the plane shape
    pPoints = [gr.Point(x + 10 * scale, y + 100 * scale ), gr.Point(x + 50 * scale, y + 100 * scale),
                  gr.Point(x + 75 * scale, y + 150 * scale), gr.Point(x + 100 * scale, y + 100 * scale),
                  gr.Point(x + 150 * scale, y + 100 * scale),gr.Point(x + 175 * scale, y + 25 * scale),
                  gr.Point(x + 150 * scale, y + 50 * scale), gr.Point(x + 100 * scale, y + 50 * scale),
                  gr.Point(x + 75 * scale ,y + 15 * scale),gr.Point(x + 50 * scale ,y + 50 * scale),
                  gr.Point(x + 25 * scale ,y + 50 * scale)]
    #sets the polygon to the var planeShape
    planeShape = gr.Polygon( pPoints )
    #fills in the plane with the color gray
    planeShape.setFill('gray')
    #Makes planeShape into a list
    plane = [planeShape]
    
    #returns plane as a list to be used with the draw function
    return plane
    
# creates a bird using lines. x,y, and scale determines the postion of the bird 
def init_bird(x, y, scale):
    #lines collectively create the simple shape of a bird 
    lwing1 = gr.Line(gr.Point(x + 50 * scale, y + 50 * scale), gr.Point(x + 75 * scale, y + 25 * scale))
    lwing2 = gr.Line(gr.Point(x + 75 * scale, y + 25 * scale), gr.Point(x + 90 * scale, y + 50 * scale))
    rwing1 = gr.Line(gr.Point(x + 90 * scale, y + 50 * scale), gr.Point(x + 105 * scale, y + 25 * scale))
    rwing2 = gr.Line(gr.Point(x + 105 * scale, y + 25 * scale), gr.Point(x + 120 * scale, y + 50 * scale))

    #takes the objects listed before and makes them into a list 
    bird = [lwing1,lwing2,rwing1,rwing2]
    #returns bird as a list to be used in the draw function
    return bird
                    
# defines the drawing of a circle with variables that determines the centerpoint and radius
def init_moon(x,y,scale):
    #creates a yellow circle
    activeMoon = gr.Circle(gr.Point(x + 100 * scale, y + 100 *scale), 30 * scale)
    activeMoon.setFill('yellow')
    
    #creates an oval that layers over the activeMoon to help create the crescent shape
    shadow = gr.Oval(gr.Point(x + 120 * scale, y + 125 * scale), gr.Point(x + 70 * scale, y + 70 * scale))
    shadow.setFill('black')
    
    # makes activeMoon and shadow into a list
    moon=[activeMoon,shadow]

    #returns moon as a list to be used in the draw function 
    return moon

# Tests the moon complex shape
def test_moon():
    win = gr.GraphWin("Complex Shapes", 700, 700)
    #Calls moon in 3 different positions
    moon1 = init_moon(-50,150,1)
    moon2 = init_moon(100,100,.5)
    moon3 = init_moon(200,200,1.5)

    #draws moons on the canvas
    for shape in moon1:
        shape.draw( win )
    for shape in moon2:
        shape.draw( win )
    for shape in moon3:
        shape.draw( win )
    
    win.getMouse()
    win.close()
#defines a pyramid with variables that determine the shape of the pyramid. x ,y , and scale determine the position of the pyramid
def init_pyramid(x,y,scale):
    #creates the first rectangle of the pyramid
    trapezoid = [gr.Point(x + 50 * scale, y + 300 * scale), gr.Point(x + 100 * scale, y + 250 * scale), 
                           gr.Point(x + 300 * scale , y + 250 * scale),gr.Point(x + 350 * scale, y + 300 * scale)]
    base = gr.Polygon( trapezoid )
    base.setFill('tan')
    
    #creates the second layer of the pyramid
    trapezoid1 = [gr.Point(x + 100 * scale, y + 250 * scale),gr.Point(x + 150 * scale, y + 200 * scale),
                            gr.Point(x + 250 * scale, y + 200 * scale),gr.Point(x + 300 * scale, y + 250 * scale)]
    base2 = gr.Polygon ( trapezoid1 )
    base2.setFill('orange')
    
    #creates the third layer of the pyramid
    trapezoid2 = [gr.Point(x + 150 * scale, y + 200 * scale),gr.Point(x + 175 * scale, y + 175 * scale), 
                            gr.Point(x + 225 * scale, y + 175 * scale),gr.Point(x + 250 * scale, y + 200 * scale)]
    base3 = gr.Polygon (trapezoid2)
    base3.setFill('gold')
    
    #creates the top layer of the pyramid that squares off the pyramid 
    topper = gr.Rectangle(gr.Point(x + 175 * scale, y + 175 * scale), gr.Point(x+ 225 * scale, y + 125 * scale))
    topper.setFill('yellow')

    #Puts the previously created objects in the function into a list 
    pyramid = [ base, base2, base3, topper ]

    #Returns the pyramid var as a list and is used with the draw function
    return pyramid

    
    # Defines a deathstar shape for the use of project 5 
def init_deathStar(x,y,scale):
    
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


# Initializes the death star's ray. Function draws out 4 small rays that apex into a circle then a large diagonal beam that points to Alderaan.
def init_deathStarRay ( x, y, scale):
    
    #Creates a line that represents the rays that ultimately create the large ray that blows up Alderaan. 
    #Takes x and y as arguments for positioning around the dish of the death star.
    #Objects are listed in order of which they should hopefully be animated 
    ray1 = gr.Line(gr.Point( x + 10 * scale, y + 40 * scale), gr.Point( x - 20 * scale, y - 15 * scale))
    ray1.setFill('green')
    ray1.setWidth(4)

    ray2 = gr.Line(gr.Point( x + 30 * scale, y + 35 * scale ), gr.Point( x - 20 * scale, y - 15 * scale))
    ray2.setFill('green')
    ray2.setWidth(4)
    
    ray3 = gr.Line(gr.Point( x + 40 * scale, y + 20 * scale), gr.Point( x - 20 * scale, y - 15 * scale))
    ray3.setFill('green')
    ray3.setWidth(4)
    
    ray4 = gr.Line(gr.Point( x + 40 * scale, y + 5 * scale), gr.Point( x - 20 * scale, y - 15 * scale))
    ray4.setFill('green')
    ray4.setWidth(4)

    #Pinnacle is where all the rays meet and create the starting point of the larger ray
    pinnacle = gr.Circle(gr.Point(x - 20 * scale, y - 15 * scale), 20 * scale)
    pinnacle.setFill('light green')
    
    #center pinnacle of energy that glows white. Uses x and y parameters to determine position inside of the larger pinnacle
    centerPinnacle = gr.Circle(gr.Point(x - 20 * scale, y - 15 * scale), 15 * scale)
    centerPinnacle.setFill('white')
    
    #puts objects in a list to be used with a draw loop
    deathRay = [ray1,ray2,ray3,ray4,pinnacle,centerPinnacle]

    #returns the deathRay 
    return deathRay

# Defines the planet of Alderaan. It is a simple bluce circle. X and Y are the positions of its placement
def init_alderaan(x, y, scale):

    #defines a circle that is filled bleu
    planet = gr.Circle(gr.Point(x + 100 * scale, y + 50  * scale), 45 * scale)
    planet.setFill('blue')

    #makes planet into a list named alderaan 
    alderaan = [planet]
    
    #returns list alderaan 
    return alderaan

# Defines the explosion of Alderaan. 4 circles create a gradient which looks like an explosion. x + y should be the same as Alderaan
def init_explosion(x, y, scale):
    #Defines circles with different colors to express an explosion 
    explosion1 = gr.Circle(gr.Point(x + 50 * scale, y + 50  * scale), 50 * scale)
    explosion1.setFill('white')

    explosion2 = gr.Circle(gr.Point(x + 50 * scale, y + 50  * scale), 60 * scale)
    explosion2.setFill('light yellow')

    explosion3 = gr.Circle(gr.Point(x + 50 * scale, y + 50  * scale), 70 * scale)
    explosion3.setFill('yellow')

    explosion4 = gr.Circle(gr.Point(x + 50 * scale, y + 50  * scale), 80 * scale)
    explosion4.setFill('orange')

    #Creates a list of explosion objects
    explosion = [explosion4,explosion3,explosion2,explosion1]
    
    #returns explosion as a list 
    return explosion

#  Defines a large ray that reaches out from the death start to Alderaan. 
#  X and Y allow the ray to be moved around and when combined with the death star and death ray fixes position at the pinnacle of death ray
#  The rebel scum will not stand a chance against this.
def init_largeRay(x ,y , scale):
    #Creates the large ray that touches Alderaan. Uses x and y parameters to determine position right at the pinnacle
    largeRay = gr.Line(gr.Point(x - 15 * scale, y - 10 * scale), gr.Point(x - 150, y - 170))
    largeRay.setFill('light green')
    largeRay.setWidth(10)

    laser = [largeRay]

    return laser

# Animates Alderaan shaking and eventually exploding after a certain frame time. 
def animate_alderaan(alderaan, frame, win):
    
    #shakes Alderaan to the left and right for 25 frames
    if frame % 2 == 0:
        shake = alderaan[0]
        shake.move(5,0)
    else:
        shake= alderaan[0]
        shake.move(-5,0)
    #At 80 frames Alderaan explodes and draws the explosion list
    if frame == 80:
        alderaan[0].undraw()
        x = 10
        y = 10
        explosion = init_explosion(x, y , 1 )
        for shape in explosion:         
            shape.draw( win )
    #At 50 frames explosion expands to double its size with scale parameter
    elif frame == 105:
        x = 10
        y = 10
        explosion = init_explosion(x, y , 2)
        for shape in explosion:
            shape.draw( win )
    #At 75 frames explosion expands to 2.5 its size with scale parameter
    elif frame == 130:
        x = 10
        y = 10
        explosion = init_explosion(x, y , 2.5)
        for shape in explosion:
            shape.draw( win )

# Creates a test function of animate alderaan
def test_alderaan():
    #draws the canvas for Zelle graphics
    win = gr.GraphWin("Death Star Test", 700, 700)
    #Sets the background to the color black (space themed)
    win.setBackground('black')

    #initizalizes the init_alderaan function. Draws the rays/lasers
    alderaan = init_alderaan(10, 10, 1)
    
    for shape in alderaan:
        shape.draw(win)

    #starts the animation for alderaan
    for frame in range(150):
        animate_alderaan(alderaan, frame, win)
        win.update()
        time.sleep(0.015)

    win.getMouse()
    win.close()

#Animates the small rays on the death star eventually creatinga ball of energy
def animate_deathRay(deathRay, frame, win):
    #Every five frames adds a new ray eventually pointing towards a pinnacle of energy
    if frame == 10:
        deathRay[0].draw( win )
    elif frame == 15:
        deathRay[1].draw( win )
    elif frame == 20:
        deathRay[2].draw( win )
    elif frame == 25:
        deathRay[3].draw( win )
    elif frame == 30:
        deathRay[4].draw( win )
    elif frame == 35:
        deathRay[5].draw ( win )

# Creates a test function of the animate death ray 
def test_deathRay():
    #draws the canvas for Zelle graphics
    win = gr.GraphWin("Death Star Test", 700, 700)
    #Sets the background to the color black (space themed)
    win.setBackground('black')

    #initizalizes the largeRay function. Draws the rays/lasers
    deathRay = init_deathStarRay(500, 500, 1)

    #initizalizes the death star and draws the death star shape
    deathstar = init_deathStar( 500, 500, 1)    
    for shape in deathstar:
        shape.draw ( win )

    #animates the deathrays
    for frame in range(150):
        animate_deathRay(deathRay, frame, win)
        time.sleep(0.015)
        win.update()
    
    win.getMouse()
    win.close()

#Animates death ray shooting across space towards Alderaan
def animate_largeRay(largeRay, frame, win ):

    #Animates the large ray and makes it move across space towards alderaan. 
    #Provides the illusion that the beam is growing but is stacking the ray
    if frame == 40:
        largeRay = init_largeRay(500, 500 , 1)
        largeRay[0].draw ( win )
    elif frame == 45:
        largeRay = init_largeRay(458, 450 , 1)
        largeRay[0].draw ( win )
    elif frame == 50:
        largeRay = init_largeRay(373, 350 , 1)
        largeRay[0].draw ( win )
    elif frame == 55:
        largeRay = init_largeRay(297, 260 , 1)
        largeRay[0].draw ( win )

#Animates the largeray function
def test_largeRay():
    #draws the canvas for Zelle graphics
    win = gr.GraphWin("Death Star Test", 700, 700)
    #Sets the background to the color black (space themed)
    win.setBackground('black')
    #initizalizes the largeRay function. Draws the rays/lasers
    largeRay = init_largeRay(500, 500, 1)

    for frame in range(150):
        animate_largeRay(largeRay, frame, win)
        time.sleep(0.015)
        win.update()

    win.getMouse()
    win.close()
        
    
#Test the deathstar function prior to animation. Makes sure the entire drawing is accessible and working.
def test_deathStar():
    #draws the canvas for Zelle graphics
    win = gr.GraphWin("Death Star Test", 700, 700)
    #Sets the background to the color black (space themed)
    win.setBackground('black')

    #deathstar1= init_deathStar( 100, 100, .5)
    #initializes the deathstar. Draws out the deathstar 
    deathstar = init_deathStar( 500, 500, 1)
    
    #initizalizes the deathStarRay function. Draws the rays/lasers
    deathRay = init_deathStarRay(500, 500, 1)

    #initizalizes the largeRay function. Draws the rays/lasers
    largeRay = init_largeRay(500, 500, 1)
    
    #initizalizes the Alderaan function. Draws Alderaan 
    alderaan = init_alderaan( 10, 10 , 1)

    # for shape in deathstar1:
    #     shape.draw( win )

    for shape in deathstar:
        shape.draw ( win )

    # for shape in deathRay:
    #     shape.draw ( win )
    
    for shape in alderaan:
        shape.draw( win )
    
    # for shape in explosion:
    #     shape.draw( win )

    for frame in range (150):
        animate_deathRay(deathRay, frame, win)
        animate_largeRay(largeRay, frame, win)
        animate_alderaan(alderaan, frame , win)
        win.update()
        time.sleep(0.015)

    win.getMouse()
    win.close()

def test_pyramid():
    win = gr.GraphWin("Complex Shapes", 700, 700)
    #Calls pyramid in 3 different positions
    pyramid1 = init_pyramid(-50,150,1)
    pyramid2 = init_pyramid(100,100,.5)
    pyramid3 = init_pyramid(200,200,1.5)

    #draws pyramids on the canvas
    for shape in pyramid1:
        shape.draw( win )
    for shape in pyramid2:
        shape.draw( win )
    for shape in pyramid3:
        shape.draw( win )
    
    win.getMouse()
    win.close()

def main(color):
    #initates the Graph Window
    win = gr.GraphWin("Complex Shapes", 700, 700)
    
    #sets the background color
    win.setBackground(color)
    
    #list of shapes
    pyramid = init_pyramid(-50,150,1)
    city = init_city(300, 300, 1)
    moon = init_moon(500,5,1)
    plane =init_airplane(300,100,1)
    sun = init_sun(10,10,1)
    bird = init_bird (10, 10, 1)

    #draw shapes
    draw(pyramid, win)
    draw(city, win)
    draw(moon, win)
    draw(plane, win)
    draw(sun, win)
    draw(bird, win)
    win.getMouse()
    win.close()
    

if __name__ =="__main__":
    # calls the main function which starts the program.
    #main('dark blue')
    #test_pyramid()
    #test_moon()
    #test_city()
    
    ###--Project 5 Tests--###
    
    #test_deathStar()
    #test_alderaan()
    #test_deathRay()
    test_largeRay()