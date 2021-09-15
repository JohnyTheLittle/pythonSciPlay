import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2, 2)
Y = np.linspace(-2, 2)
x, y = np.meshgrid(X, Y)

t = x**2+y**2
z = np.cos(2*np.pi*t)*np.exp(-t)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(x,y,z, cmap="binary_r")

plt.show()

fig = plt.figure()
plt.contour(x,y,z)
plt.show()
