"""This class creates a dynamic Matplotlib plot for every position of the trajectory"""

from threading import Thread
import time
import random
import matplotlib.pyplot as plt


class Plot (Thread):

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.pointscondition = points_monitor.getcondition()
        self.points = []

    def run(self):
        notfinished = True
        plt.show()
        time.sleep(random.uniform(0, 1) + 2)
        while notfinished:
            print("PUNTO")
            self.pointscondition.acquire()
            while True:
                print("PUNTO?")
                point = points_monitor.dequeuepoint()
                if point:
                    self.points.append(point)
                    print("PUNTO")
                    break
                self.pointscondition.wait()
            self.pointscondition.notify()
            self.pointscondition.release()

            self.pointscondition.acquire()
            while True:
                arrived = points_monitor.isarrived
                if arrived:
                    notfinished = False
                    break
                self.pointscondition.wait()
            self.pointscondition.notify()
            self.pointscondition.release()

            time.sleep(1)

        xdata, ydata = [], []
        for point in self.points:
            xdata.append(point.getx())
            ydata.append(point.gety())

        plt.plot(xdata, ydata, 'ro')
        plt.title('navigator')
        plt.show()

