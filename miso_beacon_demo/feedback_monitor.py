"""This measures monitor is access by radionavigation devices and final modelling tools"""

from threading import Condition
from miso_beacon_radiodet.position import Position

points = []
condition = Condition()

isarrived = False
initialposition = Position(x=0, y=0)


def isempty():
    return len(points) == 0


def enqueuepoint(point):
    points.insert(0, point)


def dequeuepoint():
    if len(points) > 0:
        return points.pop()
    else:
        return None


def size():
    return len(points)


def getcondition():
    return condition


def setisarrived(boolean):
    global isarrived
    isarrived = boolean