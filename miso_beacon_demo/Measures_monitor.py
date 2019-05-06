"""This measures monitor is access by measures generator and measures consumers"""

from threading import Condition

measures = []
condition = Condition()


def isempty():
    return len(measures) == 0


def enqueuemeasure(measure):
    measures.insert(0, measure)


def dequeuemeasure():
    if len(measures) > 0:
        return measures.pop()
    else:
        return None


def size():
    return len(measures)


def getcondition():
    return condition
