"""This functions creates differen types of position's paths"""

from miso_beacon_radiodet.position import Position
from miso_beacon_ai.ranging_functions import calculatedistance

from math import pi, cos, sin, atan


def generatelinepath(initialposition, targetposition, steps):
    """This function generates a secuence of positions over a line; it returns steps+1 positions, including initial and
    target points"""

    distancestep = calculatedistance(initialposition, targetposition) / steps
    if calculatedistance(initialposition, targetposition) == 0.0:
        return [initialposition]
    elif calculatedistance(initialposition, targetposition) <= distancestep:
        return [initialposition, targetposition]

    # 1.- The line y = mx + n between both points is the first equation.
    # 2.- If the domain of definition between the final point and the initial point is partitioned into segments of
    #     equal length and the line's equation is evaluated in that set of points the path is obtained.
    # 4.- The domain of definition could be either (yt - yi) or (xt - xi), due to its linearity.

    xi = initialposition.getx()
    yi = initialposition.gety()
    xt = targetposition.getx()
    yt = targetposition.gety()

    m = (yt - yi) / (xt - xi)
    n = -xi * m + yi

    path = []
    for i in range(steps):
        x = xi + i * (xt - xi)/steps
        position = Position(x=x, y=m*x+n)
        print(position)
        path.append(position)

    path.append(targetposition)

    return path


def generatecirclepath(initialposition, centerposition, stepsperrevolution, clockwise=True):
    """This function generates a secuence of positions over a line"""
    radius = calculatedistance(initialposition, centerposition)
    if radius <= 1.0:
        return [initialposition]
    if stepsperrevolution < 2:
        return [initialposition]

    # 1.- The center point defines a vector.
    # 2.- The (x cos θ, y sen θ) vector rotates on it clockwise or counter clockwise from a relative angle that
    #     determines both initial point and center point
    # 3.- The relative angle is arctan (yi-yc)/(xi-xc).

    xi = initialposition.getx()
    yi = initialposition.gety()
    xc = centerposition.getx()
    yc = centerposition.gety()

    anglestep = 2*pi/stepsperrevolution
    offsetangle = atan((yi - yc) / (xi - xc))

    path = []
    for i in range(stepsperrevolution):
        if clockwise:
            x = radius * cos(-i * anglestep + offsetangle) + xc
            y = radius * sin(-i * anglestep + offsetangle) + yc
        else:
            x = radius * cos(i * anglestep + offsetangle) + xc
            y = radius * sin(i * anglestep + offsetangle) + yc

        position = Position(x=x, y=y)
        path.append(position)
    return path
