"""This class defines any system that measures a position using ranging technologies"""

from math import asin, sqrt, pow, exp
from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.miso_beacon_range.rssi_ranger import RSSIRanger

from scipy.optimize import fsolve


class RhoRhoSystem:

    def __init__(self, frecuency, gain, measures=None):
        """Constructor"""
        if measures:
            self.measures = measures
        else:
            self.measures = []
        self.frecuency = frecuency
        self.gain = gain
        self.uuid = []
        self.classifiedmeasures = []
        self.averagedmeasures = []
        self.ranges = []

    def setmeasures(self, measures):
        self.measures = measures

    def classifymeasures(self):
        """This method classifies the measures using its UUID identification"""
        self.classifiedmeasures = []
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

    def averagemeasures(self):
        """This method calculates the measures' average"""
        self.averagedmeasures = []
        # For each measures source...
        for i, uuid in enumerate(self.uuid):
            # ...get the average.
            sum = 0
            for measure in self.classifiedmeasures[i]:
                sum = sum + measure.getrssi()
            self.averagedmeasures.append((uuid, sum / len(self.classifiedmeasures[i])))

    def getpositionusingtime(self):
        """This method performs the calculate of position using time references"""
        position = Position()

        # Classify the input measures and averaging
        self.classifymeasures()
        self.averagemeasures()

        # Calculate average ranging
        for i, uuid in enumerate(self.uuid):
            sum = 0
            for measure in self.classifiedmeasures[i]:
                sum = sum + measure.getarrivaltime()
                # Impossible to do with any absolute temporal reference

    def getpositionusingrssiranging(self, reference1, reference2, prediction=(1, 1)):
        """This method performs the calculate of position using time references"""
        position = Position(x=0.0, y=0.0)

        # Classify the input measures and averaging
        self.classifymeasures()
        self.averagemeasures()

        if len(self.uuid) > 1:
            x1 = reference1.getx()
            y1 = reference1.gety()
            x2 = reference2.getx()
            y2 = reference2.gety()
            rssi1 = self.averagedmeasures[0][1]
            rssi2 = self.averagedmeasures[1][1]
            ranger = RSSIRanger(self.frecuency, gain=self.gain)
            dis1 = ranger.rangedistance(rssi1)
            dis2 = ranger.rangedistance(rssi2)

            # Solve the determination equations
            def equations(p):
                x, y = p
                return (x - x1)**2 + (y - y1)**2 - dis1**2, (x - x2)**2 + (y - y2)**2 - dis2**2

            x, y = fsolve(equations, prediction)

            position.setx(x)
            position.sety(y)
        return position
