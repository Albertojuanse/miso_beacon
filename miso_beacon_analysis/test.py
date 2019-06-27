"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import pi, cos, sin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [0, 1]
y = [0, 1]
z = [0, 1]

gyt = 1
gpt = 0
grt = 0
"""

""" 
x.append(x[1] * cos(gyt) * cos(gpt) + y[1] * (cos(gyt) * sin(gpt) * sin(grt) - sin(gyt) * cos(grt)) + z[1] * (cos(gyt) * sin(gpt) * cos(grt) + sin(gyt) * sin(grt)))
y.append(x[1] * sin(gyt) * cos(gpt) + y[1] * (sin(gyt) * sin(gpt) * sin(grt) + cos(gyt) * cos(grt)) + z[1] * (sin(gyt) * sin(gpt) * cos(grt) - cos(gyt) * sin(grt)))
z.append(x[1] * -sin(gpt) + y[1] * cos(gpt) * sin(grt) + z[1] * cos(gpt) * cos(grt))
"""
"""
x.append(x[1] * cos(gyt) * cos(gpt) + y[1] * (cos(gyt) * sin(gpt) * sin(grt) - sin(gyt) * cos(grt)) + z[1] * (cos(gyt) * sin(gpt) * cos(grt) + sin(gyt) * sin(grt)))
y.append(x[1] * sin(gyt) * cos(gpt) + y[1] * (sin(gyt) * sin(gpt) * sin(grt) + cos(gyt) * cos(grt)) + z[1] * (sin(gyt) * sin(gpt) * cos(grt) - cos(gyt) * sin(grt)))
z.append(x[1] * -sin(gpt) + y[1] * cos(gpt) * sin(grt) + z[1] * cos(gpt) * cos(grt))

print(x[2])
print(y[2])
print(z[2])

ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
"""






"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import pi, cos, sin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

P = [(-2.22, 0.00, 0.00),
     (-2.22, 0.25, 0.00),
     (-2.22, 0.13, 0.00),
     (0.00, 0.00, 0.00),
     (0.00, 0.25, 0.00),
     (0.00, 0.13, 0.00),
     (-1.11, 0.00, 0.00),
     (-1.11, 0.25, 0.00),
     (-1.11, 0.13, 0.00),
     (-1.67, 0.00, 0.00),
     (-1.67, 0.25, 0.00),
     (-1.67, 0.13, 0.00),
     (-1.95, 0.00, 0.00),
     (-1.95, 0.25, 0.00),
     (-1.95, 0.13, 0.00),
     (-1.39, 0.00, 0.00),
     (-1.39, 0.25, 0.00),
     (-1.39, 0.13, 0.00),
     (-0.56, 0.00, 0.00),
     (-0.56, 0.25, 0.00),
     (-0.56, 0.13, 0.00),
     (-0.83, 0.00, 0.00),
     (-0.83, 0.25, 0.00),
     (-0.83, 0.13, 0.00),
     (-0.28, 0.00, 0.00),
     (-0.28, 0.25, 0.00),
     (-0.28, 0.13, 0.00),]

for p in P:
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])

print(x)
print(y)
print(z)

ax.scatter(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
"""





"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import pi, cos, sin
import sys
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

grid = [(-4.66, -3.05, 0.00),
     (-4.66, 0.56, 0.00),
     (-4.66, -1.25, 0.00),
     (-4.66, -2.15, 0.00),
     (-4.66, -2.60, 0.00),
     (-4.66, -1.70, 0.00),
     (-4.66, -0.34, 0.00),
     (-4.66, -0.79, 0.00),
     (-4.66, 0.11, 0.00),
     (1.43, -3.05, 0.00),
     (1.43, 0.56, 0.00),
     (1.43, -1.25, 0.00),
     (1.43, -2.15, 0.00),
     (1.43, -2.60, 0.00),
     (1.43, -1.70, 0.00),
     (1.43, -0.34, 0.00),
     (1.43, -0.79, 0.00),
     (1.43, 0.11, 0.00),
     (-1.62, -3.05, 0.00),
     (-1.62, 0.56, 0.00),
     (-1.62, -1.25, 0.00),
     (-1.62, -2.15, 0.00),
     (-1.62, -2.60, 0.00),
     (-1.62, -1.70, 0.00),
     (-1.62, -0.34, 0.00),
     (-1.62, -0.79, 0.00),
     (-1.62, 0.11, 0.00),
     (-3.14, -3.05, 0.00),
     (-3.14, 0.56, 0.00),
     (-3.14, -1.25, 0.00),
     (-3.14, -2.15, 0.00),
     (-3.14, -2.60, 0.00),
     (-3.14, -1.70, 0.00),
     (-3.14, -0.34, 0.00),
     (-3.14, -0.79, 0.00),
     (-3.14, 0.11, 0.00),
     (-3.90, -3.05, 0.00),
     (-3.90, 0.56, 0.00),
     (-3.90, -1.25, 0.00),
     (-3.90, -2.15, 0.00),
     (-3.90, -2.60, 0.00),
     (-3.90, -1.70, 0.00),
     (-3.90, -0.34, 0.00),
     (-3.90, -0.79, 0.00),
     (-3.90, 0.11, 0.00),
     (-4.28, -3.05, 0.00),
     (-4.28, 0.56, 0.00),
     (-4.28, -1.25, 0.00),
     (-4.28, -2.15, 0.00),
     (-4.28, -2.60, 0.00),
     (-4.28, -1.70, 0.00),
     (-4.28, -0.34, 0.00),
     (-4.28, -0.79, 0.00),
     (-4.28, 0.11, 0.00),
     (-3.52, -3.05, 0.00),
     (-3.52, 0.56, 0.00),
     (-3.52, -1.25, 0.00),
     (-3.52, -2.15, 0.00),
     (-3.52, -2.60, 0.00),
     (-3.52, -1.70, 0.00),
     (-3.52, -0.34, 0.00),
     (-3.52, -0.79, 0.00),
     (-3.52, 0.11, 0.00),
     (-2.38, -3.05, 0.00),
     (-2.38, 0.56, 0.00),
     (-2.38, -1.25, 0.00),
     (-2.38, -2.15, 0.00),
     (-2.38, -2.60, 0.00),
     (-2.38, -1.70, 0.00),
     (-2.38, -0.34, 0.00),
     (-2.38, -0.79, 0.00),
     (-2.38, 0.11, 0.00),
     (-2.76, -3.05, 0.00),
     (-2.76, 0.56, 0.00),
     (-2.76, -1.25, 0.00),
     (-2.76, -2.15, 0.00),
     (-2.76, -2.60, 0.00),
     (-2.76, -1.70, 0.00),
     (-2.76, -0.34, 0.00),
     (-2.76, -0.79, 0.00),
     (-2.76, 0.11, 0.00),
     (-2.00, -3.05, 0.00),
     (-2.00, 0.56, 0.00),
     (-2.00, -1.25, 0.00),
     (-2.00, -2.15, 0.00),
     (-2.00, -2.60, 0.00),
     (-2.00, -1.70, 0.00),
     (-2.00, -0.34, 0.00),
     (-2.00, -0.79, 0.00),
     (-2.00, 0.11, 0.00),
     (-0.09, -3.05, 0.00),
     (-0.09, 0.56, 0.00),
     (-0.09, -1.25, 0.00),
     (-0.09, -2.15, 0.00),
     (-0.09, -2.60, 0.00),
     (-0.09, -1.70, 0.00),
     (-0.09, -0.34, 0.00),
     (-0.09, -0.79, 0.00),
     (-0.09, 0.11, 0.00),
     (-0.85, -3.05, 0.00),
     (-0.85, 0.56, 0.00),
     (-0.85, -1.25, 0.00),
     (-0.85, -2.15, 0.00),
     (-0.85, -2.60, 0.00),
     (-0.85, -1.70, 0.00),
     (-0.85, -0.34, 0.00),
     (-0.85, -0.79, 0.00),
     (-0.85, 0.11, 0.00),
     (-1.24, -3.05, 0.00),
     (-1.24, 0.56, 0.00),
     (-1.24, -1.25, 0.00),
     (-1.24, -2.15, 0.00),
     (-1.24, -2.60, 0.00),
     (-1.24, -1.70, 0.00),
     (-1.24, -0.34, 0.00),
     (-1.24, -0.79, 0.00),
     (-1.24, 0.11, 0.00),
     (-0.47, -3.05, 0.00),
     (-0.47, 0.56, 0.00),
     (-0.47, -1.25, 0.00),
     (-0.47, -2.15, 0.00),
     (-0.47, -2.60, 0.00),
     (-0.47, -1.70, 0.00),
     (-0.47, -0.34, 0.00),
     (-0.47, -0.79, 0.00),
     (-0.47, 0.11, 0.00),
     (0.67, -3.05, 0.00),
     (0.67, 0.56, 0.00),
     (0.67, -1.25, 0.00),
     (0.67, -2.15, 0.00),
     (0.67, -2.60, 0.00),
     (0.67, -1.70, 0.00),
     (0.67, -0.34, 0.00),
     (0.67, -0.79, 0.00),
     (0.67, 0.11, 0.00),
     (0.29, -3.05, 0.00),
     (0.29, 0.56, 0.00),
     (0.29, -1.25, 0.00),
     (0.29, -2.15, 0.00),
     (0.29, -2.60, 0.00),
     (0.29, -1.70, 0.00),
     (0.29, -0.34, 0.00),
     (0.29, -0.79, 0.00),
     (0.29, 0.11, 0.00),
     (1.05, -3.05, 0.00),
     (1.05, 0.56, 0.00),
     (1.05, -1.25, 0.00),
     (1.05, -2.15, 0.00),
     (1.05, -2.60, 0.00),
     (1.05, -1.70, 0.00),
     (1.05, -0.34, 0.00),
     (1.05, -0.79, 0.00),
     (1.05, 0.11, 0.00)]

measures = {
    "measurePosition1":
        {"measurePosition" : (0.00, 0.00, 0.00),
         "measures": (34.69133, 34.69133, 49.00281, 54.98206)
         },
    "measurePosition2":
        {"measurePosition": (1.43, -0.38, 0.00),
         "measures": (43.6738, 38.92432, 38.92432, 38.92432, 38.92432)
         },
    "measurePosition3":
        {"measurePosition": (-2.81, -3.05, 0.00),
         "measures": (38.92432, 38.92432, 38.92432, 61.69088)
         },
    "measurePosition4":
        {"measurePosition": (-4.66, 0.56, 0.00),
         "measures": (27.55631, 24.55958, 27.55631)
         }
}


def euclideandistance(p1, p2):
    res = pow(
        pow(p2[0] - p1[0], 2) +
        pow(p2[1] - p1[1], 2) +
        pow(p2[2] - p1[2], 2),
        0.5
    )
    return res


minarg = sys.float_info.max
minargPos = (0, 0, 0)

for x in grid:

    ax.scatter(x[0], x[1], x[2], color='k')

    sum = 0
    for measurePositionKey in measures:
        measurePosition = measures[measurePositionKey]["measurePosition"]
        rSum = 0
        rSumIndex = 0
        for measure in measures[measurePositionKey]["measures"]:
            rSum += measure
            rSumIndex += 1
        r = rSum / rSumIndex
        sum += (euclideandistance(x, measurePosition) - r) ** 2

        u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
        xs = np.cos(u) * np.sin(v) * r/100 + measurePosition[0]
        ys = np.sin(u) * np.sin(v) * r/100 + measurePosition[1]
        zs = np.cos(v) * 0 + measurePosition[2]
        ax.plot_wireframe(xs, ys, zs, color="r")

    ax.text(x[0], x[1], x[2], s=str(sum), fontdict={'size': 6},)

    if sum < minarg:
        minarg = sum
        minargPos = x


ax.scatter(minargPos[0], minargPos[1], minargPos[2], 'g')
print(minargPos)

ax.scatter(-4.66, -3.05, 0.00, 'r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()

"""






from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import pi, cos, sin
import sys
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

grid = [(0.0, 0.0, 0.0),
        (0.0, 0.25, 0.0),
        (0.0, 0.5, 0.0),
        (0.0, 0.75, 0.0),
        (0.0, 1.0, 0.0),
        (0.25, 0.0, 0.0),
        (0.25, 0.25, 0.0),
        (0.25, 0.5, 0.0),
        (0.25, 0.75, 0.0),
        (0.25, 1.0, 0.0),
        (0.5, 0.0, 0.0),
        (0.5, 0.25, 0.0),
        (0.5, 0.5, 0.0),
        (0.5, 0.75, 0.0),
        (0.5, 1.0, 0.0),
        (0.75, 0.0, 0.0),
        (0.75, 0.25, 0.0),
        (0.75, 0.5, 0.0),
        (0.75, 0.75, 0.0),
        (0.75, 1.0, 0.0),
        (1.0, 0.0, 0.0),
        (1.0, 0.25, 0.0),
        (1.0, 0.5, 0.0),
        (1.0, 0.75, 0.0),
        (1.0, 1.0, 0.0)]

measures = {
    "measurePosition1":
        {"measurePosition": (0.0, 0.0, 0.0),
         "measures": (1.8, 1.8)
         },
    "measurePosition2":
        {"measurePosition": (0.0, 1.0, 0.0),
         "measures": (1.8, 1.8)
         },
    "measurePosition3":
        {"measurePosition": (1.0, 0.0, 0.0),
         "measures": (1.8, 1.8)
         },
    "measurePosition4":
        {"measurePosition": (1.0, 1.0, 0.0),
         "measures": (1.8, 1.8)
         }
}


def euclideandistance(p1, p2):
    res = pow(
        pow(p2[0] - p1[0], 2) +
        pow(p2[1] - p1[1], 2) +
        pow(p2[2] - p1[2], 2),
        0.5
    )
    return res


minarg = sys.float_info.max
minargPos = (0, 0, 0)

for x in grid:

    ax.scatter(x[0], x[1], x[2], color='r')

    sum = 0
    for measurePositionKey in measures:
        measurePosition = measures[measurePositionKey]["measurePosition"]
        rSum = 0
        rSumIndex = 0
        for measure in measures[measurePositionKey]["measures"]:
            rSum += measure
            rSumIndex += 1
        r = rSum / rSumIndex
        sum += (euclideandistance(x, measurePosition) - r) ** 2

        ax.set_aspect('equal')
        """

        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        xs = r * np.outer(np.cos(u), np.sin(v)) + measurePosition[0]
        ys = r * np.outer(np.sin(u), np.sin(v)) + measurePosition[1]
        zs = 0 * np.outer(np.ones(np.size(u)), np.cos(v)) + measurePosition[2]

        ax.plot_surface(xs, ys, zs, rstride=4, cstride=4, color='b', linewidth=0, alpha=0.1)
        """
    ax.text(x[0], x[1], x[2], s=str(sum), fontdict={'size': 6},)

    if sum < minarg:
        minarg = sum
        minargPos = x



ax.scatter(minargPos[0], minargPos[1], minargPos[2], 'g')
print(minargPos)
print(minarg)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
