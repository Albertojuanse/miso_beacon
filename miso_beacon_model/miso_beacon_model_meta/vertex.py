"""This class defines a vertex of a graph"""


class Vertex:

    def __init__(self, name, position, edges, matrix):
        """Constructor"""
        self.name = name
        self.position = position
        self.edges = edges
        self.matrix = matrix

    def getname(self):
        """Getter of vertex's name"""
        return self.name

    def setname(self, name):
        """Setter of vertex's name"""
        self.name = name

    def getposition(self):
        """Getter of vertex's position"""
        return self.position

    def setposition(self, position):
        """Setter of vertex's position"""
        self.position = position

    def getedges(self):
        """Getter of vertex's edges"""
        return self.edges

    def setedges(self, edges):
        """Setter of vertex's weight"""
        self.edges = edges

    def getmatrix(self):
        """Getter of vertex's matrix"""
        return self.matrix

    def setmatrix(self, matrix):
        """Setter of vertex's matrix"""
        self.matrix = matrix

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.position == other.getposition() and self.name == other.getname()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
