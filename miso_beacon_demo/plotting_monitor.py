"""This potting monitor saves the whole info provided in every iteration for being used by plotting tools"""

from threading import Condition

data = []
condition = Condition()


def getcondition():
    return condition


def isempty():
    return len(data) == 0


def enquedata(point):
    data.insert(0, point)


def getdata():
    if len(data) > 0:
        return data.pop()
    else:
        return None
