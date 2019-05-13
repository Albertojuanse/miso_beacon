"""This class defines a device capable to calculate a distance using RSSI values"""

from miso_beacon_ai.ranging_functions import rangedistance


class RSSIRanger:

    def __init__(self, frecuency, gain=1):
        """Constructor"""
        self.frecuency = frecuency
        self.gain = gain

    def rangedistance(self, rssi):
        """This method calculates the distance that a signal comes from using its RSSI value"""
        return rangedistance(rssi, self.frecuency, gain=self.gain)
