from graphics import Window, Point
from cell import Cell

def main():
    win = Window(800,600)

    #test code
    cell1 = Cell(Point(10,10), Point(110,110), win)
    cell1.has_right_wall = False
    cell1.draw()
    cell2 = Cell(Point(110,10), Point(210,110), win)
    cell2.has_left_wall = False
    cell2.draw()
    cell1.draw_move(cell2)

    win.wait_for_close()

main()
