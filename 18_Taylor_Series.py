"""
================================================================================
SECTION A: TAYLOR'S SERIES METHOD
================================================================================
INTRODUCTION:
Taylor's Series method solves initial value ODEs by expanding y(x) in a power 
series about x0 using high-order analytical derivatives.

QUESTION:
Find y(0.1) given dy/dx = x^2 + y^2 with initial condition y(0) = 1 up to third-order derivatives.

ALGORITHM:
1. Compute derivatives at (0, 1): y' = 1, y'' = 2, y''' = 8.
2. Evaluate Taylor series expansion: y(h) = y0 + h*y' + (h^2/2!)*y'' + (h^3/3!)*y'''.
3. Output y(0.1).
================================================================================
"""

x0, y0, h = 0.0, 1.0, 0.1
y1 = y0 + h*(1.0) + (h**2 / 2.0)*(2.0) + (h**3 / 6.0)*(8.0)

print(f"y(0.1) = {y1:.4f}")