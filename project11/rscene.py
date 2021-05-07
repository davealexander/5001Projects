#David Centeno
#5001 Intensive Foundations
#Spring 2021

import shapes as sh

def drawStack( element, x, y, scale):
    if scale < 20:
        return
    
    element.draw(x,y,scale)
    drawStack(element,x + scale*0.1,y + scale*0.8,scale * 0.8)

def tree (element, x, y, scale ):
    if scale < 10:
        return

    element.draw(x,y,scale)
    tree(element,x - 0.4*scale ,y + 0.5*scale ,scale * 0.5)
    tree(element,x + 0.9*scale ,y + 0.5*scale ,scale * 0.5)
    

def main():

    s = sh.Square( distance=1, color='purple' )
    t = sh.Triangle(distance=1, color='red')
    s.setLineWidth( 3 )
    s.setStyle( 'jitter' )
    s.setJitter( 3 )

    t.setLineWidth( 3 )
    t.setStyle( 'jitter' )
    t.setJitter( 3 )

    tree( s, -50, -150, 200)
    #drawStack( s, -200, -150, 100)
    #drawStack( t, 150,-150, 100)
    

    s.hold()


if __name__ == "__main__":
    main()