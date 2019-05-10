"""This functions creates differen types of position's paths"""

from miso_beacon_radiodet.position import Position
from miso_beacon_ai.ranging_functions import calculatedistance

from scipy.optimize import fsolve
from math import sqrt


def generatelinepath(initialposition, targetposition, distancestep):
    """This function generates a secuence of positions over a line"""
    if calculatedistance(initialposition, targetposition) == 0.0:
        return [initialposition]
    elif calculatedistance(initialposition, targetposition) <= distancestep:
        return [initialposition, targetposition]

    # 1.- The line between both points is the first equation.
    # 2.- The circle of radius distancestep and center in each point could be the second one, but both solutions of the
    #     system may be too near and so the numeric solver could get the wrong one if previous step is given as clue.
    # 3.- The circle of rising radius distancestep + each_number_of_steps * distance step and center in initial position
    #     is the second equation.
    # 4.- For the first iteration a prediction is needed anyway

    xl1 = initialposition.getx()
    yl1 = initialposition.gety()
    xl2 = targetposition.getx()
    yl2 = targetposition.gety()

    prediction = (xl1, yl1)

    if xl2 > xl1 and yl2 > yl1:
        prediction = (xl1 + distancestep/2, yl1 + distancestep/2)
    elif xl2 > xl1 and yl2 < yl1:
        prediction = (xl1 + distancestep/2, yl1 - distancestep/2)
    elif xl2 < xl1 and yl2 > yl1:
        prediction = (xl1 - distancestep/2, yl1 + distancestep/2)
    elif xl2 < xl1 and yl2 < yl1:
        prediction = (xl1 - distancestep/2, yl1 - distancestep/2)

    currentposition = initialposition
    path = []
    path.append(initialposition)
    stepindex = 1
    while not calculatedistance(currentposition, targetposition) <= distancestep:
        print(calculatedistance(currentposition, targetposition))
        print(stepindex * distancestep)
        xc = initialposition.getx()
        yc = initialposition.gety()

        # Solve the determination equations
        def equations(p):
            x, y = p
            return x * (yl2 - yl1) - y * (xl2 - xl1) - xl1 * (yl2-yl1) + yl1 * (xl2-xl1), \
                   (x - xc) ** 2 + (y - yc) ** 2 - (stepindex * distancestep) ** 2
        x, y = fsolve(equations, prediction)

        position = Position(x=x, y=y)
        path.append(position)
        currentposition = position
        stepindex = stepindex + 1
        prediction = (x, y)
        print(currentposition)
    path.append(targetposition)
    return path
