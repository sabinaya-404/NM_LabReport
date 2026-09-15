"""
================================================================================
SECTION A: LINEAR INTERPOLATION
================================================================================
INTRODUCTION:
Linear Interpolation estimates unknown intermediate values between two known data 
points by fitting a straight line between them.

QUESTION:
Estimate the population in the year 1995 given the known census data 
(1990, 20000) and (2000, 25000).

ALGORITHM:
1. Define target x = 1995 and known points (x0, y0) = (1990, 20000), (x1, y1) = (2000, 25000).
2. Apply linear formula: y = y0 + [(y1 - y0) / (x1 - x0)] * (x - x0).
3. Output the estimated value y.
================================================================================
"""

x0, y0 = 1990, 20000
x1, y1 = 2000, 25000
x = 1995

y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
print(f"Estimated Population in 1995 = {y:.2f}")