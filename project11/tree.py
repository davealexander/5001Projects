#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 4.0 ##

#File that creates Lsystem trees via a Tree class. 

import lsystem 
import shapes

class Tree(shapes.Shape):

    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        sh = shapes.Shape()
        #The init method should call the parent (Shape) init method with self, distance, angle, and color. 
        #It should assign the iterations value to an iterations field of the object (self). 
        #Finally, it should create an Lsystem object (passing in the filename) and assign it to an 
        #lsystem field of self.
        sh.__init__(self,distance,angle,color)
        self.iterations = iterations
        self.lsystem = lsystem.Lsystem(filename)

    #Function that sets the iterations for the Tree class
    def setIterations(self,n):
        self.iterations = n
    
    def read(self, filename):
        self.lsystem.read(filename)

    def draw(self, xpos, ypos, scale=1.0, orientation=90, roll =0, pitch = 0, zpos =0):
        sh = shapes.Shape()
        self.string = self.lsystem.buildString(self.iterations)
        sh.draw(xpos,ypos,scale,orientation,roll,pitch,zpos)
        #draw(xpos,ypos,scale,orientation,roll,pitch,zpos)
    
    def test(self,filename):
        tree = Tree(filename=filename)
        tree.draw(0,0, scale=1.0, orientation=90)
        tree.draw(100,100,scale=1.0,orientation=90)
        tree.draw(-100,-200,scale=1.0,orientation=90)

def main():

    t=Tree()
    t.test('systemJ.txt')

    t.hold()

if __name__ == '__main__':
    main()





        