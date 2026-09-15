"""
================================================================================
SECTION A: NEWTON'S FORWARD DIFFERENTIATION
================================================================================
INTRODUCTION:
Numerical Differentiation estimates derivatives of tabular functions using 
forward differences derived from Taylor series expansions.

QUESTION:
Find dy/dx and d2y/dx2 at x = 1 for the dataset:
x: [1, 2, 3, 4, 5]
y: [1, 8, 27, 64, 125]

ALGORITHM:
1. Compute first forward difference dy = y1 - y0.
2. Compute second forward difference d2y = y2 - 2y1 + y0.
3. Compute dy/dx = (1/h) * [dy - (1/2)*d2y].
4. Compute d2y/dx2 = (1/h^2) * [d2y].
================================================================================
"""

x = [1, 2, 3, 4, 5]
y = [1, 8, 27, 64, 125]
h = 1

dy = y[1] - y[0]
d2y = y[2] - 2*y[1] + y[0]

dy_dx = (dy - d2y / 2.0) / h
d2y_dx2 = d2y / (h**2)

print(f"dy/dx at x=1 = {dy_dx:.4f}")
print(f"d2y/dx2 at x=1 = {d2y_dx2:.4f}")