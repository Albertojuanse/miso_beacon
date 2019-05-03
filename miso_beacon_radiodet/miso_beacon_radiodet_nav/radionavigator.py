"""This class defines any radionavigation system that finds its positions or other devices one"""

from math import asin, sqrt, pow, exp
from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.miso_beacon_range.rssi_ranger import RSSIRanger

from scipy.optimize import fsolve
import time

STATES = ["WAIT", "NO_LOCATED", "LOCATED", "NEW_DATA"]

class Radionavigator:

    def __init__(self):
        """Constructor"""
        self.currentposition = Position()
        self.initialposition = Position()
        self.targetposition = Position()
        self.trajectory = []
        self.route = []
        self.inittime = time.time()

        self.state = STATES[0]

    # Getters and setters
    def getcurrentposition(self):
        """Current position getter"""
        return self.currentposition

    def setcurrentposition(self, position):
        """Current position setter"""
        self.currentposition = position

    def gettargetposition(self):
        """Target position getter"""
        return self.targetposition

    def settargetposition(self, position):
        """Target position setter"""
        self.targetposition = position

    # Route projection
    def projecttoground(self, position):
        """The method 'projects' a position to the ground """
        newposition = Position(x=position.getx(), y=position.gety(), z=0)
        return newposition

    # Journey control
    def initjourney(self, initialposition):
        """This method sets the system to an initial point"""
        self.initialposition = initialposition
        self.state = "NO_LOCATED"
        self.locate()
        self.inittime = time.time()

    def locate(self):
        while self.state != "LOCATED":
            pass

    def isarrived(self, precision=2):
        """This method checks if the current position is near enough to finish position"""
        projectedinitialposition = self.projecttoground(self.initialposition)
        projectedcurrentposition = self.projecttoground(self.currentposition)
        distance = sqrt( pow(projectedinitialposition.getx() - projectedcurrentposition.getx(), 2) +
                         pow(projectedinitialposition.gety() - projectedcurrentposition.gety(), 2) )
        if distance < precision:
            return True
        else:
            return False

