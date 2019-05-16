"""This class defines any system probe, its position and measures; implements a monitor"""

from threading import Condition


class Probe:

    def __init__(self, position):
        """Constructor"""
        self.position = position
        self.measures = []

        # Monitor's condition
        self.condition = Condition()

        self.flag_finish = False

    # Position getter and setter
    def getposition(self):
        return self.position

    def setposition(self, position):
        self.position = position

    # Measures queue management
    def isempty(self):
        """[!!] This method returns TRUE if the measures stack is empty"""
        return len(self.measures) == 0

    def enqueuemeasure(self, measure):
        """This method adds a measure to the queue"""
        self.measures.insert(0, measure)

    def dequeuemeasure(self):
        """This method pops a measure from the queue"""
        if len(self.measures) > 0:
            return self.measures.pop()
        else:
            return None

    def getmeasure(self):
        """This method inspects a measure from the queue"""
        return self.measures[len(self.measures) - 1]

    def size(self):
        """This method returns measures queue size"""
        return len(self.measures)

    def getcondition(self):
        return self.condition
