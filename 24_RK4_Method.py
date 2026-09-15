"""
================================================================================
SECTION G: FOURTH-ORDER RUNGE-KUTTA METHOD (RK4)
================================================================================
INTRODUCTION:
RK4 achieves high-order accuracy by taking a weighted average of four slope estimates 
(k1, k2, k3, k4) across sub-intervals.

QUESTION:
Find y(0.2) given dy/dx = y - x with y(0) = 2 and step size h = 0.1 using RK4.

ALGORITHM:
1. Compute k1 = h * f(x, y).
2. Compute k2 = h * f(x + 0.5h, y + 0.5k1).
3. Compute k3 = h * f(x + 0.5h, y + 0.5k2).
4. Compute k4 = h * f(x + h, y + k3).
5. Update state y = y + (k1 + 2*k2 + 2*k3 + k4) / 6.
================================================================================
"""

def f(x, y): 
    return y - x

x, y, h = 0.0, 2.0, 0.1
steps = int(0.2 / h)

for _ in range(steps):
    k1 = h * f(x, y)
    k2 = h * f(x + 0.5*h, y + 0.5*k1)
    k3 = h * f(x + 0.5*h, y + 0.5*k2)
    k4 = h * f(x + h, y + k3)
    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
    x += h

print(f"y(0.2) = {y:.4f}")