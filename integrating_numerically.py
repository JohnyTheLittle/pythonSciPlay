from scipy import integrate
import numpy as np


def erf_integrand(t):
    return np.exp(-t**2)


val_quad, err_quad = integrate.quad(erf_integrand, -1.0, 1.0)
print(val_quad)


def trapezium(f, a, b, n_steps):
    h = (b-a)/n_steps
    x_vals = np.arange(a+h, b, h)
    y_vals = f(x_vals)
    print(y_vals)
    return 0.5*h*(f(a)+f(b)+2.*np.sum(y_vals))



print(trapezium(erf_integrand, -1.0, +1.0, 100000000))

print(np.arange(1.0, 10.0, 0.5))
