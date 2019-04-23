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
        self.orderedmeasures = []
        self.ranges = []

    def getposition(self):
        """This method performs the calculate"""
        position = Position()
        self.orderedmeasures = [[] for i in range(len(self.measures))]

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
                    self.orderedmeasures[i].append(measure)

        # Calculate average ranging
        for i, uuid in enumerate(self.uuid):
            sum = 0
            for measure in self.orderedmeasures[i]:
                sum = sum + measure.getarrivaltime()
                # Impossible to do with any absolute temporal reference
