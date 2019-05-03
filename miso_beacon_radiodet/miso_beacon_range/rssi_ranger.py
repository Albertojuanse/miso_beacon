"""This class defines a system capable to calculate a distance using RSSI values"""

from math import sqrt, pow, pi

C = 299792458
F = 2440000000  # 2400 - 2480 MHz
G = 1  # 2.16 dBi


class RSSIRanger:

    def __init__(self):
        """Constructor"""

    @staticmethod
    def rangerawdistance(rssi):
        """This method calculates the distance that a signal comes from using its RSSI value"""
        return (C / (4 * pi * F)) * sqrt(G * pow(10, rssi/10))
