"""
================================================================================
SECTION B: LAGRANGE'S INTERPOLATION
================================================================================
INTRODUCTION:
Lagrange Interpolation fits a polynomial through a set of non-equispaced points 
without computing difference tables using basis polynomials L_i(x).

QUESTION:
Calculate y at x = 3 using Lagrange's Interpolation for the dataset:
x: [0, 1, 2, 4]
y: [1, 3, 7, 13]

ALGORITHM:
1. Load x_val and y_val arrays.
2. Initialize total result = 0.
3. For each point i from 0 to n-1:
   a. Compute weight product L_i(x) = PROD[(x - x_j) / (x_i - x_j)] for all j != i.
   b. Add term y_val[i] * L_i(x) to result.
4. Output result.
================================================================================
"""

x_val = [0, 1, 2, 4]
y_val = [1, 3, 7, 13]
x = 3

n = len(x_val)
result = 0.0

for i in range(n):
    term = y_val[i]
    for j in range(n):
        if i != j:
            term *= (x - x_val[j]) / (x_val[i] - x_val[j])
    result += term

print(f"y(3) = {result:.4f}")