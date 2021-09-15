class Polynomial:
    """Basic polynomial class"""

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"Polynomial({repr(self.coeffs)})"

    def __call__(self, x):
        return sum(coeff*x**i for i, coeff
                   in enumerate(self.coeffs))

    def differentiate(self):
        coeffs = [i*c for i, c in enumerate(self.coeffs[1:], start=1)]
        return Polynomial(coeffs)

    def integrate(self, constant=0):
        """Integrate the polynimial, returning the integral"""
        coeffs = [float(constant)]
        coeffs += [c/i for i, c in enumerate(self.coeffs, start=1)]
        return Polynomial(coeffs)


P = Polynomial([8, 6, 5, 4, 3])
print(P.__call__(2))
print(P)
DP=P.differentiate().differentiate()
print(DP)
print(DP.integrate().integrate())

a = [1,2,3,4,5,6,7,8,9,10]
b=[(value+1)/number for value, number in enumerate(a)]
print(b)