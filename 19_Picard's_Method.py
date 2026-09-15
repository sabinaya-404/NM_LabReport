"""
================================================================================
SECTION B: PICARD'S METHOD OF SUCCESSIVE APPROXIMATION
================================================================================
INTRODUCTION:
Picard's method computes successive integral approximations to solve differential 
equations iteratively: y_{n}(x) = y_0 + INT[f(t, y_{n-1}(t)) dt].

QUESTION:
Find y(0.1) given dy/dx = x + y^2 with y(0) = 0 using the third approximation.

ALGORITHM:
1. Integrate y0(x) = 0 -> y1(x) = x^2 / 2.
2. Integrate y1(x) -> y2(x) = x^2 / 2 + x^5 / 20.
3. Evaluate y3(0.1) using polynomial evaluation.
================================================================================
"""

x = 0.1
y3 = (x**2) / 2.0 + (x**5) / 20.0

print(f"y(0.1) = {y3:.6f}")