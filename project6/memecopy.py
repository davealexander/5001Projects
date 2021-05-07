#David Centeno
#5001 Intensive Foundations


import sys
import graphicsPlus as gr
import filter1 as filter1

def warhol( src ,text, effects):
    #Brings in an image from sys.argv
    original= gr.Image(gr.Point(0,0), src )
    #Grabs the height of the image. Used with win to create appropriate size canvas
    rows = original.getHeight()
    #Grabs the width of the image, Used with win to create appropriate size canvas
    cols = original.getWidth()
    #panels provide the amount of effects applied to an image 
    panels = len(effects)
    
    #Draws the window 
    win = gr.GraphWin('Warhol Filter', cols * panels, rows)

    #Loop that creates a clone of the original image and redraws in a new location with a filter
    for i in range(panels):
        clone = original.clone()
        if effects[i] == 'swapRedBlue':
            filter1.swapRedBlue( clone )
        elif effects[i] == 'swapincreaseBlue':
            filter1.increaseBlue( clone )
        elif effects[i] == 'cartoon':
            filter1.cartoon( clone )
    
    #Create a var that will allow sys.args to add text to meme
    
    
        clone.move(cols/2 + i * cols, rows/2)
        clone.draw(win)
    
    inputText = gr.Text(gr.Point(cols/2,rows/2),text)
    inputText.draw(win)

    return win

def main (argv):
    if len(argv) < 3:
        print('Error! Please provide the following:python3 <image filename> <effect1> <effect2> <effect3>')
        return
    
    src = sys.argv[1]
    text = sys.argv[2]
    effects = sys.argv[3: ]
    
    #creates window
    win = warhol(src, text, effects)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main(sys.argv)
       