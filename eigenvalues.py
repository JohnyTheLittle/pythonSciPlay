import numpy as np
from numpy import linalg

A = np.array([[3, -1, 4], [-1, 0, -1], [4, -1, 2]])

v, B = linalg.eig(A)

print(A)

print("eigenvalues", v)

print("columns are eigenvectors", B)


for i in range(3):
    print("lambda",i,"  ",v[i])

print(linalg.norm(v))
print(B[1:])