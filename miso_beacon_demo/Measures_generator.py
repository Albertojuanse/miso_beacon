"""This class generates Measure objects and serve them to the measures monitor"""

from threading import Thread, Condition
import random
import time

from miso_beacon_radiodet.measure import Measure
from miso_beacon_demo import measures_monitor


class MeasuresGenerator (Thread):

    def __init__(self, timestep=1, uuid=0, mode="RADIONAVIGATOR"):
        """Constructor"""
        super().__init__()
        self.timestep = timestep
        self.uuid = uuid
        self.mode = mode
        self.condition = measures_monitor.getcondition()

        # Navigator parameters
        self.navigatorcount = 0
        self.navigatormaxrssi = 100

    def run(self):
        """Overwrite run method"""
        time.sleep(random.uniform(0, 1))
        while True:
            if self.mode == "RADIOLOCATOR":
                shift = random.gauss(0, 1) * 1.5
                measure = Measure(self.uuid, rssi=50 + shift)
                self.condition.acquire()
                measures_monitor.enqueuemeasure(measure)
                self.condition.notify()
                self.condition.release()
                time.sleep(1)
            elif self.mode == "RADIONAVIGATOR":

                shift = random.gauss(0, 1) * 1.5
                measure = Measure(self.uuid, rssi=self.navigatormaxrssi - self.navigatorcount + shift)
                self.condition.acquire()
                measures_monitor.enqueuemeasure(measure)
                self.condition.notify()
                self.condition.release()
                self.navigatorcount = self.navigatorcount + 1
                time.sleep(1)

