from tkinter import *
from threading import Thread
import time
import random
from miso_beacon_radiodet.position import Position
from miso_beacon_demo import plotting_monitor
from miso_beacon_demo.measures_generator import MeasuresGenerator

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600


class Lienzo:

    def __init__(self):
        super().__init__()

        self.plottingcondition = plotting_monitor.getcondition()

        self.raiz = Tk()
        self.raiz.title("Lienzo")
        self.lienzo = Canvas(self.raiz, bg="white", width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.lienzo.pack()

        self.plottingcondition.acquire()
        while True:
            print("Point checking")
            point = plotting_monitor.getdata()
            if point:
                print("Point printed")
                self.lienzo.create_oval(point.getx()-1,
                                        point.gety()-1,
                                        point.getx(),
                                        point.gety())
                break
            self.plottingcondition.wait()
        self.plottingcondition.notify()
        self.plottingcondition.release()

        self.raiz.mainloop()

    def start(self):
        self.lienzo.create_line(100, 100, 200, 200)


class GUI (Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        lienzo = Lienzo()


class PointsGenerator(Thread):

    def __init__(self):
        super().__init__()
        self.condition = plotting_monitor.getcondition()

    def run(self):
        while True:
            ran1 = random.uniform(0, 1)*300
            ran2 = random.uniform(0, 1)*300
            self.condition.acquire()
            plotting_monitor.enquedata(Position(x=ran1, y=ran2))
            print("New point")
            self.condition.notify()
            self.condition.release()
            time.sleep(1)


if __name__ == "__main__":
    gui = GUI()

    generator = PointsGenerator()

    gui.start()
    generator.start()
