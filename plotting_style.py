import numpy as np

import matplotlib.pyplot as plt

y1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 9.1, 9.2, 1.1, 4.5])
y2 = np.array([1.3, 4.4, 2.4, 5.6, 3.4, 0.0, 6.6, 6.8, 6.8])
fig, ax = plt.subplots()
ax = ax.plot(y1, "o--", y2, "x--")
ax.set_title("Plot of the data y1 and y2")
plt.set_xlabel("x axis label")
plt.show()
