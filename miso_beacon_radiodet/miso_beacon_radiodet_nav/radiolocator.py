"""This class defines any radiolocator system that finds other device position"""

from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.miso_beacon_radiodet_loc.rho_rho_system import RhoRhoSystem
from miso_beacon_radiodet.miso_beacon_radiodet_loc.rho_theta_system import RhoThetaSystem
from miso_beacon_radiodet.miso_beacon_radiodet_loc.theta_theta_system import ThetaThetaSystem
from miso_beacon_ai.ranging_functions import calculatedistance
from miso_beacon_demo import feedback_monitor

from threading import Thread
import time
import random

MEASURE_MODES = ["CONCURRENT", "TEMPORAL"]
SYSTEM_MODES = ["RHO_RHO", "RHO_THETA", "THETA_THETA"]
STATES = ["IDLE", "NO_LOCATED", "LOCATED", "NEW_DATA"]
MAX_MEASURES = 100
MIN_MEASURES_FOR_PRECISION = 10
EVALUATIONS_FOR_PRECISION = 5
PRECISION = 7


class Radiolocator (Thread):

    def __init__(self, probes, measure_mode, system_mode, frecuency, gain, targetpositionprediction):
        """Constructor"""
        super().__init__()

        # Probes will stack the measures and its own position
        self.probes = probes

        # Measure_mode determines if the probes will be treated at the same time or not
        self.measure_mode = measure_mode

        # System mode is the radiodetermination paradigme in use: rho rho, rho theta or theta theta
        self.system_mode = system_mode

        # Frecuency and gain are needed for propagation phenomena
        self.frecuency = frecuency
        self.gain = gain

        # A target prediction is needed for numerical methods
        self.targetpositionprediction = targetpositionprediction

        # State machine's init state and stop condition
        self.state = STATES[0]
        self.idle = False

        # Instance parameters
        # Measures list for probes measurements
        self.measures = []
        # Path's positions list
        self.calculatedpositions = []
        self.targetposition = targetpositionprediction

        if measure_mode == "CONCURRENT":
            if system_mode == "RHO_RHO":
                self.system = RhoRhoSystem(self.frecuency, self.gain)
            elif system_mode == "RHO_THETA":
                pass
            elif system_mode == "THETA_THETA":
                pass
        elif measure_mode == "TEMPORAL":
            if system_mode == "RHO_RHO":
                self.system = RhoRhoSystem(self.frecuency, self.gain)
            elif system_mode == "RHO_THETA":
                pass
            elif system_mode == "THETA_THETA":
                pass

        self.inittime = None

    # Getters and setters
    def getprobes(self):
        """Probes getter"""
        return self.probes

    def setprobes(self, probes):
        """Probes setter"""
        self.probes = probes

    def getmeasuremode(self):
        """Measure mode getter"""
        return self.measure_mode

    def setmeasuremode(self, measure_mode):
        """Measure mode setter"""
        self.measure_mode = measure_mode

    def getsystemmode(self):
        """System mode getter"""
        return self.system_mode

    def setsystemmode(self, system_mode):
        """System mode setter"""
        self.system_mode = system_mode

    def getfrecuency(self):
        """Frecuency getter"""
        return self.frecuency

    def setfrecuency(self, frecuency):
        """Frecuency setter"""
        self.frecuency = frecuency

    def getgain(self):
        """Gain getter"""
        return self.gain

    def setgain(self, gain):
        """Gain setter"""
        self.gain = gain

    def gettargetposition(self):
        """Target position getter"""
        return self.targetposition

    def settargetposition(self, position):
        """Target position setter"""
        self.targetposition = position

    def gettargetpositionprediction(self):
        """Target position prediction getter"""
        return self.targetpositionprediction

    def settargetpositionprediction(self, positionprediction):
        """Target position prediction setter"""
        self.targetpositionprediction = positionprediction

    def isidle(self):
        """Idle flag getter"""
        return self.idle

    def setidle(self, idle):
        """Idle flag setter"""
        self.idle = idle

    def getcalculatedpositions(self):
        """Calculated position list getter; if radiolocator is not idle it returns None"""
        if self.idle:
            return self.calculatedpositions
        else:
            return None

    # Route projection
    @staticmethod
    def projecttoground(position):
        """The method 'projects' a position to the ground """
        if position:
            newposition = Position(x=position.getx(), y=position.gety(), z=0)
            return newposition
        else:
            return position

    # Journey control
    def run(self):
        """Overwrite run method with the radiolocator behave"""
        # For preventing collisions and simulate a real behave
        time.sleep(random.uniform(0, 1))

        if self.measure_mode == "CONCURRENT":
            # If it is concurrent mode, each probe is located and evaluated at the same time
            # Every probe is turn on
            for probe in self.probes:
                probe.getcondition.acquire()
                probe.setflagon(True)
                probe.getcondition.notify()
                probe.getcondition.release()

            # Start execution time
            self.inittime = time.time()

            # State machine; from state to state if a method is satisfied
            while not self.idle:
                print(self.state)
                if self.state == "IDLE":
                    if self.isnewdata():
                        self.state = "NEW_DATA"
                elif self.state == "NEW_DATA":
                    if self.getnewdata():
                        self.state = "NO_LOCATED"
                elif self.state == "NO_LOCATED":
                    if self.locate():
                        self.state = "LOCATED"
                    elif self.isnewdata():
                        self.state = "NEW_DATA"
                elif self.state == "LOCATED":
                    if self.isprecised():
                        # Stop condition
                        self.idle = True
                        self.state = "IDLE"
                    else:
                        if self.isnewdata():
                            self.state = "NEW_DATA"
                        else:
                            print("[ERROR]: NO_DATA; redirecting to NO_LOCATED")
                            self.state = "NO_LOCATED"
                time.sleep(0.5)

            # Results in console
            print("Target position:", self.targetposition)
            print("Positions measured:")
            for pos in self.calculatedpositions:
                print(pos)
            print("Time of execution:", time.time() - self.inittime)

            # Ask probes to stop taking measures
            for probe in self.probes:
                probe.getcondition.acquire()
                probe.setflagon(False)
                probe.getcondition.notify()
                probe.getcondition.release()

            # Ask measure generators to stop
            feedback_monitor.getcondition().acquire()
            feedback_monitor.setradiolocatoridle(self.idle)
            feedback_monitor.getcondition().notify()
            feedback_monitor.getcondition().release()

        elif self.measure_mode == "TEMPORAL":
            # If it is concurrent mode, each probe is located and evaluated one after another
            pass

        # At this point someone must ask for self.gettargetposition()

    def isnewdata(self):
        """This method checks if there is new measures available for triggering a new location process"""
        # Check if there is measures in any queue
        newdata = False
        for probe in self.probes:
            probe.getcondition().acquire()
            newdata = newdata or probe.isempty()
            probe.getcondition().notify()
            probe.getcondition().release()

        return newdata

    def getnewdata(self):
        """This method get from the queue the new measures available for location process"""
        # Ask probes for measures, but if there is no room for the new ones, delete oldest one
        flag = False
        for probe in self.probes:
            probe.getcondition().acquire()
            measure = probe.dequeuemeasure()
            # dequeue measure method returns None if the queue is empty
            if measure:
                flag = True
                if len(self.measures) <= MAX_MEASURES:
                    self.measures.append(measure)
                else:
                    self.measures.pop(0)
                    self.measures.append(measure)
            probe.getcondition().notify()
            probe.getcondition().release()
        return flag

    def locate(self):
        """This method localizes the radionavigator using the measures it gets and offers the target direction"""
        # Only if there is a minimum of measures calculations will be tried
        if len(self.measures) > MIN_MEASURES_FOR_PRECISION:

            # Depending on the system used the treatment of the measures will be different
            if self.measure_mode == "CONCURRENT":
                if self.system_mode == "RHO_RHO":

                    # In concurrent rho rho mode, every measure is given to the system and it calculates the position
                    self.system.setmeasures(self.measures)
                    self.targetposition = self.system.getpositionusingrssiranging(self.probes[0].getposition(),
                                                                                  self.probes[0].getposition(),
                                                                                  self.targetposition
                                                                                  )
                    self.calculatedpositions.append(self.targetposition)

                elif self.system_mode == "RHO_THETA":
                    pass
                elif self.system_mode == "THETA_THETA":
                    pass
            elif self.measure_mode == "TEMPORAL":
                if self.system_mode == "RHO_RHO":
                    pass
                elif self.system_mode == "RHO_THETA":
                    pass
                elif self.system_mode == "THETA_THETA":
                    pass

            # If everything successful return True
            return True
        else:
            return False

    def isprecised(self):
        """This method evaluated if the estimated position is good enough"""
        # Only if there is a minimum of measures calculations will be tried
        if len(self.calculatedpositions) > MIN_MEASURES_FOR_PRECISION:
            # Do a pondered average of lasts measures
            sum = 0
            lastdistance = 0
            number = len(self.calculatedpositions) - 1
            for i in range(EVALUATIONS_FOR_PRECISION):
                distance = calculatedistance(self.calculatedpositions[number - i - 2],
                                             self.calculatedpositions[number - i - 1])
                sum = sum + (distance - lastdistance)
                lastdistance = distance

            if sum < PRECISION:
                return True
            else:
                return False
        else:
            return False
