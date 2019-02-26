
from graphics import *

def grid():
    win = GraphWin("My Grid", 1001, 601)
    win.setBackground("white")
    win.getMouse()
    columns = 0
    x1 = 1
    x2 = 100
    y1 = 100
    y2 = 1    
    while columns < 10:
        rows = 0
        while rows < 6:
            square = Rectangle(Point(x1,y1), Point(x2,y2))
            square.draw(win)
            y1 += 100
            y2 += 100
            rows += 1
        columns += 1
        x1 += 100
        x2 += 100
        y1 = 100
        y2 = 1
   
    win.getMouse() # pause for click in window
    win.close()

grid()