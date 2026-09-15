"""
================================================================================
SECTION H: HIGHER-ORDER ODE SOLUTION VIA RK4
================================================================================
INTRODUCTION:
Higher-order differential equations are solved by reducing them into coupled 
systems of first-order ODEs and updating state vectors simultaneously.

QUESTION:
Reduce 2nd order ODE y'' + y = 0 with y(0) = 0, y'(0) = 1 to 1st order systems 
and evaluate y(0.2) using h = 0.1.

ALGORITHM:
1. Reduce system: Let dy/dx = z and dz/dx = -y.
2. Calculate coupled RK4 slope parameters for both y and z variables.
3. Update states y and z simultaneously using weighted RK4 averages.
================================================================================
"""

x, y, z, h = 0.0, 0.0, 1.0, 0.1
steps = int(0.2 / h)

for _ in range(steps):
    k1_y = h * z
    k1_z = h * (-y)
    
    k2_y = h * (z + 0.5 * k1_z)
    k2_z = h * (-(y + 0.5 * k1_y))
    
    k3_y = h * (z + 0.5 * k2_z)
    k3_z = h * (-(y + 0.5 * k2_y))
    
    k4_y = h * (z + k3_z)
    k4_z = h * (-(y + k3_y))
    
    y += (k1_y + 2*k2_y + 2*k3_y + k4_y) / 6.0
    z += (k1_z + 2*k2_z + 2*k3_z + k4_z) / 6.0
    x += h

print(f"y(0.2) = {y:.4f}")