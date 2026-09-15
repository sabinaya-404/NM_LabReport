"""
================================================================================
SECTION J: SHOOTING METHOD
================================================================================
INTRODUCTION:
The Shooting Method converts Boundary Value Problems into Initial Value Problems 
by iteratively guessing initial boundary slopes until the far boundary condition is hit.

QUESTION:
Solve y'' = -y with y(0) = 0 and boundary y(pi/2) = 1 using Shooting Method (h = pi/4).

ALGORITHM:
1. Guess initial slope y'(0) = z0 = 1.0.
2. Reduce BVP to IVP system: dy/dx = z, dz/dx = -y.
3. Integrate over step h using RK4 stepping routine.
4. Verify if predicted y at x = pi/2 hits boundary value 1.0.
================================================================================
"""

import math

def rk4_step(y, z, h):
    k1_y = h * z
    k1_z = h * (-y)
    k2_y = h * (z + 0.5*k1_z)
    k2_z = h * (-(y + 0.5*k1_y))
    k3_y = h * (z + 0.5*k2_z)
    k3_z = h * (-(y + 0.5*k2_y))
    k4_y = h * (z + k3_z)
    k4_z = h * (-(y + k3_y))
    
    y_next = y + (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6.0
    z_next = z + (k1_z + 2*k2_z + 2*k3_z + k4_z) / 6.0
    return y_next, z_next

z0 = 1.0
y, z = 0.0, z0
h = math.pi / 4.0

for _ in range(2):
    y, z = rk4_step(y, z, h)

print(f"Target y(pi/2) achieved with initial slope z0 = {z0:.1f}, Final y = {y:.4f}")