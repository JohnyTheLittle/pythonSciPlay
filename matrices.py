import numpy as np
from numpy import linalg
a = np.eye(3)

print(a.trace())

mat = np.array([[1, 2], [3, 4]])

print(mat)
print("")
print(mat.T)

A = np.array([[1, 2], [3, 4]])
print(A.trace())

print(A[0][0])


def func(a):
    print(a)
    print("yes ama fucking function")


print("MATRIX MULTIPLICATION")
A = np.array([[10, 2.4], [0.4, 4.2]])
B = np.array([[45, 6.9], [8, 8.8]])
print(A)
print("-------")
print(B)
print("-------")
print(A@B)

print("IDENTITY MATRIX")
I=np.eye(2)
print(I)
print(A@I)
print("DETERMINANT")
print(linalg.det(A))
print(linalg.det(I))
print("INVERSE MATRIX")
invA=linalg.inv(A)
print(invA)
print(invA@A)

