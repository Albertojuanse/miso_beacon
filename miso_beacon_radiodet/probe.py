"""This class defines a radiogoniometer's probe, its position and measures"""


class Probe:

    def __init__(self, position):
        """Constructor"""
        self.position = position
        self.measures = []

    # Position getter and setter
    def getposition(self):
        return self.position

    def setposition(self, position):
        self.position = position

    # Measures stack management
    def nomeasures(self):
        """[!!] This method returns TRUE if the measures stack is empty"""
        return self.measures == []

    def addmeasure(self, item):
        """This method adds a measure to the stack"""
        self.measures.append(item)

    def popmeasure(self):
        """This method pops a measure from the stack"""
        return self.measures.pop()

    def getmeasure(self):
        """This method inspects a measure from the stack"""
        return self.measures[len(self.measures) - 1]

    def size(self):
        """This method returns measures stack size"""
        return len(self.measures)
