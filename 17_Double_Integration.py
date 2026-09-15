"""
================================================================================
SECTION E: NUMERICAL DOUBLE INTEGRATION
================================================================================
INTRODUCTION:
Numerical Double Integration extends 1D quadrature rules across 2D spatial grids 
to calculate surface areas and volumes.

QUESTION:
Evaluate double integral of f(x, y) = 1 / (x + y) dx dy over domain [1,2] x [1,2] 
with step sizes h = k = 0.5 using 2D Composite Trapezoidal rule.

ALGORITHM:
1. Generate node vectors x = [1.0, 1.5, 2.0] and y = [1.0, 1.5, 2.0].
2. Evaluate function grid f(x_i, y_j).
3. Construct weight matrix W (corners=1, edges=2, interior=4).
4. Calculate integral = (h * k / 4) * sum(grid * weights).
================================================================================
"""

import numpy as np

def f(x, y): 
    return 1.0 / (x + y)

h = k = 0.5
x = [1.0, 1.5, 2.0]
y = [1.0, 1.5, 2.0]

grid = np.array([[f(xi, yi) for xi in x] for yi in y])
weights = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

integral = (h * k / 4.0) * np.sum(grid * weights)
print(f"Double Integral Result = {integral:.4f}")