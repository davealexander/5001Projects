#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 5.0 ##

#A shape file that creates classes to be called for use of drawing shapes in other files. 

import turtle_interpreter

class Shape:
    
    def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = ''):
    # create a field of self called distance and assign it distance
        self.distance = distance
    # create a field of self called angle and assign it angle
        self.angle = angle
    # create a field of self called color and assign it color
        self.color = color
    # create a field of self called string and assign it istring
        self.string = istring
    # creates a field of self called style and assigns a string that will define a style
        self.style = 'normal'
    # creates a field of self called jitterSigma which causes the line to move a small amount
        self.jitterSigma = 2
    # creates a field of self called lineWidth which sets the line width
        self.lineWidth = 1
    # creates a field of self called dotSize which sets the size of the dot being created.
        self.dotSize = 2
    
    
    #Method that sets the style
    def setStyle(self, s):
        self.style = s
    #Method that gets the style currently stored
    def getStyle(self):
        return self.style
    #Method that sets the jitterSigma
    def setJitter(self,j):
        self.jitterSigma = j
    #Method that get the current jitterSigma
    def getJitter(self):
        return self.jitterSigma
    #Method that sets the lineWidth
    def setLineWidth(self,l):
        self.lineWidth = l
    #Method that gets the current lineWidth
    def getLineWidth(self):
        return self.lineWidth
    #Method that sets the jitter3 style
    def setdotSize(self,dot):
        self.dotSize = dot
    #Method that gets the jitter3 style
    def getdotSize(self):
        return self.dotSize
    
    # setColor(self, c) - set the color field to c
    def setColor(self,c):
        self.color = c
    # setDistance(self, d) - set the distance field to d
    def setDistance(self,d):
        self.distance = d 
    # setAngle(self, a) - set the angle field to a
    def setAngle(self,a):
        self.angle = a
    # setString(self, s) - set the string field to s
    def setString(self, s):
        self.string = s
    
    
    #draw function
    def draw(self, xpos, ypos, scale=1.0, orientation=0, roll=0, pitch=0,zpos=0 ):
      # Sets ti to use the TurtleInterpreter from the turtle)interpreter.py file
        ti = turtle_interpreter.TurtleInterpreter() 
      # Uses the turtle interpreter class place method to set the position of this Class
        ti.place(xpos,ypos,orientation,roll,pitch,zpos)
      # Uses the turtle interpreter class setcolor method to set the color of this Class
        ti.setColor(self.color)
      # Uses the turtle interpreter class setStyle method to set the style of this Class 
        ti.setStyle(self.style)
      # Uses the turtle interpreter class setJitter method to set the jitter of this Class 
        ti.setJitter(self.jitterSigma)
      # Uses the turtle interpreter class setStyle method to set the style of this Class 
        ti.setWidth(self.lineWidth)
      # Uses the turtle interpreter class drawstring method to draw the string of this Class
        ti.drawString(self.string, self.distance * scale ,self.angle)
     
    
    #method that holds up the drawing canvas of the turtle class
    def hold(self):
        turtle_interpreter.TurtleInterpreter.hold(self)

#Class that makes a square using a set L-System string
class Square(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        #Borrowing init function from the parent class shape to set distance,
        #angle, color and istring
        
        Shape.__init__(self,distance,90,color,'F-F-F-F-')

#Class that creates a triangle using a set L-system string
class Triangle(Shape):
    #Triangles init function
    def __init__(self, distance=100, color=(0, 0, 0) ):
        #Borrowing init function from the parent class shape to set distance,
        #angle, color and istring
        Shape.__init__(self,distance,120,color,'F-F-F-')

#Class that creates a Hexagon using a set L-system string
class Hexagon(Shape):
    #Hexagon init function
    def __init__(self,distance=100, color=(0 , 0, 0)):
        #Borrowing init function from the parent class shape to set distance,
        #angle, color and istring
        Shape.__init__(self,distance,60,color, '{F-F-F-F-F-F}')

#Class that creates a Star using a set L-system string
class Star (Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        #Borrowing init function from the parent class shape to set distance
        #angle, color and istring
        Shape.__init__(self,distance,216,color,'{F-F-F-F-F-}')

#Class that creates a Cross using a set L-system string
class Cross (Shape):
    #Borrowing init function from the parent class shape to set distance,
    #angle, color and istring
    def __init__(self, distance=100, color=(0,0,0), style='normal' ):
        Shape.__init__(self,distance,90,color,'F-F+F-F-F+F-F-F+F-F-F+F-F')

#Class that creates a circle using a set L-system string
class Circle (Shape):
    #Borrowing init function from the parent class shape to set distance,
    #angle, color and istring
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self,1,1,color,'F+F+F+F+F+F+F+F+F+F+F+F+F'*30)

#<-- 3D Shapes -->
class cube (Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self,distance,90,color,'F+F+F+F(90)^F(90)^F(90)^F(90)^F+F(90)^F(90)^F(90)^F(90)^F+F+F(90)^F(90)^F[+F]+(90)^F')

class octagon (Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self,distance,90,color,'F[(90)^F](45)+F[(90)^F](45)+F[(90)^F](45)+F[(90)^F](45)+F[(90)^F](45)+F[(90)^F](45)+F[(90)^F]{(45)+F(90)^F(90)^F(45)+F(45)+F(45)+F(45)+F(45)+F(45)+F(45)+F}')

class rectangle (Shape):
    #Borrowing init function from the parent class shape to set distance,
    #angle, color and istring
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self,distance,90,color,'{F+F+F+F}{(90)^FFF}{(90)^+F-[F-F-F]}(90)^FFF(90)&F(90)&}{FFF-F-FFF}')

class parallelogram (Shape):
    #Borrowing init function from the parent class shape to set distance,
    #angle, color and istring
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self,distance,90,color,'F(45)+[F(135)+[F(45)+[F(90)^F(90)^F](90)^F(90)^(45)+F](90)^{F(90)^(135)+F](90)^F(90)^(45)+F}')

class pyramid (Shape):
    def __init__(self, distance=100, color=(0,0,0)):
        Shape.__init__(self,distance,90,color, '[F+F+F+[F(135)+(45)^F(90)&F](45)+(45)^F(90)&F]')

   


#Function that initiates shape classes 
def testShape():
    #Object creation for shape classes
    s = Shape()
    cr = Cross()
    st = Star()
    hx = Hexagon()
    tr = Triangle()
    sq = Square()
    cir = Circle()

    #Cross init function that designates a color to the cross class (Color is Red)
    cr.__init__(color=(0.8,0.3,0.3))
    #Uses draw method to draw Cross
    cr.draw(-200,-200,.5,0)
    #Uses draw method to draw Star
    st.draw(-100,100,1,90)
    #Hexagon init function that designates a color to the hexagon class (Color is purple)
    hx.__init__(color=(0.6,0.2,0.6))
    #Uses draw method to draw Hexagon
    hx.draw(0,0,.5,0)
    #Uses draw method to draw Triangle
    tr.draw(100,-100,1,60)
    #Uses draw method to draw Square
    sq.draw(200,-200,.5,0)
    #Shape method hold that keeps the canvas open until button is clicked or q is pressed
    cir.draw(300,300,.2,0)
    s.hold()
