"""This functions allows to calculate real distances or its RSSI values"""

from math import sqrt, pow, pi

C = 299792458
F = 2440000000  # 2400 - 2480 MHz
G = 1  # 2.16 dBi


def calculatedistance(pos1, pos2):
    return sqrt(pow(pos2.getx() - pos1.getx(), 2) + pow(pos2.gety() - pos1.gety(), 2))


def rangedistance(rssi, frecuency=F, gain=G):
    """This function calculates the distance that a signal comes from using its RSSI value"""
    return (C / (4 * pi * frecuency)) * sqrt(gain * pow(10, rssi / 10))
