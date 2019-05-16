"""This class generates Measure objects and serve them to the measures monitor"""

from threading import Thread
import random
import time

from miso_beacon_radiodet.measure import Measure
from miso_beacon_radiodet.position import Position
from miso_beacon_ai.ranging_functions import calculatedistance, calculaterssifordistance
from miso_beacon_demo import measures_monitor
from miso_beacon_demo import feedback_monitor


class MeasuresGenerator (Thread):

    def __init__(self,
                 timestep=1,
                 uuid=0,
                 mode="RADIONAVIGATOR",
                 randomparameters=(0, 1),
                 frecuency=2440000000,
                 gain=1,
                 targetpositionprediction = Position(x=50.0, y=50.0),
                 sourceposition = Position(x=50.0, y=50.0)):
        """Constructor"""
        super().__init__()
        self.timestep = timestep
        self.uuid = uuid
        self.mode = mode
        self.expectedvalue = randomparameters[0]
        self.variance = randomparameters[1]
        self.frecuency = frecuency
        self.gain = gain
        self.condition = measures_monitor.getcondition()
        self.feedbackcondition = feedback_monitor.getcondition()
        self.targetpositionprediction = targetpositionprediction
        self.sourceposition = sourceposition

    def run(self):
        """Overwrite run method"""
        time.sleep(random.uniform(0, 1))
        while True:
            if self.mode == "RADIOLOCATOR":
                # Static source and static device

                self.feedbackcondition.acquire()
                deviceposition = feedback_monitor.dequeuepoint()
                self.feedbackcondition.notify()
                self.feedbackcondition.release()
                if not deviceposition:
                    deviceposition = self.targetpositionprediction
                measure = generaterandomrssimeasurewithtwopositions(self.uuid,
                                                                    self.sourceposition,
                                                                    deviceposition)
                self.enqueuemeasure(measure)
            elif self.mode == "RADIONAVIGATOR":
                # Static source but mobile device
                sourceposition = self.sourceposition
                deviceposition = self.dequeueposition()
                measure = generaterandomrssimeasurewithtwopositions(self.uuid,
                                                                    sourceposition,
                                                                    deviceposition,
                                                                    expectedvalue=self.expectedvalue,
                                                                    variance=self.variance,
                                                                    frecuency=self.frecuency,
                                                                    gain=1)
                self.enqueuemeasure(measure)

            # Check stop condition
            self.condition.acquire()
            flag = measures_monitor.flag_finish
            self.condition.notify()
            self.condition.release()
            if flag:
                break

            time.sleep(self.timestep)

    def enqueuemeasure(self, measure):
        """This method enqueue a measure in its monitor"""
        self.condition.acquire()
        measures_monitor.enqueuemeasure(measure)
        self.condition.notify()
        self.condition.release()

    def dequeueposition(self):
        """This method dequeue a position from its monitor"""
        self.feedbackcondition.acquire()
        if not feedback_monitor.isempty():
            position = feedback_monitor.dequeuepoint()
        else:
            position = feedback_monitor.initialposition
        self.feedbackcondition.notify()
        self.feedbackcondition.release()
        return position


# ------ END OF CLASS -------


# Single measures generation methods
def generaterssimeasurewithtwopositions(uuid,
                                        sourceposition,
                                        deviceposition,
                                        frecuency=2440000000,
                                        gain=1):
    """This method generate measure with a RSSI value as seen by a device from another point."""
    distance = calculatedistance(sourceposition, deviceposition)
    rssi = calculaterssifordistance(distance, frecuency, gain)
    return Measure(uuid, rssi=rssi)


def generaterandomrssimeasurewithtwopositions(uuid,
                                              sourceposition,
                                              deviceposition,
                                              expectedvalue=0,
                                              variance=1.0,
                                              frecuency=2440000000,
                                              gain=1):
    """This method generate measure with a RSSI value as seen by a device from another point."""
    distance = calculatedistance(sourceposition, deviceposition)
    shift = random.gauss(expectedvalue, variance)
    rssi = calculaterssifordistance(distance, frecuency, gain)
    return Measure(uuid, rssi=rssi + shift)


def generaterssimeasurewithrssi(uuid, rssi):
    """This method generate measure using a rssi value."""
    return Measure(uuid, rssi=rssi)


def generaterssimeasurewitharrivaltime(uuid, timearrival):
    """This method generate measure using a signal's time arrival value."""
    return Measure(uuid, arrivaltime=timearrival)


# Path measures generation methods n
def generaterssimeasureswithpath(uuid,
                                 sourcepath,
                                 deviceposition,
                                 index,
                                 frecuency=2440000000,
                                 gain=1):
    """This method generates measures with RSSI that together represent a moving source in certain path."""
    return generaterssimeasurewithtwopositions(uuid,
                                               sourcepath[index],
                                               deviceposition,
                                               frecuency=frecuency,
                                               gain=gain)


def generaterandomrssimeasureswithpath(uuid,
                                       sourcepath,
                                       deviceposition,
                                       index,
                                       expectedvalue=0,
                                       variance=1.0,
                                       frecuency=2440000000,
                                       gain=1):
    """This method generates random measures that together represent a moving source in certain path."""
    return generaterandomrssimeasurewithtwopositions(uuid,
                                                     sourcepath[index],
                                                     deviceposition,
                                                     expectedvalue=expectedvalue,
                                                     variance=variance,
                                                     frecuency=frecuency,
                                                     gain=gain)


def generatearrivaltimemeasurewithpath(uuid, sourcepath, timearrival):
    """This method generates measures with arrival value that together represent a moving source in certain path."""
    return generaterssimeasurewitharrivaltime(uuid, timearrival)


# Feedback measures generation methods
def generaterssimeasurewithfeedback():
    """This function generate a measure"""


