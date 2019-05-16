"""This file executes a demo of the system"""

from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.probe import Probe
from miso_beacon_demo.measures_generator import MeasuresGenerator
from miso_beacon_radiodet.miso_beacon_radiodet_nav.radiolocator import Radiolocator
from miso_beacon_model import model_generator

import time

# Demo configuration parameters
TARGET_POSITIONS = [  # Number of calculations
    Position(x=60.0, y=20.0),
    Position(x=60.0, y=60.0),
    Position(x=20.0, y=60.0),
    Position(x=20.0, y=20.0),
]
C = 299792458  # Speed of light
F = 2440000000  # 2400 - 2480 MHz
G = 1  # 2.16 dBi

# Measure generators configuration parameters
PROBES_POSITIONS = [  # Positions of device probes
    Position(x=0.0, y=0.0),
    Position(x=0.0, y=100.0),
]
MEASURE_TIMESTEP = 1
UUID = [  # Same length than PROBES_POSITIONS or greater
    10,
    20,
    30,
    40,
    50,
]
GENERATOR_MODES = ["RADIONAVIGATOR", "RADIOLOCATOR"]
GAUSSIAN_NOISE_STATISTICS = (0, 1) # Average and standard deviation for gaussian noise
# Radiolocator configuration parameters
MEASURE_MODES = ["CONCURRENT", "TEMPORAL"]
SYSTEM_MODES = ["RHO_RHO", "RHO_THETA", "THETA_THETA"]


def main():
    """Main execution"""

    # Each iteration will radiodetermine a position
    locatedpositions = []

    # Probes are needed by the devices as a source of mesurements
    probes = []
    for pos in PROBES_POSITIONS:
        probes.append(Probe(pos))

    for i, pos in enumerate(TARGET_POSITIONS):
        generators = []
        for j, probe in enumerate(probes):
            generator = MeasuresGenerator(
                MEASURE_TIMESTEP,
                UUID[j],
                GENERATOR_MODES[1],
                GAUSSIAN_NOISE_STATISTICS,
                F,
                G,
                pos,
                [probe]
            )
            generators.append(generator)

        radiolocator = Radiolocator(
            probes,
            MEASURE_MODES[0],
            SYSTEM_MODES[0],
            F,
            G,
            Position(x=pos.getx() + 1, y=pos.gety() + 1)
        )

        for generator in generators:
            generator.start()
        radiolocator.start()
        radiolocator.join()
        for generator in generators:
            generator.join()

        locatedpositions.append((i, radiolocator.getcalculatedpositions()))

    """

    locatedpositions = [(0, Position(x=10, y=10)),
                        (1, Position(x=30, y=90)),
                        (2, Position(x=100, y=10)),
                        (3, Position(x=70, y=15)),
                        (4, Position(x=100, y=100)),
                        (5, Position(x=10, y=100)),
                        (6, Position(x=50, y=60))
                        ]
    """
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
