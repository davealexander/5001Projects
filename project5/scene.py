#David Centeno
#February 4th 2021
#5001 Intensive foundations
#Spring 2021
# File creates the scene from star wars where the Death Star blows up Alderaan

# Scene Animation: https://drive.google.com/file/d/17bIHSun-le4QPID0b9vvY9rIrI_teyTV/view?usp=sharing
# Large Ray Animation: https://drive.google.com/file/d/19uT-Rlj2v909HbyP-ZVV33arM6Jf9UUP/view?usp=sharing
# Death Ray Animation: https://drive.google.com/file/d/1QbrROOjAweuF_v6B67Do4VDkiE0BGZGn/view?usp=sharing
# Alderaan Animation: https://drive.google.com/file/d/1gh9_Jvgi93QjZWGHGMvNFt-oDVgyk8VB/view?usp=sharing

import complex_objects as cshape
import graphicsPlus as gr
import time
import sys

def main(argv):
    speed = float(sys.argv[1])
    if speed >= 10:
        print("Error: Please pick a number from .001 - 1.0")
        exit(-1)
    else:
        #draws the canvas for Zelle graphics
        win = gr.GraphWin("Death Star Test", 700, 700)
        #Sets the background to the color black (space themed)
        win.setBackground('black')
        #deathstar1= init_deathStar( 100, 100, .5)
        #initializes the deathstar. Draws out the deathstar 
        deathstar = cshape.init_deathStar( 500, 500, 1)
        
        #initizalizes the deathStarRay function. Draws the rays/lasers
        deathRay = cshape.init_deathStarRay(500, 500, 1)

        #initizalizes the largeRay function. Draws the rays/lasers
        largeRay = cshape.init_largeRay(500, 500, 1)
        
        #initizalizes the Alderaan function. Draws Alderaan 
        alderaan = cshape.init_alderaan( 10, 10 , 1)

        #draws the deathstar
        for shape in deathstar:
            shape.draw ( win )
        #draws Alderaan
        for shape in alderaan:
            shape.draw( win )
        
        #animates the deathRay that causes alderaaan to explode
        for frame in range (150):
            cshape.animate_deathRay(deathRay, frame, win)
            cshape.animate_largeRay(largeRay, frame, win)
            cshape.animate_alderaan(alderaan, frame , win)
            win.update()
            time.sleep(speed)

        win.getMouse()
        win.close()

if __name__ =="__main__":
    main(sys.argv)