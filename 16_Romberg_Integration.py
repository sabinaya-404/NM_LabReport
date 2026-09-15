"""
================================================================================
SECTION D: ROMBERG INTEGRATION
================================================================================
INTRODUCTION:
Romberg Integration combines Trapezoidal rule estimates at decreasing step sizes 
with Richardson extrapolation to achieve higher-order accuracy.

QUESTION:
Evaluate the integral of e^(-x^2) dx from 0 to 1 using Romberg Integration with 
step sizes h = 0.5, 0.25, and 0.125.

ALGORITHM:
1. Compute Trapezoidal estimates R[i, 0] for step sizes h = 0.5, 0.25, 0.125.
2. Extrapolate values: R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4^j - 1).
3. Return R[2, 2] as final integrated value.
================================================================================
"""

import math
import numpy as np

def f(x): 
    return math.exp(-x**2)

def trap(h):
    n = int(1.0 / h)
    return h * (0.5*f(0) + sum(f(i*h) for i in range(1, n)) + 0.5*f(1))

R = np.zeros((3, 3))
h_vals = [0.5, 0.25, 0.125]

for i in range(3):
    R[i, 0] = trap(h_vals[i])

for j in range(1, 3):
    for i in range(j, 3):
        R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

print(f"Romberg Integral Result = {R[2, 2]:.6f}")