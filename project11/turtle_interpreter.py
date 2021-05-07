#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 5.0 ##

# Version 5 implements Turtle 3D graphics
import sys
import turtleTk3D
import random

global t

class TurtleInterpreter:
    initialized = False

    def __init__(self, dx = 800 , dy = 800):
        #style field
        self.style = 'normal'
        #jitterSigma
        self.jitterSigma = 2
        #dotSize
        self.dotSize = 4
        #checks to see if TurtleInterpreter has been initialized
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True
        global t 
        t = turtleTk3D.Turtle3D(dx,dy)
        #sets ups the turtle canvas
        t.setup(dx,dy)
        #Sets the tracer to false to draw instantly
        t.tracer(False)

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
    #Method that sets the jitter3 style
    def setJitter3(self,j3):
        self.jitter3 = j3
    #Method that gets the jitter3 style
    def getJitter3(self):
        return self.jitter3
    #Method that sets the jitter3 style
    def setdotSize(self,dot):
        self.dotSize = dot
    #Method that gets the jitter3 style
    def getdotSize(self):
        return self.dotSize
    
    
    def forward(self, distance):
        # if self.style is equal to 'jitter'
        if self.style == 'jitter':
            # assign to x0 and y0 the result of turtle.position()
            x0, y0, z0 = t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward(distance)
            # assign to xf and yf the result of turtle.position()
            xf, yf, zf= t.position()
            # assign to curwidth the result of turtle.width()
            curwidth = t.width()
            # assign to jx the result of random.gauss(0, self.jitterSigma)
            jx = random.gauss(0,self.jitterSigma)
            # assign to jy the result of random.gauss(0, self.jitterSigma)
            jy = random.gauss(0,self.jitterSigma)
            # assign to jy the result of random.gauss(0, self.jitterSigma)
            jz = random.gauss(0,self.jitterSigma)
            # assign to kx the result of random.gauss(0, self.jitterSigma)
            kx = random.gauss(0,self.jitterSigma)
            # assign to ky the result of random.gauss(0, self.jitterSigma)
            ky = random.gauss(0,self.jitterSigma)
            # assign to ky the result of random.gauss(0, self.jitterSigma)
            kz = random.gauss(0,self.jitterSigma)
            # set the turtle width to (curwidth + random.randint(0, 2))
            t.width(curwidth + random.randint(0,2))
            # have the turtle go to (x0 + jx, y0 + jy)
            t.goto(x0 + jx, y0 + jy, z0 + jz)
            # put the turtle down
            t.down()
            # have the turtle go to (xf + kx, yf + ky)
            t.goto(xf + kx, yf + ky, zf + kz)
            # pick up the turtle
            t.up()
            # have the turtle go to (xf, yf)
            t.goto(xf,yf, zf)
            # set the turtle width to curwidth
            t.width(curwidth)
            # put the turtle down
            t.down()
        
        elif self.style == 'jitter3':
            #Creates starting position
            x0, y0, z0 = t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward(distance)
            # assign to xf and yf the result of turtle.position() (final position)
            xf, yf, zf = t.position()
            # assign to curwidth the result of turtle.width()
            curwidth = t.width()
            
            for i in range (3):
                # assign to jx the result of random.gauss(0, self.jitterSigma)
                jx = random.gauss(0,self.jitterSigma)
                # assign to jy the result of random.gauss(0, self.jitterSigma)
                jy = random.gauss(0,self.jitterSigma)
                # assign to jz the result of random.gauss(0, self.jitterSigma)
                jz = random.gauss(0,self.jitterSigma)
                # assign to kx the result of random.gauss(0, self.jitterSigma)
                kx = random.gauss(0,self.jitterSigma)
                # assign to ky the result of random.gauss(0, self.jitterSigma)
                ky = random.gauss(0,self.jitterSigma)
                # assign to kz the result of random.gauss(0, self.jitterSigma)
                kz = random.gauss(0,self.jitterSigma)
                # set the turtle width to (curwidth + random.randint(0, 2))
                t.width(curwidth + random.randint(0,2))
                # have the turtle go to (x0 + jx, y0 + jy)
                t.goto(x0 + jx, y0 +jy, z0 + jz)
                # put the turtle down
                t.down()
                # have the turtle go to (xf + kx, yf + ky)
                t.goto(xf + kx ,yf + ky, zf + kz)
                # pick up the turtle
                t.up()
                t.width(curwidth)
                # have the turtle go to (xf, yf)
                t.goto(xf, yf, zf)
                # put the turtle down
                t.down()
        
        elif self.style == 'dotted':
            #Creates starting position
            x0, y0, z0  = t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward(distance)
            # assign to xf and yf the result of turtle.position() (final position)
            xf, yf, zf = t.position()
            #X position difference
            xdif = xf - x0
            #Y position difference
            ydif = yf - y0
            #Z position difference
            zdif = zf - z0
            #spacing
            space = 5
            #steps
            steps = distance / space
            #if a step is less than 1 makes the step 1 so loop can iterate
            # if steps <1:
            #     steps = 1
            stepsize = space / distance
            #If a stepsize is less than 1 it makes the distance 1
            # if stepsize < 1:
            #     stepsize = 1
        
            for i in range(int(steps)):
                # assign to jx the result of random.gauss(0, self.jitterSigma)
                jx = random.gauss(0,self.jitterSigma)
                # assign to jy the result of random.gauss(0, self.jitterSigma)
                jy = random.gauss(0,self.jitterSigma)
                # assign to jz the result of random.gauss(0, self.jitterSigma)
                jz = random.gauss(0,self.jitterSigma)
                # assign rad a jitter 
                rad = random.gauss(self.dotSize, self.jitterSigma)   
                xsum= x0 + xdif * stepsize * i + jx
                ysum= y0 + ydif * stepsize * i + jy
                zsum= z0 + zdif * stepsize * i + jz
                t.goto(xsum, ysum, zsum)
                #draw circle
                #Color set is for npr_scene1.py
                #t.color(random.uniform(0.7,0.9),random.uniform(0.5,0.7),random.uniform(0.5,0.9))
                #Color set is for npr_scene2.py
                t.color(random.uniform(0.5,0.9),random.uniform(0.5,0.9),random.uniform(0.8,0.9))
                t.down()
                t.begin_fill()
                t.circle(rad)
                t.end_fill()
                t.up()
            #Go to end point
            t.goto(xf, yf , zf)

        else:
            # have the turtle go foward by distance
            t.forward(distance)

    def drawString(self, dstring, distance, angle):
        """ The distance specifies how far the turtle should move forward for the F character, 
        and the angle specifies the number of degrees the turtle should turn for a + or - character."""
    
        # Character	Action
        # F	Move the turtle forward by distance
        # +	Turn the turtle left by angle
        # -	Turn the turtle right by angle
        # [	Append the turtle's heading and position to a list (e.g. stack)
        # ]	Pop the turtle's heading and position from the list (e.g. stack) and restore the turtle's state

        #Stack to store the L-System Instructions
        stack = []
        colorStack = []
        modval = None
        modgrab = False
        
        #Loop that handles the drawing
        for c in dstring:
            if c == '(':
               modval = ''
               modgrab = True
               continue
            elif c == ')':
                modval = float(modval)
                modgrab = False
                continue
            elif modgrab == True:
                modval = modval+c
                continue
            #symbol sets F to move turtle forward
            if c == 'F':
                if modval == None:
                    self.forward(distance)
                else:
                    self.forward(distance * modval)
            if c == 'f':
                if modval == None:
                    self.forward(distance)
                else:
                    self.forward(distance * modval)
            elif c == 'L':
                t.color(colorStack[0])
                t.begin_fill()
                t.circle(5)
                t.end_fill()
            #symbol sets - to change turtle direction to the right by a certain angle or by modval angle
            elif c == '-':
                if modval == None:
                    t.right(angle)
                else: 
                    t.right(modval)
            #symbol sets + to change turtle direction to the left by a certain angle or by modval angle
            elif c == '+':
                if modval == None:
                    t.left(angle)
                else: 
                    t.left(modval)
            #symbol sets ! to change turtle width or change it by modval
            if c == '!':
                if modval == None:
                    w = t.width()
                    if w > 1:
                        t.width(w-1)
                else:
                    t.width(modval)
            #Appends the turtle postion and heading to the stack list
            elif c == '[':
                stack.append(t.position())
                stack.append(t.heading())
            #sets the heading and position from popping values from the stack list
            elif c == ']':
                t.up()
                t.setheading(stack.pop())
                t.goto(stack.pop())
                t.down()
            #Sets the pitch with positive angle heading down
            elif c == '&':
                if modval == None:
                    t.pitch(angle)
                else:
                    t.pitch(modval)
            #Sets the pitch with negative angle heading up
            elif c == '^':
                if modval == None:
                    t.pitch(angle*-1)
                else:
                    t.pitch(modval *-1)
            #Sets the roll with a positive angle right
            elif c == '\\':
                if modval == None:
                    t.roll(angle)
                else:
                    t.roll(modval)
            #Sets the roll with a negative angle left
            elif c == '/':
                if modval == None:
                    t.roll(angle*-1)
                else:
                    t.roll(modval*-1)
            #Appends t.color to the colorstack at the 0 position
            elif c =='<':
                colorStack.append(t.color()[0] )
            #Sets the color 
            elif c =='>':
                currentColor = colorStack.pop(0)
                t.color(currentColor)
            #Sets r to the color red
            elif c == 'r':
                t.color((0.7, 0.4, 0.5))
            #Sets y tp the color yellow
            elif c == 'y':
                t.color((0.8, 0.8, 0.3))
            #Sets g to the color green
            elif c == 'g':
                t.color((0.1, 0.5, 0.2))
           #sets b to the color blue
            elif c == 'b':
                t.color((0.1, 0.5, 0.8))
            #sets p to the color light pink
            elif c == 'p':
                t.color((0.9,0.6,0.6))
            elif c == '?':
                t.color((random.uniform(0.2,0.6),random.uniform(0.4,0.7),random.uniform(0.5,0.9)))
            #sets 0 to a specific position used for project 8
            elif c == '0':
                self.place(-120,150,270)
            #Starts the begin fill for coloring an object
            elif c == '{':
                t.begin_fill()
            #Ends the fill for coloring an object
            elif c == '}':
                t.end_fill()
            modval=None
        t.update()
    
    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        t.mainloop()
    
    #Places the turtle interpreter at a position and orientation
    #May need to change Angle to NONE instead of 0
    def place(self, xpos, ypos, angle=None, roll=0, pitch=0, zpos=0):
        if angle != None:
            self.orient(angle,roll,pitch)
        t.up()
        t.goto(xpos,ypos,zpos)
        t.down()
    
    def orient(self, angle, roll=0, pitch=0):
        t.setheading(0)
        t.roll(roll)
        t.pitch(pitch)
        t.yaw(angle)
    
    def goto(self, xpos, ypos, zpos= 0):
        t.up()
        t.goto(xpos,ypos,zpos)
        t.down()
    
    def setColor(self, c):
        t.begin_fill()
        t.color(c)
        t.end_fill()
        
    
    def setWidth(self, w):
        t.width(w)
    
    def roll(self,ro):
        t.roll(ro)
    
    def pitch(self, pi ):
        t.pitch(pi)

    def yaw(self, ya):
        t.yaw(ya)
