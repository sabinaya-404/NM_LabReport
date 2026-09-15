"""
================================================================================
PDE TUTORIAL: LAPLACE STEADY STATE EQUATION
================================================================================
INTRODUCTION:
Laplace's PDE (∇^2 u = 0) models steady-state heat conduction across 2D plates using 
5-point finite difference stencils: 4*u_{i,j} - u_{i+1,j} - u_{i-1,j} - u_{i,j+1} - u_{i,j-1} = 0.

QUESTION:
Calculate steady-state temperatures at internal grid nodes of a 90cm x 90cm plate 
with 30cm grid spacing, given boundary temperatures of 100°C on left/top and 200°C on right/bottom.

ALGORITHM:
1. Label 4 interior nodes (u11, u12, u21, u22).
2. Apply 5-point Liebmann stencil at each node to build 4x4 coefficient matrix A.
3. Move boundary condition temperatures to right-hand vector B.
4. Solve matrix system u = A^(-1) * B using np.linalg.solve.
================================================================================
"""

import numpy as np

A = np.array([
    [ 4, -1, -1,  0],
    [-1,  4,  0, -1],
    [-1,  0,  4, -1],
    [ 0, -1, -1,  4]
])

B = np.array([200, 300, 300, 400])
u = np.linalg.solve(A, B)

print(f"Node u11 Temp = {u[0]:.2f}°C")
print(f"Node u12 Temp = {u[1]:.2f}°C")
print(f"Node u21 Temp = {u[2]:.2f}°C")
print(f"Node u22 Temp = {u[3]:.2f}°C")