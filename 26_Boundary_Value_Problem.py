"""
================================================================================
SECTION I: FINITE DIFFERENCE METHOD FOR BVPs
================================================================================
INTRODUCTION:
Finite Difference replaces derivative terms with central difference algebraic 
approximations, converting differential BVPs into linear matrix systems.

QUESTION:
Solve y'' + y + 1 = 0 with boundary conditions y(0) = 0, y(1) = 0 and step h = 0.25.

ALGORITHM:
1. Discretize derivative: y'' ≈ (y_{i-1} - 2y_i + y_{i+1}) / h^2.
2. Rearrange terms to linear equation form: y_{i-1} - (2 - h^2)y_i + y_{i+1} = -h^2.
3. Construct tridiagonal matrix A and vector B. Solve system A * Y = B using np.linalg.solve.
================================================================================
"""

import numpy as np

h = 0.25
diag = -(2.0 - h**2)

A = np.array([
    [diag, 1.0, 0.0],
    [1.0, diag, 1.0],
    [0.0, 1.0, diag]
])

B = np.array([-h**2, -h**2, -h**2])
y_internal = np.linalg.solve(A, B)

print(f"y(0.25) = {y_internal[0]:.4f}")
print(f"y(0.50) = {y_internal[1]:.4f}")
print(f"y(0.75) = {y_internal[2]:.4f}")