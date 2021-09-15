import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def f(t, y):
    return -0.2*y


t_range = (0, 5)
T0 = np.array([50.])

print(T0)


def true_solution(t):
    return 50.*np.exp(-0.2*t)


sol = integrate.solve_ivp(f, t_range, T0, max_step=0.001)
t_vals = sol.t
T_vals = sol.y[0, :]
print("t:", t_vals)
print("T:", T_vals)

fig, (ax1, ax2) = plt.subplots(1, 2, tight_layout=True)
ax1.plot(t_vals, T_vals)

plt.show()