"""
================================================================================
SECTION C: NEWTON'S FORWARD DIFFERENCE INTERPOLATION
================================================================================
INTRODUCTION:
Newton's Forward Interpolation evaluates polynomial values near the start of an 
equally spaced dataset using forward differences Δy.

QUESTION:
Find f(15) using Newton's Forward Difference formula for dataset:
x: [10, 20, 30, 40]
y: [1.1, 2.0, 4.4, 7.9]

ALGORITHM:
1. Build forward difference table matrix Δy.
2. Calculate step size h = x1 - x0 and factor u = (x - x0) / h.
3. Apply formula: f(x) = y0 + u*Δy0 + [u(u-1)/2!]*Δ^2y0 + ...
4. Accumulate sum across table columns and print output.
================================================================================
"""

import numpy as np

x_val = [10, 20, 30, 40]
y_val = [1.1, 2.0, 4.4, 7.9]
x = 15

n = len(x_val)
diff = np.zeros((n, n))
diff[:, 0] = y_val

for j in range(1, n):
    for i in range(n - j):
        diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

h = x_val[1] - x_val[0]
u = (x - x_val[0]) / h
res = diff[0][0]
u_term = 1.0
fact = 1.0

for i in range(1, n):
    u_term *= (u - (i - 1))
    fact *= i
    res += (u_term * diff[0][i]) / fact

print(f"f(15) = {res:.4f}")