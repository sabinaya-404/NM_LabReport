"""
================================================================================
SECTION G: LEAST SQUARE METHOD (CURVE FITTING)
================================================================================
INTRODUCTION:
The Least Squares Method fits a polynomial function y = a + bx + cx^2 to data 
by minimizing the sum of squared residuals between observed and predicted values.

QUESTION:
Fit a second-degree parabola y = a + bx + cx^2 to the given dataset:
x: [0, 1, 2, 3, 4]
y: [1.0, 1.8, 1.3, 2.5, 6.3]

ALGORITHM:
1. Input arrays x and y.
2. Use np.polyfit(x, y, 2) to build and solve the system of normal equations.
3. Extract coefficients c, b, and a. Print fitted parabola equation.
================================================================================
"""

import numpy as np

x = np.array([0, 1, 2, 3, 4])
y = np.array([1.0, 1.8, 1.3, 2.5, 6.3])

coeffs = np.polyfit(x, y, 2)
c, b, a = coeffs[0], coeffs[1], coeffs[2]

print(f"Parabola: y = {a:.4f} + {b:.4f}x + {c:.4f}x^2")