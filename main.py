from graphics import Window
from maze import Maze

def main():
    num_cols = 10
    num_rows = 10
    cell_size = 50

    win = Window(20 + num_rows * cell_size, 20 + num_cols * cell_size)
    m1 = Maze(10, 10, num_rows, num_cols, cell_size, cell_size, win)
    m1.solve()
    win.wait_for_close()

main()
