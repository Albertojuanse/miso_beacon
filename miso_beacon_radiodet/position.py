"""This class defines a single point in the space"""

from math import sqrt, pow, pi, sin, cos, acos, atan


class Position:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Constructor"""
        self.x = x
        self.y = y
        self.z = z

    # Cartesian getters and setters
    def setx(self, x):
        """X coordinate setter"""
        self.x = x

    def getx(self):
        """X coordinate getter"""
        return self.x

    def sety(self, y):
        """Y coordinate setter"""
        self.y = y

    def gety(self):
        """Y coordinate getter"""
        return self.y

    def setz(self, z):
        """Z coordinate setter"""
        self.z = z

    def getz(self):
        """Z coordinate getter"""
        return self.z

    # Polar getters and setters
    def setrho(self, rho):
        """Rho coordinate setter"""
        # Get current phi value
        phi = 0.0
        if self.x > 0 and self.y >= 0:
            phi = atan(self.y / self.x)
        elif self.x == 0 and self.y > 0:
            phi = pi/2
        elif self.x < 0:
            phi = atan(self.y / self.x) + pi
        elif self.x == 0 and self.y < 0:
            phi = 3*pi/2
        elif self.x > 0 and self.y < 0:
            phi = atan(self.y / self.x) + 2*pi

        # Set new rho value
        self.x = rho * cos(phi)
        self.y = rho * sin(phi)

    def getrho(self):
        """Rho coordinate getter"""
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def setphi(self, phi):
        """Phi coordinate setter"""
        # Get current rho value
        rho = sqrt(pow(self.x, 2) + pow(self.y, 2))

        # Set new phi value
        self.x = rho * cos(phi)
        self.y = rho * sin(phi)

    def getphi(self):
        """Phi coordinate getter"""
        phi = 0.0
        if self.x > 0 and self.y >= 0:
            phi = atan(self.y / self.x)
        elif self.x == 0 and self.y > 0:
            phi = pi/2
        elif self.x < 0:
            phi = atan(self.y / self.x) + pi
        elif self.x == 0 and self.y < 0:
            phi = 3*pi/2
        elif self.x > 0 and self.y < 0:
            phi = atan(self.y / self.x) + 2*pi
        return phi

    # Spherical getters and setters
    def setrad(self, rad):
        """Radial coordinate setter"""
        # Get current inclination and azimuth value
        if self.x == 0 and self.y == 0 and self.z == 0:
            inc = acos(self.z / sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)))
        else:
            inc = 0.0
        if self.z == 0:
            azi = 0
        else:
            azi = atan(self.y / self.z)

        # Set new radial value
        self.x = rad * sin(inc) * cos(azi)
        self.y = rad * sin(inc) * sin(azi)
        self.z = rad * cos(inc)

    def getrad(self):
        """Radial coordinate getter"""
        return sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    def setinc(self, inc):
        """Inclination coordinate setter"""
        # Get current azimuth and radial value
        rad = sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
        if self.z == 0:
            azi = 0
        else:
            azi = atan(self.y / self.z)

        # Set new inclination value
        self.x = rad * sin(inc) * cos(azi)
        self.y = rad * sin(inc) * sin(azi)
        self.z = rad * cos(inc)

    def getinc(self):
        """Inclination coordinate getter"""
        if self.x == 0 and self.y == 0 and self.z == 0:
            return 0.0
        else:
            return acos(self.z / sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)))

    def setazi(self, azi):
        """Azimuth coordinate setter"""
        # Get current inclination and radial value
        rad = sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
        if self.x == 0 and self.y == 0 and self.z == 0:
            inc = acos(self.z / sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)))
        else:
            inc = 0.0

        # Set new azimuth value
        self.x = rad * sin(inc) * cos(azi)
        self.y = rad * sin(inc) * sin(azi)
        self.z = rad * cos(inc)

    def getazi(self):
        """Azimuth coordinate getter"""
        if self.z == 0:
            return 0.0
        else:
            return atan(self.y / self.z)

    # Location setters
    def setcartesianlocation(self, x, y, z=0):
        """Cartesian location setter; (x, y, z) is required"""
        self.setx(x)
        self.sety(y)
        self.setz(z)

    def setcilindricallocation(self, rho, phi, z=0):
        """Cilindrical location setter; (rho, phi, z) is required"""
        self.setrho(rho)
        self.setphi(phi)
        self.setz(z)

    def setsphericallocation(self, rad, inc, azi):
        """Cilindrical location setter; (rho, phi, z) is required"""
        self.setrad(rad)
        self.setinc(inc)
        self.setazi(azi)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
