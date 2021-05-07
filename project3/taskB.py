#David Centeno
#5001 Intensenive Foundations Spring 2021
#February 12th 2021
#This file will create a drawing of a surreal image using scene2 function from newshapelib

 import newshapelib as nslib
 import turtle as t
def main():
    #enables instant drawing
    t.tracer(False)
    
    #Calls the scene2 drawing from newshapelib with an argument that will create a number of planets based of command line argument
    nslib.scene2(nPlanets)
    #keeps canvas open
    t.mainloop()

if __name__ == "__main__":
    main()