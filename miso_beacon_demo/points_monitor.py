"""This measures monitor is access by measures generator and measures consumers"""

from threading import Condition

points = []
condition = Condition()

isarrived = False


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
