"""This class defines a single point in the space"""


class Position:

    def __init__(self, x=0, y=0, z=0):
        """Constructor"""
        self.x = x
        self.y = y
        self.z = z

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @property
    def z(self):
        return self.z