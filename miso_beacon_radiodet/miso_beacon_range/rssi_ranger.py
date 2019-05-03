"""This class defines a system capable to calculate a distance using RSSI values"""

from math import sqrt, pow, pi

c = 299792458
f = 2440000000  # 2400 - 2480 MHz
g = 1  # 2.16 dBi


class RSSIRanger:

    def __init__(self):
        """Constructor"""

    @staticmethod
    def rangerawdistance(rssi):
        """This method calculates the distance that a signal comes from using its RSSI value"""
        return (c / (4 * pi * f)) * sqrt(g * pow(10, rssi/10))
