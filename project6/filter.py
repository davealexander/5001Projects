#David Centeno
#5001 Intensive Foundations

import sys
import graphicsPlus as gr

#Swaps the red and blue values of an image
def swapRedBlue( src ):
    #col gets src's width
    cols = src.getWidth()
    #row gets src's height
    rows = src.getHeight() 

    #iterates through the col and row of srcs pixels.
    #Its first step sets src's rgb values to a r, g, b var
    #Its second step switches the values
    for row in range(rows):
        for col in range(cols):
            r, g, b = src.getPixel(col,row)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            src.setPixel(col,row, gr.color_rgb(b,g,r))

#Makes a bluer image
def increaseBlue ( src ):
    #col gets src's width
    cols = src.getWidth()
    #row gets src's height
    rows = src.getHeight() 

    for row in range(rows):
        for col in range(cols):
            #Grabs the RGB color pixels
            r, g, b = src.getPixel(col,row)
            # Reduces R and G pixel colors and leaves blue. Result is a bluer image 
            src.setPixel(col ,row , gr.color_rgb(r//2, g//2, b))

#Creates a grayscale filter
def grayscale ( src ):
    #col gets src's width
    cols = src.getWidth()
    #row gets src's height
    rows = src.getHeight() 

    for row in range(rows):
        for col in range(cols):
            #Grabs the RGB value from the pixel
            r, g, b = src.getPixel(col,row)
            #Var that adds together rgb value and divides by 3 result is a whole number
            grayscale = (r+g+b)//3
            # sets the pixels to grayscale color
            src.setPixel(col ,row , gr.color_rgb(grayscale,grayscale,grayscale))

#Creates a cartoon filter
def cartoon ( src ):
    #col gets src's width
    cols = src.getWidth()
    #row gets src's height
    rows = src.getHeight() 

    for row in range(rows):
        for col in range(cols):
            #Grabs the R G B values from the pixel
            r, g, b = src.getPixel(col,row)
            #Takes the R G B values and divides them by 32 with no float value
            cR = r //32
            cG = g //32
            cB = b //32
            # sets the pixels to some multiple of 32 which limits the colors to look more cartoon. 
            src.setPixel(col ,row , gr.color_rgb(cR * 32, cG * 32, cB * 32))

def test_Filter (argv):
    #bring in image file from the command line
    filename = sys.argv[1]

    #stores image
    image = gr.Image(gr.Point(0,0),filename)
    
    #determines picture width and height
    col = image.getWidth()
    row = image.getHeight() 

    #swaps reds for blue in an image
    swapRedBlue( image )

    #creates the window for the image to be drawn
    win = gr.GraphWin(filename,col,row)

    #image.move(col/2,row/2)
    image.move(col/2,row/2)
    
    #draws out the image
    image.draw( win )
    
    #Save an image of the file to current directory 
    image.save('SavedFilter.ppm')
    
    #closes out canvas when mouse is clicked
    win.getMouse()
    win.close()

if __name__ == "__main__":
    test_Filter(sys.argv)