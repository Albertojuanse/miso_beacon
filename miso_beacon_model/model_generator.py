"""This functions are used for creating a graph's model"""

from miso_beacon_model.miso_beacon_model_meta.graph_metamodel import GRAPH_METAMODEL
from miso_beacon_ai.graph_functions import convexhullgrahamscan

from math import sqrt, pow


def createmodel(name, locations, metamodel=GRAPH_METAMODEL):
    """This function creates a model returns a dictionary object with the model representation"""
    model = [name]

    # Create components
    vertices = generatevertices(locations, metamodel)
    edges = generateedges(vertices, metamodel)

    # Complete information of components
    vertices, edges = generatecompletegraph(vertices, edges)

    # Compose the class object Model
    for comp in vertices:
        model.append(comp)
    for comp in edges:
        model.append(comp)

    dicmodel = generateclassdic(name, vertices, edges)
    return model, dicmodel


def generatevertices(locations, metamodel):
    """This function creates the 'vertices' type components of the model representation"""
    vertices = []
    for loc in locations:
        newvertice = metamodel[0](loc[0], loc[1], [], [])
        newvertice.setposition(loc[1])
        vertices.append(newvertice)
    return vertices


def generateedges(vertices, metamodel):
    """This function creates the 'edge' type components of the model representation"""
    # Get the convex hull of the vertices set, which for an small graph must be an ccw ordered set of the vertices
    convexhull, vertices, descartedvertices = convexhullgrahamscan(vertices)
    if not descartedvertices == []:
        for vertex in descartedvertices:
            print("DESCARTED_VERTEX:", vertex.getposition().getx(), vertex.getposition().gety())
    else:
        print("NOT DESCARTED VERTICES")

    # Generate the edges connecting the ordered set of vertex
    edges = []
    for i in range(len(convexhull) - 1):
        v1 = convexhull[i]
        v2 = convexhull[i + 1]
        distance = sqrt(
            pow(v2.getposition().getx() - v1.getposition().getx(), 2) +
            pow(v2.getposition().gety() - v1.getposition().gety(), 2)
        )
        newedge = metamodel[1](distance, [v1, v2], [], None)
        edges.append(newedge)
    # Last one is generated manually, since array is not "circular" and so last element is not connected with first one
    v1 = convexhull[len(convexhull) -1]
    v2 = convexhull[0]
    distance = sqrt(
        pow(v2.getposition().getx() - v1.getposition().getx(), 2) +
        pow(v2.getposition().gety() - v1.getposition().gety(), 2)
    )
    newedge = metamodel[1](distance, [v1, v2], [], None)
    edges.append(newedge)

    return edges


def generatecompletegraph(vertices, edges):
    """This function completes the vertices and edges sets with the information needed"""
    return vertices, edges


def generateclassdic(name, vertices, edges):
    """This function creates the model representation descriptive dictionary"""
    dic = {
        "model name": name,
        "vertices": {},
        "edges": {}
    }

    for i, vertex in enumerate(vertices):
        dic["vertices"].update({
            str(i): {
                "name": vertex.getname(),
                "position": str(vertex.getposition()),
            }
        })

    for i, edge in enumerate(edges):
        verticesdic = {}
        for j, vertex in enumerate(edge.getvertices()):
            verticesdic.update({
                str(j): {
                    "name": vertex.getname(),
                    "position": str(vertex.getposition()),
                }
            })

        dic["edges"].update({
            str(i): {
                "vertices": verticesdic,
                "weight": str(edge.getweight()),
                "isDirected": str(edge.getisdirected())
            }
        })

    return dic
