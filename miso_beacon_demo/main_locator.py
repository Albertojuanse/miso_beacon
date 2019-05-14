"""This file executes a demo of the system"""

from miso_beacon_radiodet.position import Position
from miso_beacon_demo.measures_generator import MeasuresGenerator
from miso_beacon_radiodet.miso_beacon_radiodet_nav.radiolocator import Radiolocator
from miso_beacon_demo import points_monitor
from miso_beacon_model import model_generator

import time

POSITIONS = [
    [51, 49],
    [49, 51]
]


def main():
    """Main execution"""
    """
    for pos in POSITIONS:
        generator1 = MeasuresGenerator(
            timestep=1,
            uuid=1,
            mode="RADIOLOCATOR",
            randomparameters=(0, 1),
            frecuency=2440000000,
            gain=1)
        generator2 = MeasuresGenerator(
            timestep=1,
            uuid=1,
            mode="RADIOLOCATOR",
            randomparameters=(0, 1),
            frecuency=2440000000,
            gain=1)

        radiolocator = Radiolocator(
            [Position(x=0, y=100), Position(x=100, y=100)],
            "CONCURRENT",
            "RHO_RHO",
            2440000000,
            1
            targetpositionprediction=Position(x=50.0, y=50.0)
        )

        generator1.start()
        generator2.start()
        radiolocator.start()
        radiolocator.join()
        generator1.join()
        generator2.join()

    locatedpositions = []
    index = 0
    while not points_monitor.isempty():
        locatedpositions.append((index, points_monitor.dequeuepoint()))
        index = index + 1
    """

    locatedpositions = [(0, Position(x=10, y=10)),
                        (1, Position(x=30, y=90)),
                        (2, Position(x=100, y=10)),
                        (3, Position(x=70, y=15)),
                        (4, Position(x=100, y=100)),
                        (5, Position(x=10, y=100)),
                        (6, Position(x=50, y=60))
                        ]

    name = "id" + \
           str(time.localtime().tm_year) + \
           str(time.localtime().tm_mon) + \
           str(time.localtime().tm_mday) + \
           str(time.localtime().tm_hour) + \
           str(time.localtime().tm_min) + \
           str(time.localtime().tm_sec)

    classmodel, dicmodel = model_generator.createmodel(name, locatedpositions)

    print(classmodel)
    print(dicmodel)


if __name__ == "__main__":
    main()
