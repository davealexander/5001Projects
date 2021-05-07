#David Centeno
#February 11 2021
#5001 Intensive foundations

import graphicsPlus as gr


def draw_shapes():
    win = gr.GraphWin("Messing around", 400 , 400 )
    c = gr.Circle(gr.Point(50,50), 10)
    

    mycircle = gr.Circle(gr.Point(100, 150), 20)
    mycircle.draw( win )

    myrectangle = gr.Rectangle(gr.Point(50,50), gr.Point(150,150))
    myrectangle.draw( win )

    myPolygon = gr.Polygon(gr.Point(100,25),
                           gr.Point(125,75),
                           gr.Point(100,100), 
                           gr.Point(75,75))
    myPolygon.draw( win )
    
    
    win.getMouse()
    win.close()



if __name__ == "__main__":
    draw_shapes()


