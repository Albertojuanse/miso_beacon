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
x.append(x[1] * cos(gyt) * cos(gpt) + y[1] * (cos(gyt) * sin(gpt) * sin(grt) - sin(gyt) * cos(grt)) + z[1] * (cos(gyt) * sin(gpt) * cos(grt) + sin(gyt) * sin(grt)))
y.append(x[1] * sin(gyt) * cos(gpt) + y[1] * (sin(gyt) * sin(gpt) * sin(grt) + cos(gyt) * cos(grt)) + z[1] * (sin(gyt) * sin(gpt) * cos(grt) - cos(gyt) * sin(grt)))
z.append(x[1] * -sin(gpt) + y[1] * cos(gpt) * sin(grt) + z[1] * cos(gpt) * cos(grt))
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
