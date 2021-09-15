import matplotlib.pyplot as plt


def euler(func, t_range, y0, step_size):
    t = [t_range[0]]
    y = [y0]
    i = 0
    print(t)
    print(y0)
    while t[i] < t_range[1]:
        i += 1
        t.append(t[i-1]+step_size)
        y.append(y[i-1]+step_size*func(t[i-1], y[i-1]))
    return t, y


def f(t, y):
    return -0.2*y


t, y = euler(f, (0, 4), 1, 0.1)
print(t)
print(y)
plt.plot(t, y)
plt.show()
