"""This class defines a probe's measure"""

from math import sqrt, pow, pi, sin, cos, acos, atan


class Measure:

    def __init__(self, uuid, arrivaltime=0, rssi=0):
        """Constructor"""
        self.uuid = uuid
        self.arrivaltime = arrivaltime
        self.rssi = rssi

    # UUID getter and setter
    def getuuid(self):
        return self.uuid

    def setuuid(self, uuid):
        self.uuid = uuid

    # Arrival time getter and setter
    def getarrivaltime(self):
        return self.arrivaltime

    def setarrivaltime(self, arrivaltime):
        self.arrivaltime = arrivaltime

    # RSSI value getter and setter
    def getrssi(self):
        return self.rssi

    def setrssi(self, rssi):
        self.rssi = rssi
