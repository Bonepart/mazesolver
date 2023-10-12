from graphics import Window, Line

class Cell:
    def __init__(self, window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.__win = window

    def draw(self, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None and y1 is not None and x2 is not None and y2 is not None:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        if self.x1 is None or self.y1 is None or self.x2 is None or self.y2 is None:
            raise Exception("Do not have coordinates for Cell Location")

        if self.has_left_wall:
            left_wall = Line(self.x1, self.y1, self.x1, self.y2)
            self.__win.draw_line(left_wall, self.__win.draw_color)
        else:
            left_wall = Line(self.x1, self.y1 + 1, self.x1, self.y2 - 1)
            self.__win.draw_line(left_wall, self.__win.background_color)

        if self.has_right_wall:
            right_wall = Line(self.x2, self.y1, self.x2, self.y2)
            self.__win.draw_line(right_wall, self.__win.draw_color)
        else:
            right_wall = Line(self.x2, self.y1 + 1, self.x2, self.y2 - 1)
            self.__win.draw_line(right_wall, self.__win.background_color)

        if self.has_top_wall:
            top_wall = Line(self.x1, self.y1, self.x2, self.y1)
            self.__win.draw_line(top_wall, self.__win.draw_color)
        else:
            top_wall = Line(self.x1 + 1, self.y1, self.x2 - 1, self.y1)
            self.__win.draw_line(top_wall, self.__win.background_color)

        if self.has_bottom_wall:
            bottom_wall = Line(self.x1, self.y2, self.x2, self.y2)
            self.__win.draw_line(bottom_wall, self.__win.draw_color)
        else:
            bottom_wall = Line(self.x1 + 1, self.y2, self.x2 - 1, self.y2)
            self.__win.draw_line(bottom_wall, self.__win.background_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "blue"
        x1 = (self.x2 - self.x1) // 2 + self.x1
        y1 = (self.y2 - self.y1) // 2 + self.y1
        x2 = (to_cell.x2 - to_cell.x1) // 2 + to_cell.x1
        y2 = (to_cell.y2 - to_cell.y1) // 2 + to_cell.y1
        line = Line(x1, y1, x2, y2)
        #print(f"x1: {line.x1} y1: {line.y1}")
        #print(f"x2: {line.x2} y2: {line.y2}")
        self.__win.draw_line(line, fill_color)