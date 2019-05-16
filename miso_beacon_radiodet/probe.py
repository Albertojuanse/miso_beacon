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
        self.flag_on = False

    # Position getter and setter
    def getposition(self):
        """Position getter"""
        return self.position

    def setposition(self, position):
        """Position setter"""
        self.position = position

    def isflagfinish(self):
        """Getter of the flag of finish localization for informing measures creator"""
        return self.flag_finish

    def setflagfinish(self, flag):
        """Setter of the flag of finish localization for informing measures creator"""
        self.flag_finish = flag

    def isflagon(self):
        """On flag getter; if on, the probe accepts measures"""
        return self.flag_finish

    def setflagon(self, flag):
        """On flag getter; if on, the probe accepts measures"""
        self.flag_on = flag

    # Measures queue management
    def isempty(self):
        """This method returns TRUE if the measures stack is empty"""
        return len(self.measures) == 0

    def enqueuemeasure(self, measure):
        """This method adds a measure to the queue"""
        if self.flag_on:
            self.measures.insert(0, measure)

    def dequeuemeasure(self):
        """This method pops a measure from the queue"""
        if len(self.measures) > 0:
            return self.measures.pop()
        else:
            return None

    def getmeasure(self):
        """This method inspects a measure from the queue"""
        if len(self.measures) > 0:
            return self.measures[len(self.measures) - 1]
        else:
            return None

    def size(self):
        """This method returns measures queue size"""
        return len(self.measures)

    def getcondition(self):
        return self.condition
