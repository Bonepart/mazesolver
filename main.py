from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, height=height, width=width)
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2) -> None:
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1,self.y1,self.x2,self.y2, fill=fill_color, width=2)
        canvas.pack()

class Cell:
    def __init__(self, point1, point2, window) -> None:
        self.has_left_wall = True
        self.__left_wall = Line(point1, Point(point1.x, point2.y))
        self.has_right_wall = True
        self.__right_wall = Line(Point(point2.x, point1.y), point2)
        self.has_top_wall = True
        self.__top_wall = Line(point1, Point(point2.x, point1.y))
        self.has_bottom_wall = True
        self.__bottom_wall = Line(Point(point1.x, point2.y), point2)
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
        self.__win = window

    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(self.__left_wall, "purple")
        if self.has_right_wall:
            self.__win.draw_line(self.__right_wall, "purple")
        if self.has_top_wall:
            self.__win.draw_line(self.__top_wall, "purple")
        if self.has_bottom_wall:
            self.__win.draw_line(self.__bottom_wall, "purple")

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
