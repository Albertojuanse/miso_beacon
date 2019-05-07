"""This functions are used for creating a graph's model"""

from miso_beacon_model.miso_beacon_model_meta.graph_metamodel import GRAPH_METAMODEL
from miso_beacon_model.model import Model
from miso_beacon_ai.graph_functions import maximazeareawithvertices


def createmodel(name, locations, metamodel=GRAPH_METAMODEL):
    """This function creates a model returns a dictionary object with the model representation"""
    classmodel = Model(name)

    vertices = generatevertices(locations, metamodel)
    for comp in vertices:
        classmodel.addcomponent(comp)

    edges = generateedges(vertices, metamodel)
    for comp in edges:
        classmodel.addcomponent(comp)

    dicmodel = generateclassdic(classmodel)
    return classmodel, dicmodel


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
    return []


def generateclassdic(model):
    """This function creates the model representation descriptive dictionary"""
    return {}
