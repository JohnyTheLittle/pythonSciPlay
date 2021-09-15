import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import sparse

aplha = 1
x0 = 0
xL = 2
N = 10
x = np.linspace(x0, xL, N+1)
print("x:", x)
h = (xL-x0)/N
print("h:", h)
k = 0.01
steps = 100
print("k", k)
print("steps", steps)
t = np.array([i*k for i in range(steps+1)])
print(f"t: {t}")
r = aplha*k/h**2
print(f"r: {r}")

diag = [1, *(1-2*r for _ in range(N-1)), 1]
abv_diag = [0, *(r for _ in range(N-1))]
blw_diag = [*(r for _ in range(N-1)), 0]
A = sparse.diags([blw_diag, diag, abv_diag], (-1, 0, 1),
                 shape=(N+1, N+1),
                 dtype=np.float64, format="csr")
u = np.zeros((steps+1, N+1), dtype=np.float64)
print(A)
print(u)


def initial_profile(x):
    return 3*np.sin(np.pi*x/2) - 2*x


u[0, :] = initial_profile(x)

for i in range(steps):
    u[i+1, :] = A@u[i, :]

print(u)

X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(T, X, u, cmap="hot")
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.set_zlabel("u")
plt.show()
