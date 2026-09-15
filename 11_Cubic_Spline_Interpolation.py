"""
================================================================================
SECTION F: CUBIC SPLINE INTERPOLATION
================================================================================
INTRODUCTION:
Cubic Spline interpolation constructs smooth piecewise cubic polynomials between 
data points with continuous first and second derivatives.

QUESTION:
Fit a natural cubic spline to data points (1,1), (2,5), (3,11), (4,19) and estimate y at x = 2.5.

ALGORITHM:
1. Pass dataset arrays to scipy.interpolate.CubicSpline.
2. Set boundary condition bc_type='natural' (second derivative = 0 at boundaries).
3. Evaluate spline function at target value x = 2.5.
================================================================================
"""

from scipy.interpolate import CubicSpline

x_val = [1, 2, 3, 4]
y_val = [1, 5, 11, 19]

cs = CubicSpline(x_val, y_val, bc_type='natural')
result = cs(2.5)

print(f"y(2.5) = {result:.4f}")