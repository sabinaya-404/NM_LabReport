"""
================================================================================
SECTION C: NUMERICAL INTEGRATION (TRAPEZOIDAL, SIMPSON'S 1/3 & 3/8)
================================================================================
INTRODUCTION:
Numerical integration methods approximate definite integrals by partitioning 
the region under curves into geometric shapes (trapezoids or parabolas).

QUESTION:
Evaluate the definite integral of f(x) = ln(x) dx from a = 1 to b = 4 using n = 6 
subintervals with Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rules.

ALGORITHM:
1. Compute step size h = (b - a) / n.
2. Evaluate node values y_i = f(x_i) for i = 0 to n.
3. Apply Trapezoidal: (h/2) * [y0 + 2*sum(middle) + yn].
4. Apply Simpson's 1/3: (h/3) * [y0 + 4*sum(odd) + 2*sum(even) + yn].
5. Apply Simpson's 3/8: (3h/8) * [y0 + 3(y1+y2+y4+y5) + 2*y3 + y6].
================================================================================
"""

import math

def f(x): 
    return math.log(x)

a, b, n = 1.0, 4.0, 6
h = (b - a) / n
x = [a + i*h for i in range(n + 1)]
y = [f(val) for val in x]

trap = (h / 2.0) * (y[0] + 2*sum(y[1:-1]) + y[-1])
simp13 = (h / 3.0) * (y[0] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-1:2]) + y[-1])
simp38 = (3 * h / 8.0) * (y[0] + 3*y[1] + 3*y[2] + 2*y[3] + 3*y[4] + 3*y[5] + y[6])

print(f"Trapezoidal Result = {trap:.4f}")
print(f"Simpson's 1/3 Result = {simp13:.4f}")
print(f"Simpson's 3/8 Result = {simp38:.4f}")