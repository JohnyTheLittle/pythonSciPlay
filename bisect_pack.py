import math
from math import copysign
"""Bisection method fow root finding"""
def bisect(f,a,b,tol=1e-5):
    fa, fb = f(a), f(b)
    assert not copysign(fa,fb)==fa
    while (b-a)>tol:
        m=(b-a)/2
        fm = f(m)
        if fm == 0:
            return m
        if copysign(fm,fa)==fm:
            a=m
            fa=fm
        else: 
            b=m
        return a

def f(x):
    return (x*x-2*x)*math.exp(3-x)

print(bisect(f,-1,0.4))