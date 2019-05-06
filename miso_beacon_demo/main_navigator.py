"""This file executes a demo of the system"""

from miso_beacon_radiodet.position import Position
from miso_beacon_demo.measures_generator import MeasuresGenerator
from miso_beacon_demo.canvas import MyCanvas
from miso_beacon_radiodet.miso_beacon_radiodet_nav.radionavigator import Radionavigator


def main():
    """Main execution"""

    canvas = MyCanvas()

    navigator = Radionavigator(Position(x=0, y=0), [Position(x=200, y=0), Position(x=0, y=200)], canvas)
    navigator.setinitialposition(Position(x=0, y=0))
    navigator.settargetposition(Position(x=100, y=100))
    references = [Position(x=100, y=0), Position(x=0, y=100)]
    navigator.setreferences(references)

    generator1 = MeasuresGenerator(uuid=1, mode="RADIONAVIGATOR")
    generator2 = MeasuresGenerator(uuid=2, mode="RADIONAVIGATOR")

    generator1.start()
    generator2.start()

    navigator.start()

    canvas.start()


if __name__ == "__main__":
    main()
