"""This class defines any system that measures a position using ranging technologies"""

from math import asin, sqrt, pow
from miso_beacon_radiodet.Position import Position

c = 299792458


class RhoRhoSystem:

    def __init__(self, measures=None):
        """Constructor"""
        if measures:
            self.measures = measures
        else:
            self.measures = []
        self.uuid = []
        self.classifiedmeasures = []
        self.ranges = []

    def classifymeasures(self):
        """This method classifies the measures using its UUID identification"""
        # It could be as large as the number of measures if everyone has got a different UUID
        self.classifiedmeasures = [[] for i in range(len(self.measures))]

        # Get every measures source's UUID
        for measure in self.measures:
            current = False
            newuuid = measure.getuuid()
            for uuid in self.uuid:
                if uuid == newuuid:
                    current = True
            if not current:
                self.uuid.append(newuuid)

        # Get the measures of every UUID
        for i, uuid in enumerate(self.uuid):
            for measure in self.measures:
                if measure.getuuid() == uuid:
                    self.classifiedmeasures[i].append(measure)

    def getpositionusingtime(self):
        """This method performs the calculate of position using time referencies"""
        position = Position()

        # Classify the input measures
        self.classifymeasures()

        # Calculate average ranging
        for i, uuid in enumerate(self.uuid):
            sum = 0
            for measure in self.classifiedmeasures[i]:
                sum = sum + measure.getarrivaltime()
                # Impossible to do with any absolute temporal reference

    def getpositionusingrssi(self):
        """This method performs the calculate of position using time referencies"""
        position = Position()

        # Classify the input measures
        self.classifymeasures()

        # Calculate average ranging
        # For each measures source...
        for i, uuid in enumerate(self.uuid):
            pass

