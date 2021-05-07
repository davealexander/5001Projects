#David Centeno
#5001 Intensive Foundations
#Spring 2021
#March 11 2021
# Program that uses Zelle to make a meme generator. 

import sys
import graphicsPlus as gr
import filter as fil

#Function that defines how the meme is drawn on to a canvas.
#Takes a src (filename), text (What the meme will say), and a list of effects (filters to apply to an image) as parameters
def meme( src , text, color, effects):
    #Brings in an image from sys.argv
    original= gr.Image(gr.Point(0,0), src )
    #Grabs the height of the image. Used with win to create appropriate size canvas
    rows = original.getHeight()
    #Grabs the width of the image, Used with win to create appropriate size canvas
    cols = original.getWidth()
    #panels provide the amount of effects applied to an image 
    panels = len(effects)
    
    #Draws the window 
    win = gr.GraphWin('Meme Generator', cols * panels, rows)

    #Loop that creates a clone of the original image and redraws in a new location with a filter
    for i in range(panels):
        clone = original.clone()
        if effects[i] == 'grayscale':
            fil.grayscale( clone )
        elif effects[i] == 'increaseBlue':
            fil.increaseBlue( clone )
        elif effects[i] == 'cartoon':
            fil.cartoon( clone )

        #Moves the meme over if there are multiple instances
        clone.move(cols/2 + i * cols, rows/2)
        #Draws the meme
        clone.draw(win)
    
    #Text settings
    #Places and calls in text from sys.argv and centers into meme
    #coordinates for angry cat meme cols +300 rows -150
    inputText = gr.Text(gr.Point(cols/2 + 300,rows/2 - 150),text)
    #Sets the size of the text
    inputText.setSize(20)
    #Sets the text to bold
    inputText.setStyle('bold')
    #Sets the color to Yellow
    inputText.setTextColor(color)
    #Draws the text in
    inputText.draw(win)
    #Returns win to be used in the main function
    return win

#Main function that calls the meme function and sets system arguments
def main (argv):
    if len(argv) < 3:
        print('Error! Please provide the following:python3 <image filename> <text> <effect1> <effect2> <effect3>')
        return
    # Saves the filepath of the image to src
    src = sys.argv[1]
    # Save the sys.argv text argument to text
    text = sys.argv[2]
    #if statement if the text field is left blank text will default to Hello World
    if text == "":
        text == "Hello World!"
    # Saves the sys.argv desired color to the color var
    color = sys.argv[3]
    # Defaults the color to black if a blank filed is left
    if color == "":
        color = "black"
    # Saves the list of filters to effects
    effects = sys.argv[4: ]
    
    #creates window
    win = meme(src, text, color, effects)

    #Closes out canvas when mouse button is clicked
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)
       