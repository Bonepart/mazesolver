from graphics import Window
from maze import Maze

def main():
    num_cols = 12
    num_rows = 12
    cell_size = 50

    win = Window(20 + num_rows * cell_size, 20 + num_cols * cell_size)
    m1 = Maze(10, 10, num_rows, num_cols, cell_size, cell_size, win)
    if m1.solve():
        print("Solved Maze")
    else:
        print("Solve Failed")

    win.wait_for_close()

main()
