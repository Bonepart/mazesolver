from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.draw_color = "black"
        self.background_color = "white"
        self.move_color = "blue"
        self.undo_color = "grey"
        self.canvas = Canvas(self.__root, height=height, width=width, background=self.background_color)
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

class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1,self.y1,self.x2,self.y2, fill=fill_color, width=2)
        canvas.pack()