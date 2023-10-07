from graphics import Window, Line, Point

class Cell:
    def __init__(self, window=None) -> None:
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
        point1 = Point(self.x1, self.y1)
        point2 = Point(self.x2, self.y2)
        fill_color = None

        if self.has_left_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        left_wall = Line(point1, Point(point1.x, point2.y))
        self.__win.draw_line(left_wall, fill_color)

        if self.has_right_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        right_wall = Line(Point(point2.x, point1.y), point2)
        self.__win.draw_line(right_wall, fill_color)

        if self.has_top_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        top_wall = Line(point1, Point(point2.x, point1.y))
        self.__win.draw_line(top_wall, fill_color)

        if self.has_bottom_wall:
            fill_color = "black"
        else:
            fill_color = "white"
        bottom_wall = Line(Point(point1.x, point2.y), point2)
        self.__win.draw_line(bottom_wall, fill_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        point1 = Point(((self.x2 - self.x1) // 2) + self.x1, ((self.y2 - self.y1) // 2) + self.y1)
        point2 = Point(((to_cell.x2 - to_cell.x1) // 2) + to_cell.x1, ((to_cell.y2 - to_cell.y1) // 2) + to_cell.y1)
        line = Line(point1, point2)
        print(f"x1: {line.x1} y1: {line.y1}")
        print(f"x2: {line.x2} y2: {line.y2}")
        self.__win.draw_line(line, fill_color)