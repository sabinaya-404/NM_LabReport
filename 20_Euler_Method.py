"""
================================================================================
SECTION C: EULER'S METHOD
================================================================================
INTRODUCTION:
Euler's Method is a first-order numerical procedure for solving ODEs using tangent 
steps y_{n+1} = y_n + h * f(x_n, y_n).

QUESTION:
Find y(2.0) given dy/dx = y - x^2 + 1 with initial condition y(0) = 0.5 and h = 0.2.

ALGORITHM:
1. Set initial values x = 0.0, y = 0.5, step size h = 0.2.
2. Compute step count N = target / h.
3. Update y = y + h * f(x, y) and x = x + h iteratively.
================================================================================
"""

def f(x, y): 
    return y - x**2 + 1.0

x, y, h = 0.0, 0.5, 0.2
steps = int(2.0 / h)

for _ in range(steps):
    y = y + h * f(x, y)
    x = round(x + h, 2)

print(f"y(2.0) = {y:.4f}")