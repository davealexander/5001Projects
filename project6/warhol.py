#David Centeno
#5001 Intensive Foundations
#Spring 2021
#March 11 2021
# Program that uses Zelle graphics to create warhol type images made with programmed filters

import sys
import graphicsPlus as gr
import filter as fil

def warhol( src , effects):
    #Brings in an image from sys.argv
    oImage= gr.Image(gr.Point(0,0), src )
    #Grabs the height of the image. Used with win to create appropriate size canvas
    rows = oImage.getHeight()
    #Grabs the width of the image, Used with win to create appropriate size canvas
    cols = oImage.getWidth()
    #filters provide the amount of effects applied to an image 
    filters = len(effects)
    
    #Draws the window 
    win = gr.GraphWin('Warhol Filter', cols * filters, rows)

    #Loop that creates a clone of the original image and redraws in a new location with a filter
    for i in range(filters):
        clone = oImage.clone()
        if effects[i] == 'swapRedBlue':
            fil.swapRedBlue( clone ) 
        elif effects[i] == 'increaseBlue':
            fil.increaseBlue( clone )
        elif effects[i] == 'cartoon':
            fil.cartoon( clone )
        elif effects[i] == 'grayscale':
            fil.grayscale( clone )

        clone.move(cols/2 + i * cols, rows/2)
        clone.draw(win)
    
    return win

def main (argv):
    if len(argv) < 3:
        print('Error! Please provide the following:python3 <image filename> <effect1> <effect2> <effect3>')
        return
    
    src = sys.argv[1]
    effects = sys.argv[2: ]
    
    #creates window
    win = warhol(src, effects)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)
       