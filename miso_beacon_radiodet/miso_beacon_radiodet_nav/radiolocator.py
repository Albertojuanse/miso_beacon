"""This class defines any radiolocator system that finds other device position"""

from math import asin, sqrt, pow, exp
from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.miso_beacon_radiodet_loc.rho_rho_system import RhoRhoSystem
from miso_beacon_radiodet.miso_beacon_radiodet_loc.rho_theta_system import RhoThetaSystem
from miso_beacon_radiodet.miso_beacon_radiodet_loc.theta_theta_system import ThetaThetaSystem
from miso_beacon_ai.ranging_functions import calculatedistance
from miso_beacon_demo import measures_monitor
from miso_beacon_demo import points_monitor

import time
from threading import Thread
import random

MEASURE_MODES = ["CONCURRENT", "TEMPORAL"]
SYSTEM_MODES = ["RHO_RHO", "RHO_THETA", "THETA_THETA"]
STATES = ["IDLE", "NO_LOCATED", "LOCATED", "NEW_DATA"]
MAX_MEASURES = 100
MIN_MEASURES_FOR_PRECISION = 10
EVALUATIONS_FOR_PRECISION = 5
PRECISION = 7


class Radiolocator (Thread):

    def __init__(self, positions, measure_mode, system_mode, frecuency, gain,
                 targetpositionprediction=Position(x=1.0, y=1.0)):
        """Constructor"""
        super().__init__()

        self.measures = []
        self.calculatedpositions = []
        self.measurescondition = measures_monitor.getcondition()
        self.targetposition = targetpositionprediction

        self.measure_mode = measure_mode
        self.system_mode = system_mode
        self.positions = positions
        if measure_mode == "CONCURRENT":
            if system_mode == "RHO_RHO":
                self.ranges = []
            elif system_mode == "RHO_THETA":
                self.range = []
                self.angle = 0
            elif system_mode == "THETA_THETA":
                self.angles = []
        elif measure_mode == "TEMPORAL":
            if system_mode == "RHO_RHO":
                self.ranges = []
            elif system_mode == "RHO_THETA":
                self.range = []
                self.angle = 0
            elif system_mode == "THETA_THETA":
                self.angles = []

        self.state = STATES[0]
        self.idle = False
        self.system = None
        self.inittime = time.time()

    # Getters and setters
    def gettargetposition(self):
        """Current position getter"""
        return self.targetposition

    def settargetposition(self, position):
        """Current position setter"""
        self.targetposition = position

    def isidle(self):
        """Idle getter"""
        return self.idle

    def setidle(self, idle):
        """Idle setter"""
        self.idle = idle

    # Route projection
    def projecttoground(self, position):
        """The method 'projects' a position to the ground """
        if position:
            newposition = Position(x=position.getx(), y=position.gety(), z=0)
            return newposition
        else:
            return position

    # Journey control
    def run(self):
        """Overwrite run method with the radiolocator behave"""
        time.sleep(random.uniform(0, 1))

        if self.measure_mode == "CONCURRENT":

            if self.system_mode == "RHO_RHO":
                self.inittime = time.time()
                self.system = RhoRhoSystem(frecuency, gain)

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
                            self.idle = True
                            self.state = "IDLE"
                        else:
                            if self.isnewdata():
                                self.state = "NEW_DATA"
                            else:
                                print("[ERROR]: NO_DATA")
                    time.sleep(0.5)

                print("Target position:", self.targetposition)
                print("Positions measured:")
                for pos in self.calculatedpositions:
                    print(pos.getx(), pos.gety())
                print("Time", time.time() - self.inittime)

                self.measurescondition.acquire()
                measures_monitor.flag_finish = True
                self.measurescondition.notify()
                self.measurescondition.release()

                points_monitor.enqueuepoint(self.targetposition)

            elif self.system_mode == "RHO_THETA":
                self.inittime = time.time()
                self.system = RhoThetaSystem()

            elif self.system_mode == "THETA_THETA":
                self.inittime = time.time()
                self.system = ThetaThetaSystem()

        elif self.measure_mode == "TEMPORAL":

            if self.system_mode == "RHO_RHO":
                self.inittime = time.time()
                self.system = RhoRhoSystem()

            elif self.system_mode == "RHO_THETA":
                self.inittime = time.time()
                self.system = RhoThetaSystem()

            elif self.system_mode == "THETA_THETA":
                self.inittime = time.time()
                self.system = ThetaThetaSystem()

    def isnewdata(self):
        """This method ask if there is new measures available for triggering a new location process"""
        newdata = None

        self.measurescondition.acquire()
        while True:
            newdata = not measures_monitor.isempty()
            if newdata is not None:
                break
            self.measurescondition.wait()
        self.measurescondition.notify()
        self.measurescondition.release()

        return newdata

    def getnewdata(self):
        """This method ask the new measures available for location process"""
        flag = False
        self.measurescondition.acquire()
        while True:
            measure = measures_monitor.dequeuemeasure()
            if measure:
                if len(self.measures) <= MAX_MEASURES:
                    self.measures.append(measure)
                else:
                    self.measures.pop(0)
                    self.measures.append(measure)
                flag = True
                break
            self.measurescondition.wait()
        self.measurescondition.notify()
        self.measurescondition.release()
        return flag

    def locate(self):
        """This method localizes the radionavigator using the measures it gets and offers the target direction"""
        if len(self.measures) > MIN_MEASURES_FOR_PRECISION:
            self.system.setmeasures(self.measures)
            self.targetposition = self.system.getpositionusingrssiranging(self.positions[0],
                                                                          self.positions[1],
                                                                          (self.targetposition.getx() + 1,
                                                                           self.targetposition.gety() + 1
                                                                           )
                                                                          )
            self.calculatedpositions.append(self.targetposition)
            return True
        else:
            return False

    def isprecised(self):
        """This method evaluated if the estimated position is good enough"""
        if len(self.calculatedpositions) > MIN_MEASURES_FOR_PRECISION:
            sum = 0
            lastdistance = 0
            number = len(self.calculatedpositions) - 1
            for i in range(EVALUATIONS_FOR_PRECISION):
                distance = calculatedistance(self.calculatedpositions[number-i-2], self.calculatedpositions[number-i-1])
                sum = sum + (distance - lastdistance)

            if sum < PRECISION:
                return True
            else:
                return False
