import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x-2)*np.exp(3-x)

x=np.linspace(-0.5, 31.0)
y=f(x)
plt.plot(x, y)

lines = plt.plot(x, f(x), x**2, x, 1-x)

plt.show()
