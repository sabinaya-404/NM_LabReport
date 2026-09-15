"""
================================================================================
SECTION E: NEWTON'S DIVIDED DIFFERENCE INTERPOLATION
================================================================================
INTRODUCTION:
Newton's Divided Difference method handles unequally spaced datasets by constructing 
divided differences f[x_i, ..., x_k] = (f[x_{i+1}] - f[x_i]) / (x_k - x_i).

QUESTION:
Find f(2) using Newton's Divided Difference formula for dataset:
x: [0, 1, 3, 4]
y: [5, 6, 50, 105]

ALGORITHM:
1. Create table and compute divided differences column by column.
2. Initialize sum = f[x0].
3. For each order i, compute product (x - x0)(x - x1)...(x - x_{i-1}).
4. Multiply product by divided difference table[0][i] and add to sum.
================================================================================
"""

import numpy as np

x_val = [0, 1, 3, 4]
y_val = [5, 6, 50, 105]
x = 2

n = len(x_val)
table = np.zeros((n, n))
table[:, 0] = y_val

for j in range(1, n):
    for i in range(n - j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x_val[i+j] - x_val[i])

res = table[0][0]
product = 1.0

for i in range(1, n):
    product *= (x - x_val[i-1])
    res += product * table[0][i]

print(f"f(2) = {res:.4f}")