"""This class generates Measure objects and serve them to the measures monitor"""

from threading import Thread
import random
import time

from miso_beacon_radiodet.measure import Measure
from miso_beacon_ai.ranging_functions import calculatedistance, calculaterssifordistance
from miso_beacon_demo import feedback_monitor

MODES = ["RADIONAVIGATOR", "RADIOLOCATOR"]


class MeasuresGenerator (Thread):
    
    def __init__(self, timestep, uuid, mode, randomparameters, frequency, gain, targetposition, listeningprobes):
        """Constructor"""
        super().__init__()
        
        # Timestep defines the how much the state machine will wait until next iteration
        self.timestep = timestep
        
        # The UUID identifies the measures as from a certain source
        self.uuid = uuid
        
        # The mode determines the behave of the run method
        self.mode = mode
        
        # The statistical values for gaussian noise modelling
        self.expectedvalue = randomparameters[0]
        self.variance = randomparameters[1]
        
        # Frequency and gain will be important for distance calculations
        self.frequency = frequency
        self.gain = gain

        # Target position is the position of the object that radiolocator wants to locate or the radionavigator's goal
        self.targetposition = targetposition

        # And measurements will be created for an specific set of listening probes with same UUID
        self.listeningprobes = listeningprobes

    def run(self):
        """Overwrite run method with the measures generator behave."""
        # For preventing collisions and simulate a real behave
        time.sleep(random.uniform(0, 1))

        # Stop condition
        run = True
        while run:
            if self.mode == "RADIOLOCATOR":
                # Static source and static device

                # Create a measure for each listening probe with same UUID an enqueue it
                for probe in self.listeningprobes:
                    measure = generaterandomrssimeasurewithtwopositions(self.uuid,
                                                                        self.targetposition,
                                                                        probe.getposition())
                    self.enqueuemeasure(measure, probe)

                # Check stop condition
                feedback_monitor.getcondition().acquire()
                flag = feedback_monitor.isradiolocatoridle()
                feedback_monitor.getcondition().notify()
                feedback_monitor.getcondition().release()
                if flag:
                    run = False

            elif self.mode == "RADIONAVIGATOR":
                # Static source but mobile device
                sourceposition = self.sourceposition
                deviceposition = self.dequeueposition()
                measure = generaterandomrssimeasurewithtwopositions(self.uuid,
                                                                    sourceposition,
                                                                    deviceposition,
                                                                    expectedvalue=self.expectedvalue,
                                                                    variance=self.variance,
                                                                    frequency=self.frequency,
                                                                    gain=1)
                self.enqueuemeasure(measure)

                # Check stop condition
                feedback_monitor.getcondition().acquire()
                flag = feedback_monitor.isradionavegatoridle()
                feedback_monitor.getcondition().notify()
                feedback_monitor.getcondition().release()
                if flag:
                    run = False

            time.sleep(self.timestep)

    def enqueuemeasure(self, measure, probe):
        """This method enqueue a measure in its monitor"""
        probe.getcondition().acquire()
        probe.enqueuemeasure(measure)
        probe.getcondition().notify()
        probe.getcondition().release()

    def dequeueposition(self):
        """This method dequeue a position from its monitor"""
        feedback_monitor.getcondition().acquire()
        if not feedback_monitor.isempty():
            position = feedback_monitor.dequeuepoint()
        else:
            position = feedback_monitor.initialposition
        feedback_monitor.getcondition().notify()
        feedback_monitor.getcondition().release()
        return position


# ------ END OF CLASS -------


# Single measures generation methods
def generaterssimeasurewithtwopositions(uuid,
                                        sourceposition,
                                        deviceposition,
                                        frequency,
                                        gain):
    """This method generate measure with a RSSI value as seen by a device from another point."""
    distance = calculatedistance(sourceposition, deviceposition)
    rssi = calculaterssifordistance(distance, frequency, gain)
    return Measure(uuid, rssi=rssi)


def generaterandomrssimeasurewithtwopositions(uuid,
                                              sourceposition,
                                              deviceposition,
                                              expectedvalue,
                                              variance,
                                              frequency,
                                              gain):
    """This method generate measure with a RSSI value as seen by a device from another point."""
    distance = calculatedistance(sourceposition, deviceposition)
    shift = random.gauss(expectedvalue, variance)
    rssi = calculaterssifordistance(distance, frequency, gain)
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
                                 frequency,
                                 gain):
    """This method generates measures with RSSI that together represent a moving source in certain path."""
    return generaterssimeasurewithtwopositions(uuid,
                                               sourcepath[index],
                                               deviceposition,
                                               frequency,
                                               gain)


def generaterandomrssimeasureswithpath(uuid,
                                       sourcepath,
                                       deviceposition,
                                       index,
                                       expectedvalue,
                                       variance,
                                       frequency,
                                       gain):
    """This method generates random measures that together represent a moving source in certain path."""
    return generaterandomrssimeasurewithtwopositions(uuid,
                                                     sourcepath[index],
                                                     deviceposition,
                                                     expectedvalue,
                                                     variance,
                                                     frequency,
                                                     gain)


def generatearrivaltimemeasurewithpath(uuid, sourcepath, timearrival):
    """This method generates measures with arrival value that together represent a moving source in certain path."""
    return generaterssimeasurewitharrivaltime(uuid, timearrival)


# Feedback measures generation methods
def generaterssimeasurewithfeedback():
    """This function generate a measure"""
    # TODO


