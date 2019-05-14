"""This class defines an edge of a graph"""


class Edge:

    def __init__(self, weight, vertices, matrix, isdirected):
        """Constructor"""
        self.weight = weight
        self.vertices = vertices
        self.matrix = matrix
        self.isdirected = isdirected

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
        return self.isdirected

    def setisdirected(self, isdirected):
        """Setter of isDirected property of edge"""
        self.isdirected = isdirected

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vertices == other.vertices() and self.weight == other.getweight()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
