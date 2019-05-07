
"""miso_beacon_radiodet_gonio"""

from miso_beacon_radiodet.position import Position
from miso_beacon_radiodet.probe import Probe
from miso_beacon_radiodet.measure import Measure
from miso_beacon_radiodet.miso_beacon_radiodet_gonio.radiogoniometer import Radiogoniometer
punto1 = Position(x=0, y=0, z=0)
punto2 = Position(x=1, y=0, z=0)
probe1 = Probe(punto1)
probe2 = Probe(punto2)
measure1 = Measure(1, 0)
measure2 = Measure(2, 3.33564095e-9)
probe1.addmeasure(measure1)
probe2.addmeasure(measure2)
probes = [probe1, probe2]
radiogoniometro = Radiogoniometer(probes)
angle = radiogoniometro.gettimelapseangle()
if angle == 1.5707618581188734:
    print("miso_beacon_radiodet_gonio: SUCCESS")
else:
    print("miso_beacon_radiodet_gonio: FAILED")
