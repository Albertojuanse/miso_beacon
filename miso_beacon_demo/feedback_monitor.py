"""This feedback monitor is access by devices and measures generators"""

from threading import Condition
from miso_beacon_radiodet.position import Position

points = []
condition = Condition()

initialposition = Position(x=0, y=0)


# Common functions
def getcondition():
    """This method is the concurrent manage condition getter"""
    return condition


# Radiolocator feedback functions
radiolocatoridle = False


def isradiolocatoridle():
    """The getter of radiolocator's 'idle' flag"""
    return radiolocatoridle


def setradiolocatoridle(flag):
    """The getter of radiolocator's 'idle' flag"""
    global radiolocatoridle
    radiolocatoridle = flag


# Radionavigator feedback functions
isarrived = False
radionavegatoridle = False


def isradionavegatoridle():
    """The getter of radionavegator's 'idle' flag"""
    return radionavegatoridle


def setradionavegatoridle(flag):
    """The getter of radionavegator's 'idle' flag"""
    global radionavegatoridle
    radionavegatoridle = flag

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


def setisarrived(boolean):
    global isarrived
    isarrived = boolean