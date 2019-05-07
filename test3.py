from miso_beacon_model.miso_beacon_model_meta.graph_metamodel import GRAPH_METAMODEL

vertex = GRAPH_METAMODEL[0]
from miso_beacon_radiodet.position import Position

positions = [Position(x=10, y=10), Position(x=30, y=90), Position(x=100, y=10), Position(x=70, y=15), Position(x=100, y=100), Position(x=10, y=100), Position(x=50, y=60)]
locations = []
for i, pos in enumerate(positions):
    locations.append((i, pos))

vertices = []
for loc in locations:
    newvertice = vertex(loc[0], loc[1], [], [])
    newvertice.setposition(loc[1])
    vertices.append(newvertice)

from miso_beacon_ai.graph_functions import convexhullgrahamscan

convexhull, vertices, descartedvertices = convexhullgrahamscan(vertices)
print(convexhull)
print(vertices)
print(descartedvertices)