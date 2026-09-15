"""
================================================================================
SECTION D: NEWTON'S BACKWARD DIFFERENCE INTERPOLATION
================================================================================
INTRODUCTION:
Newton's Backward Interpolation evaluates polynomial values near the end of an 
equally spaced dataset using backward differences ∇y.

QUESTION:
Estimate f(38) using Newton's Backward Difference formula for dataset:
x: [20, 25, 30, 35, 40]
y: [354, 332, 291, 260, 231]

ALGORITHM:
1. Construct backward difference matrix ∇y.
2. Compute step size h = x1 - x0 and factor u = (x - x_n) / h.
3. Apply formula: f(x) = y_n + u*∇y_n + [u(u+1)/2!]*∇^2y_n + ...
4. Evaluate polynomial sum and print result.
================================================================================
"""

import numpy as np

x_val = [20, 25, 30, 35, 40]
y_val = [354, 332, 291, 260, 231]
x = 38

n = len(x_val)
diff = np.zeros((n, n))
diff[:, 0] = y_val

for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
        diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

h = x_val[1] - x_val[0]
u = (x - x_val[-1]) / h
res = diff[-1][0]
u_term = 1.0
fact = 1.0

for i in range(1, n):
    u_term *= (u + (i - 1))
    fact *= i
    res += (u_term * diff[-1][i]) / fact

print(f"f(38) = {res:.4f}")