from cell import Cell
from graphics import Line
import time
import random

class Maze:
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win,seed=None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        else:
            random.seed(0)
        self._draw_borders()
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0 , 0)

    def _create_cells(self):
        self._cells = []
        for i in range(0, self.num_cols):
            new_col = []
            for j in range(0, self.num_rows):
                new_col.append(Cell(self.win))
            self._cells.append(new_col)
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

    def _draw_borders(self):
        x2 = self.x1 + self.num_cols * self.cell_size_x
        y2 = self.y1 + self.num_rows * self.cell_size_y
        top_border = Line(self.x1 - 1, self.y1, x2 + 1, self.y1)
        bottom_border = Line(self.x1 - 1, y2, x2 + 1, y2)
        left_border = Line(self.x1, self.y1, self.x1, y2)
        right_border = Line(x2, self.y1, x2, y2)

        self.win.draw_line(top_border, self.win.draw_color)
        self.win.draw_line(bottom_border, self.win.draw_color)
        self.win.draw_line(left_border, self.win.draw_color)
        self.win.draw_line(right_border, self.win.draw_color)

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

    def _break_walls_r(self, i, j):
        #print(f"_break_walls_r: {i}, {j}")
        self._cells[i][j].visited = True
        while True:
            to_visit = [("up", [i, j - 1]), ("right", [i + 1, j]), ("down", [i, j + 1]), ("left", [i - 1, j])]
            possible_direction = []
            for cell in to_visit:
                try:
                    if cell[1][0] < 0 or cell[1][1] < 0:
                        raise IndexError
                    if not self._cells[cell[1][0]][cell[1][1]].visited:
                        possible_direction.append(cell)
                except IndexError:
                    #print(f"IndexError at {cell[0]} - {cell[1][0]}, {cell[1][1]}")
                    pass
            if len(possible_direction) == 0:
                return
            direction = random.randint(0, len(possible_direction) - 1)
            vI = possible_direction[direction][1][0]
            vJ = possible_direction[direction][1][1]
            cell_to_visit = self._cells[vI][vJ]
            #print(f"direction: {possible_direction[direction][0]}")
            match possible_direction[direction][0]:
                case "up":
                    self._cells[i][j].has_top_wall = False
                    cell_to_visit.has_bottom_wall = False
                case "right":
                    self._cells[i][j].has_right_wall = False
                    cell_to_visit.has_left_wall = False
                case "down":
                    self._cells[i][j].has_bottom_wall = False
                    cell_to_visit.has_top_wall = False
                case "left":
                    self._cells[i][j].has_left_wall = False
                    cell_to_visit.has_right_wall = False
            self._cells[i][j].draw()
            self.__animate()
            cell_to_visit.draw()
            self.__animate()
            self._break_walls_r(vI, vJ)

    def _reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, i, j):
        
