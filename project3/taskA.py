#David Centeno
#5001 Intensenive Foundations Spring 2021
#February 12th 2021
#This file will create a drawing of fish in the ocean using scene1 function from newshapelib

import newshapelib as nslib
import turtle as t

def main():
    #tracer draws function instantly
    t.tracer(False)
    #Calls the scene 1 function
    nslib.scene1(0,0,2,12,1)
    nslib.scene1(-200,-200,2,6,.5)
    nslib.scene1(200,-200,2,2,.2)
    #mainloop keeps the canvas open
    t.mainloop()

if __name__ == "__main__":
    main()