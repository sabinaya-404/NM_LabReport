"""
================================================================================
SECTION B: NEWTON'S BACKWARD DIFFERENTIATION
================================================================================
INTRODUCTION:
Backward differentiation estimates derivatives at or near the end of a tabular 
dataset using backward difference operators.

QUESTION:
Find dy/dx at x = 0.5 given the tabular data for y = e^x with step size h = 0.1:
y: [1.10517, 1.2214, 1.34986, 1.49182, 1.64872]

ALGORITHM:
1. Compute first backward difference del1 = y_n - y_{n-1}.
2. Compute second backward difference del2 = y_n - 2*y_{n-1} + y_{n-2}.
3. Apply formula: dy/dx = (1/h) * [del1 + (1/2)*del2].
================================================================================
"""

y = [1.10517, 1.2214, 1.34986, 1.49182, 1.64872]
h = 0.1

del1 = y[-1] - y[-2]
del2 = y[-1] - 2*y[-2] + y[-3]

dy_dx = (del1 + del2 / 2.0) / h

print(f"dy/dx at x=0.5 = {dy_dx:.4f}")