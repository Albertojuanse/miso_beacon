"""This class defines any radionavigation system that finds its positions or other devices one"""

from math import sqrt, pow
from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.miso_beacon_radiodet_loc.rho_rho_system import RhoRhoSystem
from miso_beacon_demo import measures_monitor
from miso_beacon_demo import points_monitor
from miso_beacon_demo import feedback_monitor

import time
from threading import Thread
import random

STATES = ["WAIT", "NO_LOCATED", "LOCATED", "NEW_DATA"]
MAX_MEASURES = 10


class Radionavigator (Thread):

    def __init__(self, position, references, canvas=None):
        """Constructor"""
        super().__init__()
        self.started = True
        self.references = references
        self.currentposition = Position()
        self.initialposition = position
        self.targetposition = None
        self.trajectory = []
        self.route = []
        self.inittime = time.time()
        self.condition = measures_monitor.getcondition()
        self.pointscondition = points_monitor.getcondition()
        self.feedbackcondition = feedback_monitor.getcondition()
        self.measures = []

        self.state = STATES[0]

        if canvas:
            self.canvas = canvas
        else:
            self.canvas = None

        self.feedbackcondition.acquire()
        feedback_monitor.initialposition = self.currentposition
        self.feedbackcondition.notify()
        self.feedbackcondition.release()

    # Getters and setters
    def getcurrentposition(self):
        """Current position getter"""
        return self.currentposition

    def setcurrentposition(self, position):
        """Current position setter"""
        self.currentposition = position

    def gettargetposition(self):
        """Target position getter"""
        return self.targetposition

    def settargetposition(self, position):
        """Target position setter"""
        self.targetposition = position

    def getinitialposition(self):
        """Initial position getter"""
        return self.initialposition

    def setinitialposition(self, position=Position()):
        """Initial position setter"""
        self.initialposition = position

    def getreferences(self):
        """References getter"""
        return self.references

    def setreferences(self, references):
        """References setter"""
        self.references = references

    def isstarted(self):
        """Started flag getter"""
        return self.started

    def setstarted(self, started=True):
        """Started flag setter; True default"""
        self.started = started

    def gettrajectory(self):
        """Getter of trajectory"""
        return self.trajectory

    # Route projection
    def projecttoground(self, position):
        """The method 'projects' a position to the ground """
        if position:
            print("method projected", position.getx(), position.gety())
            newposition = Position(x=position.getx(), y=position.gety(), z=0)
            print(newposition)
            return newposition
        else:
            return position

    # Journey control
    def run(self):
        """Overwrite run method with the state machine of the navigator"""
        time.sleep(random.uniform(0, 1))
        while True:
            print(self.state)
            if self.state == "WAIT":
                if self.started:
                    if self.initjourney():
                        self.pointscondition.acquire()
                        points_monitor.isarrived = False
                        self.pointscondition.notify()
                        self.pointscondition.release()
                        self.feedbackcondition.acquire()
                        feedback_monitor.isarrived = False
                        self.feedbackcondition.notify()
                        self.feedbackcondition.release()
                        self.state = "NEW_DATA"
            elif self.state == "NEW_DATA":
                if self.getnewdata():
                    self.state = "NO_LOCATED"
            elif self.state == "NO_LOCATED":
                if self.locate():
                    if self.currentposition:
                        self.state = "LOCATED"
            elif self.state == "LOCATED":
                print(self.currentposition)
                if self.isarrived():
                    self.started = False
                    self.pointscondition.acquire()
                    points_monitor.isarrived = True
                    self.pointscondition.notify()
                    self.pointscondition.release()
                    self.feedbackcondition.acquire()
                    feedback_monitor.isarrived = True
                    self.feedbackcondition.notify()
                    self.feedbackcondition.release()
                    self.state = "WAIT"
                else:
                    if self.isnewdata():
                        self.state = "NEW_DATA"

    def initjourney(self):
        """This method sets the system to an initial position"""
        self.inittime = time.time()
        self.system = RhoRhoSystem()
        return True

    def targetpath(self):
        """This method calculates the target path that must be done for reaching it"""
        pass

    def locate(self):
        """This method localizes the radionavigator using the measures it gets and offers the target direction"""
        for mea in self.measures:
            print(mea.getrssi(), mea.getuuid())
        for ref in self.references:
            print(ref.getx(), ref.gety())
        print(self.currentposition, self.initialposition, self.targetposition)
        self.system.setmeasures(self.measures)
        self.currentposition = self.system.getpositionusingrssiranging(self.references[0],
                                                                       self.references[1],
                                                                       (self.currentposition.getx() + 1,
                                                                        self.currentposition.gety() + 1
                                                                        )
                                                                       )
        self.trajectory.append(self.currentposition)
        if self.canvas and len(self.measures) > 2:
            self.canvas.paint(self.currentposition.getx(), self.currentposition.gety())
        self.pointscondition.acquire()
        points_monitor.enqueuepoint(Position(x=self.currentposition.getx(), y=self.currentposition.gety()))
        self.pointscondition.notify()
        self.pointscondition.release()
        self.feedbackcondition.acquire()
        feedback_monitor.enqueuepoint(Position(x=self.currentposition.getx(), y=self.currentposition.gety()))
        self.feedbackcondition.notify()
        self.feedbackcondition.release()
        return True

    def isnewdata(self):
        """This method ask if there is new measures available for triggering a new location process"""
        self.condition.acquire()
        newdata = measures_monitor.isempty()
        self.condition.notify()
        self.condition.release()
        return not newdata

    def getnewdata(self):
        """This method ask the new measures available for location process"""
        flag = False
        self.condition.acquire()
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
            self.condition.wait()
        self.condition.notify()
        self.condition.release()
        print(len(self.measures))
        return flag

    def isarrived(self, precision=1):
        """This method checks if the current position is near enough to finish position"""
        projectedcurrentposition = self.projecttoground(self.currentposition)
        projectedtargetposition = self.projecttoground(self.targetposition)
        print("projected", projectedtargetposition, projectedcurrentposition)
        if projectedcurrentposition and projectedtargetposition:
            distance = sqrt(pow(projectedtargetposition.getx() - projectedcurrentposition.getx(), 2) +
                            pow(projectedtargetposition.gety() - projectedcurrentposition.gety(), 2))
            print(distance)
            if distance < precision and self.state == "LOCATED" and len(self.measures) > 10:
                return True
            else:
                return False
        else:
            return False
