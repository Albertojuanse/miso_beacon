from miso_beacon_radiodet.miso_beacon_radiodet_loc.rho_rho_system import RhoRhoSystem
from miso_beacon_radiodet.measure import Measure
from miso_beacon_radiodet.position import Position
mea1 = Measure(uuid=7, rssi=50)
mea2 = Measure(uuid=6, rssi=50)
sys = RhoRhoSystem([mea1, mea2])
sys.classifymeasures()
sys.averagemeasures()
prediction = (-1, 1)
print(sys.getpositionusingrssi(Position(x=0, y=0), Position(x=0, y=2), prediction=prediction).getx(),
      sys.getpositionusingrssi(Position(x=0, y=0), Position(x=0, y=2), prediction=prediction).gety())

from miso_beacon_radiodet.miso_beacon_range.rssi_ranger import RSSIRanger

print(RSSIRanger.rangedistance(50))


