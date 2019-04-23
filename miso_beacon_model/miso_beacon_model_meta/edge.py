"""This class defines an edge of a graph"""


class Edge:

    def __init__(self, weight, vertices, matrix, isdirected):
        """Constructor"""
        self.weight = weight
        self.vertices = vertices
        self.matrix = matrix
        self.isDirected = isdirected

    def getweight(self):
        """Getter of edge's weight"""
        return self.weight

    def setweight(self, weight):
        """Setter of edge's weight"""
        self.weight = weight

    def getvertices(self):
        """Getter of edge's vertices"""
        return self.vertices

    def setvertices(self, vertices):
        """Setter of edge's vertices"""
        self.vertices = vertices

    def getmatrix(self):
        """Getter of edge's matrix"""
        return self.matrix

    def setmatrix(self, matrix):
        """Setter of edge's matrix"""
        self.matrix = matrix

    def getisdirected(self):
        """Getter of isDirected property of edge"""
        return self.isDirected

    def setisdirected(self, isdirected):
        """Setter of isDirected property of edge"""
        self.isDirected = isdirected
