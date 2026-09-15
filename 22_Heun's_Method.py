"""
================================================================================
SECTION E: HEUN'S METHOD
================================================================================
INTRODUCTION:
Heun's Method is a second-order Runge-Kutta technique using intermediate slope estimates 
k1 and k2 to integrate ODEs accurately.

QUESTION:
Find y(0.2) given dy/dx = 2x + y with y(0) = 1 and step size h = 0.1.

ALGORITHM:
1. Compute k1 = f(x, y).
2. Compute k2 = f(x + h, y + h*k1).
3. Advance state: y = y + (h/2) * (k1 + k2).
4. Increment x += h and repeat.
================================================================================
"""

def f(x, y): 
    return 2*x + y

x, y, h = 0.0, 1.0, 0.1
steps = int(0.2 / h)

for _ in range(steps):
    k1 = f(x, y)
    k2 = f(x + h, y + h * k1)
    y = y + (h / 2.0) * (k1 + k2)
    x += h

print(f"y(0.2) = {y:.4f}")