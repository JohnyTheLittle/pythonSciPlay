import matplotlib.pyplot as plt
import numpy as np


def predator_prey_system(t, y):
    return np.array([5*y[0]-0.1*y[0]*y[1], 0.1*y[1]*y[0]-6*y[1]])


p = np.linspace(0, 100, 25)
w = np.linspace(0, 100, 25)
P, W = np.meshgrid(p, w)

dp, dw = predator_prey_system(0, np.array([P, W]))

print(dp)
print(dw)

fig, ax = plt.subplots()

ax.quiver(P, W, dp, dw)
ax.set_xlabel("P")
ax.set_ylabel("W")
plt.show()
