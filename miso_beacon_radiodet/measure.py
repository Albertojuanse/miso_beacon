"""This class defines a probe's measure"""


class Measure:

    def __init__(self, uuid, arrivaltime=None, rssi=None):
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

    def __str__(self):
        if self.rssi and not self.arrivaltime:
            return "[" + str(self.uuid) + "] measure: rssi value " + str(self.rssi)
        if not self.rssi and self.arrivaltime:
            return "[" + str(self.uuid) + "] measure: time arrival value " + str(self.arrivaltime)
        if self.rssi and self.arrivaltime:
            string = "[" + str(self.uuid) + "] measure: time arrival value " +\
                     str(self.arrivaltime) + " and rssi value " + str(self.rssi)
            return string

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.arrivaltime == other.getarrivaltime() \
                   and self.rssi == other.getrssi() \
                   and self.uuid == other.getuuid()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
