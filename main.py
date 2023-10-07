from graphics import Window, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800,600)

    #test code
    num_cols = 6
    num_rows = 6
    m1 = Maze(10, 10, num_rows, num_cols, 40, 40, win)

    win.wait_for_close()

main()
