from cell import Cell
import time

class Maze:
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__create_cells()
        self._break_entrance_and_exit()

    def __create_cells(self):
        self._cells = []
        for i in range(0, self.num_cols):
            new_col = []
            for j in range(0, self.num_rows):
                new_col.append(Cell(self.win))
            self._cells.append(new_col)
        if self.win is not None:
            for i in range(0, len(self._cells)):
                for j in range(0, len(self._cells[i])):
                    self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        i,j = 0,0
        self._cells[i][j].has_top_wall = False
        self.__draw_cell(i,j)
        i = self.num_cols - 1
        j = self.num_rows - 1
        self._cells[i][j].has_bottom_wall = False
        self.__draw_cell(i,j)
