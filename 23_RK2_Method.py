"""
================================================================================
SECTION F: SECOND-ORDER RUNGE-KUTTA METHOD (RK2)
================================================================================
INTRODUCTION:
RK2 evaluates slope estimates at interval midpoint boundaries to eliminate second-order 
truncation error terms.

QUESTION:
Find y(0.4) given dy/dx = x^2 - y with y(0) = 1 and h = 0.2 using RK2.

ALGORITHM:
1. Calculate k1 = h * f(x, y).
2. Calculate k2 = h * f(x + h, y + k1).
3. Compute state update: y = y + 0.5 * (k1 + k2).
4. Update x += h.
================================================================================
"""

def f(x, y): 
    return x**2 - y

x, y, h = 0.0, 1.0, 0.2
steps = int(0.4 / h)

for _ in range(steps):
    k1 = h * f(x, y)
    k2 = h * f(x + h, y + k1)
    y = y + 0.5 * (k1 + k2)
    x += h

print(f"y(0.4) = {y:.4f}")