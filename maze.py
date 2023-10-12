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
        random.seed(seed)
        self._draw_borders()
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0 , 0)
        self._reset_cells_visited()

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

    def _draw_first_move(self):
        first_cell = self._cells[0][0]
        x1 = (first_cell.x2 - first_cell.x1) // 2 + first_cell.x1
        y2 = (first_cell.y2 - first_cell.y1) // 2 + first_cell.y1
        self.__animate()
        first_move = Line(x1, 0, x1, y2)
        self.win.draw_line(first_move, self.win.move_color)

    def _draw_last_move(self):
        last_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        x1 = (last_cell.x2 - last_cell.x1) // 2 + last_cell.x1
        y1 = (last_cell.y2 - last_cell.y1) // 2 + last_cell.y1
        self.__animate()
        last_move = Line(x1, y1, x1, last_cell.y2 + 10)
        self.win.draw_line(last_move, self.win.move_color)

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
                    pass
            if len(possible_direction) == 0:
                return
            direction = random.randint(0, len(possible_direction) - 1)
            vI = possible_direction[direction][1][0]
            vJ = possible_direction[direction][1][1]
            cell_to_visit = self._cells[vI][vJ]
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
        self._draw_first_move()
        if self._solve_r(0, 0):
            self._draw_last_move()
            return True
        else:
            return False

    def _solve_r(self, i, j):
        self.__animate()
        self._cells[i][j].visited = True
        eI = len(self._cells) - 1
        eJ = len(self._cells[eI]) - 1
        if i == eI and j == eJ:
            return True
        
        #Check for possible move to the right or down first
        to_visit = [("right", [i + 1, j]), ("down", [i, j + 1]), ("left", [i - 1, j]), ("up", [i, j - 1])]
        possible_direction = []
        for cell in to_visit:
            try:
                if cell[1][0] < 0 or cell[1][1] < 0:
                    raise IndexError(f"IndexError on {cell[0]}, {cell[1]}")
                if not self._cells[cell[1][0]][cell[1][1]].visited:
                    possible_direction.append(cell)
            except IndexError as e:
                pass
        if len(possible_direction) == 0:
            return False

        while len(possible_direction) > 0:
            vI = possible_direction[0][1][0]
            vJ = possible_direction[0][1][1]
            cell_to_visit = self._cells[vI][vJ]
            match possible_direction[0][0]:
                case "up":
                    if not self._cells[i][j].has_top_wall and not cell_to_visit.has_bottom_wall:
                        self._cells[i][j].draw_move(cell_to_visit)
                        if self._solve_r(vI, vJ):
                            return True
                        else:
                            self._cells[i][j].draw_move(cell_to_visit, True)
                    possible_direction.pop(0)
                case "right":
                    if not self._cells[i][j].has_right_wall and not cell_to_visit.has_left_wall:
                        self._cells[i][j].draw_move(cell_to_visit)
                        if self._solve_r(vI, vJ):
                            return True
                        else:
                            self._cells[i][j].draw_move(cell_to_visit, True)
                    possible_direction.pop(0)
                case "down":
                    if not self._cells[i][j].has_bottom_wall and not cell_to_visit.has_top_wall:
                        self._cells[i][j].draw_move(cell_to_visit)
                        if self._solve_r(vI, vJ):
                            return True
                        else:
                            self._cells[i][j].draw_move(cell_to_visit, True)
                    possible_direction.pop(0)
                case "left":
                    if not self._cells[i][j].has_left_wall and not cell_to_visit.has_right_wall:
                        #print(f"calling draw_move({vI}, {vJ})")
                        self._cells[i][j].draw_move(cell_to_visit)
                        #print(f"calling _solve_r({vI}, {vJ})")
                        if self._solve_r(vI, vJ):
                            return True
                        else:
                            self._cells[i][j].draw_move(cell_to_visit, True)
                    possible_direction.pop(0)