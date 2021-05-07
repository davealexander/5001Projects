#David Centeno
#February 15 2021
#5001 Intensive foundations
#Spring 2021
#Uses the complex_shape library to create a scene and takes sys arguuments to change background color of scene

#imports the grpahics plus library
import graphicsPlus as gr
#imports the complex_shapes file
import complex_shapes as cs
#imports the sys library to take system arguments
import sys

def main():
    #conditional statement that changes the background color of the canvas with a default to dark blue
    if len( sys.argv ) > 1:
        argv = str( sys.argv[1] )
    else:
        argv = 'dark blue'
    
    #calls the main function from the complex_shapes.py file
    cs.main(argv)

if __name__ =="__main__":
    main()