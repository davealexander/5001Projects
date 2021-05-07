#David Centeno
#5001 Intensive Foundations
#Spring 2021

#Creates the 3D made shapes in shapes.py with different line styles. 

import shapes
import turtle_interpreter

def main():
    ti = turtle_interpreter.TurtleInterpreter()
    
    cu = shapes.cube()
    cu.__init__(100)
    cu.setStyle('jitter')
    cu.setJitter(4)
    cu.setColor( (0.6, 0.1, 0.7) )
    cu.draw(0,0,1,90,0,0,0)

    oc = shapes.octagon()
    oc.__init__(100)
    oc.setStyle('jitter3')
    oc.setJitter(5)
    oc.setColor( (0.3, 0.6, 0.8) )
    oc.draw(-200,-100,1,90,0,0,100)

    
    re = shapes.rectangle()
    re.__init__(100)
    re.setStyle('dotted')
    re.setJitter(5)
    re.draw(250,100,1,90,0,0,100)

    
    pa = shapes.parallelogram()
    pa.__init__(100)
    pa.draw(200,-100,1,0,0,0,0)

    ti.hold()

if __name__ == "__main__":
    main()
    
    

