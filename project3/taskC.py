#David Centeno
#5001 Intensenive Foundations Spring 2021
#February 12th 2021
#This file will create a drawing of a surreal image using scene2 function from newshapelib.
#This file also uses sys.argv to take in command line arguments to change the scene.


import newshapelib as nslib
import turtle as t
import sys

def main():
 #Establish a minimum of 1 planet being created with sysargs
    nPlanets= 1
    if len( sys.argv ) > 1:
        nPlanets= int( sys.argv[1] )
   
    #enables instant drawing
    t.tracer(False)
    
    #Calls the scene2 drawing from newshapelib with an argument that will create a number of planets based of command line argument
    nslib.scene2(nPlanets)
    #keeps canvas open
    t.mainloop()

if __name__ == "__main__":
    main()
