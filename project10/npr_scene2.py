#David Centeno
#5001 Intensive Foundations
#Spring 2021

## Version 4.0 ##

#Creates a scene with a house, mirrored tress and a moon.

import tree
import shapes
import turtle_interpreter

def main():
    ti = turtle_interpreter.TurtleInterpreter()
    s = shapes.Shape()
    t = tree.Tree()

    #<-- Creates a square -->
    sq = shapes.Square()
    sq.__init__(distance=200)
    sq.setColor((0.3,0.6,0.8))
    sq.setLineWidth(5)
    sq.setStyle('jitter')
    sq.setJitter(2)
    sq.draw(-100,-50)

    #<-- Creates a Window (Right) -->
    sq = shapes.Square()
    sq.__init__(distance=75)
    sq.setColor((0.3,0.6,0.8))
    sq.setLineWidth(3)
    sq.setStyle('jitter')
    sq.setJitter(5)
    sq.draw(25,-75)

    #<-- Creates a Window2 (Left) -->
    sq = shapes.Square()
    sq.__init__(distance=75)
    sq.setColor((0.3,0.6,0.8))
    sq.setLineWidth(3)
    sq.setStyle('jitter3')
    sq.setJitter(2)
    sq.draw(-85,-75)

     #<-- Creates a door (center) -->
    sq = shapes.Square()
    sq.__init__(distance=75)
    sq.setColor((0.2,0.2,0.2))
    sq.setLineWidth(2)
    sq.setStyle('jitter')
    sq.setJitter(2)
    sq.draw(-40,-175)

    #<-- Creates a Triangle -->
    tr = shapes.Triangle()
    tr.__init__(distance=220)
    tr.setColor((0.6,0.5,0.9))
    tr.setLineWidth(1)
    tr.setStyle('jitter3')
    tr.setJitter(5)
    tr.draw(-120,-50,orientation=60)

    #<-- Creates a L-System Tree (Left) -->
    lt = tree.Tree()
    lt.__init__(30,iterations=4,filename='npr_treeL.txt')
    lt.setStyle('jitter3')
    lt.setJitter(5)
    lt.draw(-230,-250)

    #<-- Creates a L-System Tree (Right) -->
    lt = tree.Tree()
    lt.__init__(30,iterations=4,filename='npr_treeR.txt')
    lt.setStyle('jitter3')
    lt.setJitter(5)
    lt.draw(230,-250)

    #<-- Creates a L-System Tree (Right) -->
    cir = shapes.Circle()
    cir.setStyle('dotted')
    cir.setdotSize(5)
    cir.setJitter(5)
    cir.draw(230,250)

    ti.hold()
if __name__ == "__main__":
    main()