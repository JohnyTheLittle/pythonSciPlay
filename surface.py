import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
X = np.linspace(-2, 2)
Y = np.linspace(-1, 1)
x, y = np.meshgrid(X, Y)
z = np.sqrt(x**2+y**2)*x
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(x, y, z)
plt.show()
fig = plt.figure()
plt.contour(x,y,z)
plt.show()
