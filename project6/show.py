#David Centeno
#5001 Intensive Foundations

import sys
import graphicsPlus as gr

def main(argv):
    #test if there are two strings in the sys.argv
    if len(sys.argv) < 2 : 
        print("No image name detected. Try again")
        exit(-1)
    else:
        print("Great!Image has been received. Applying filter...")

    #bring in image file from the command line
    filename = sys.argv[1]
    
    #stores image
    src = gr.Image(gr.Point(0,0),filename)

    #Creates height and width of the image by looking at pictures size
    col = src.getWidth()
    row = src.getHeight() 
    
    #creates the window for the image to be drawn
    win = gr.GraphWin(filename,col,row)

    #image.move(col/2,row/2)
    src.move(col/2,row/2)
    src.draw( win )
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)
    
    
