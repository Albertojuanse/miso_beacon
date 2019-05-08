"""This file executes a demo of the system"""

from miso_beacon_radiodet.position import Position
from miso_beacon_demo.measures_generator import MeasuresGenerator
from miso_beacon_radiodet.miso_beacon_radiodet_nav.radiolocator import Radiolocator
from miso_beacon_demo import points_monitor
from miso_beacon_model import model_generator

POSITIONS = [
    [51, 49],
    [49, 51]
]


def main():
    """Main execution"""

    for pos in POSITIONS:
        generator1 = MeasuresGenerator(uuid=1, mode="RADIOLOCATOR", rssi=pos[0])
        generator2 = MeasuresGenerator(uuid=2, mode="RADIOLOCATOR", rssi=pos[1])

        radiolocator = Radiolocator(
            [Position(x=0, y=100), Position(x=100, y=100)],
            "CONCURRENT",
            "RHO_RHO",
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
    """

    classmodel, dicmodel = model_generator.createmodel("MODELO_NOMBRE", locatedpositions)

    print(classmodel)
    print(dicmodel)


if __name__ == "__main__":
    main()
