"""
================================================================================
SECTION 2: NEWTON-RAPHSON METHOD
================================================================================
INTRODUCTION:
The Newton-Raphson Method uses linear approximation via tangent lines to find 
roots rapidly using the iterative derivative formula x_{n+1} = x_n - f(x_n)/f'(x_n).

QUESTION 5
Find a real root of the equation f(x) = x * e^x - 2 = 0 correct to 4 decimal 
places using the Newton-Raphson Method.

ALGORITHM:
1. Define f(x) = x * e^x - 2 and its derivative f'(x) = e^x * (x + 1).
2. Choose an initial guess x0 = 1.0.
3. Compute the next approximation: x_new = x - f(x) / f'(x).
4. Check convergence: If |x_new - x| < tolerance (0.00005), stop.
5. Update x = x_new and repeat from step 3.
================================================================================
"""

import math

def f(x): 
    return x * math.exp(x) - 2

def df(x): 
    return math.exp(x) * (x + 1)

x = 1.0
for i in range(100):
    xn = x - f(x) / df(x)
    if abs(xn - x) < 0.00005:
        x = xn
        break
    x = xn

print(f"Root = {x:.4f}")