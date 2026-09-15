"""
================================================================================
SECTION 4: SECANT METHOD
================================================================================
INTRODUCTION:
The Secant Method approximates derivatives using finite differences between two 
initial points, removing the need for an explicit analytical derivative.

QUESTION 2:
Find a root of f(x) = cos(x) - x * e^x = 0 correct to 4 decimal places using 
the Secant Method.

ALGORITHM:
1. Define f(x) = cos(x) - x * e^x.
2. Choose two initial estimates x0 = 0.0 and x1 = 1.0.
3. Compute x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)).
4. Check stopping criterion: If |x2 - x1| < 0.0001, stop.
5. Update x0 = x1 and x1 = x2. Repeat steps 3-4.
================================================================================
"""

import math

def f(x): 
    return math.cos(x) - x * math.exp(x)

x0, x1 = 0.0, 1.0

for i in range(100):
    if abs(f(x1) - f(x0)) < 1e-9:
        break
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    if abs(x2 - x1) < 0.0001:
        x1 = x2
        break
    x0, x1 = x1, x2

print(f"Root = {x1:.4f}")