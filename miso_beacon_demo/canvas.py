from tkinter import *
from threading import Thread

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 700


class MyCanvas:

    def __init__(self):
        super().__init__()

        self.raiz = Tk()
        self.raiz.title("Radionavegador")
        self.canvas = Canvas(self.raiz, width=CANVAS_HEIGHT, height=CANVAS_HEIGHT)
        self.canvas.pack()

        mainloop()

    def paint(self, x, y):
        python_green = "#476042"
        self.canvas.create_oval(x-1, y-1, x+1, y+1, fill=python_green)
        self.canvas.after(1)


class GUI (Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        return MyCanvas()



