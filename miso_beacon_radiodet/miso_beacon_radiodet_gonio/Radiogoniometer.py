"""This class defines a device that measures the angle of a radio transmission comes from"""

from math import asin, sqrt, pow

c = 299792458


class Radiogoniometer:

    def __init__(self, probes=None):
        """Constructor"""
        if probes:
            self.probes = probes
        else:
            self.probes = []

    def getprobes(self):
        """Probes getter"""
        return self.probes

    def setprobes(self, probes):
        """Probes setter"""
        self.probes = probes

    def gettimelapseangle(self):
        angle = 0
        probe1 = self.probes[0]
        probe2 = self.probes[1]
        if probe1 and probe2:
            if not probe1.nomeasures and not probe2.nomeasures:
                time1 = probe1.getarrivaltime()
                time2 = probe2.getarrivaltime()
                pos1 = probe1.getposition()
                pos2 = probe1.getposition()
                distance = sqrt(pow((pos1.getx() - pos2.getx()),2) +
                                pow((pos1.gety() - pos2.gety()),2) +
                                pow((pos1.getz() - pos2.getz()),2))
                timestep = time2 - time1
                angle = asin((c * timestep) / distance)
        return angle
