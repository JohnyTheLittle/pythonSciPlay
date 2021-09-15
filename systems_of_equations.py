import numpy as np
from numpy import linalg
""" 
3x1-2x2+x3=7
x1+x2-2x3=-4
-3x1-2x2+x3=1
"""

A = np.array([[3, -2, 1], [1, 1, -2], [-3, -2, 1]])
b = np.array([7, -4, 1])
x = linalg.solve(A, b)

print(A)
print(b)
print(x)

print("-------")
print(A@x)
