import sympy
import numpy as np
import matplotlib.pyplot as plt
x = sympy.symbols('x')
f = (x**2-2*x)*sympy.exp(3-x)
fp = sympy.simplify(sympy.diff(f))
print(fp)
F = sympy.integrate(fp, x)
print(F)


def f(x):
    return x*(x-2)*np.exp(3-x)


def zero(x):
    return 0 * x


x = np.linspace(0.0, 2.2)
y = f(x)
y1 = 0
plt.plot(x, y, zero(x))
plt.show()
