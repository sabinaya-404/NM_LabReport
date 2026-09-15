"""
================================================================================
SECTION 1: BISECTION METHOD
================================================================================
INTRODUCTION:
The Bisection Method is a root-finding algorithm that repeatedly bisects an 
interval [a, b] where f(a) and f(b) have opposite signs, guaranteeing a root 
by the Intermediate Value Theorem.

QUESTION 2
Find a real root of the non-linear equation f(x) = x^3 - 4x - 9 = 0, 
correct to 3 decimal places using the Bisection Method.

ALGORITHM:
1. Define the function f(x) = x^3 - 4x - 9.
2. Choose initial bounds [a, b] such that f(a) * f(b) < 0.
3. Compute the midpoint c = (a + b) / 2.
4. Evaluate f(c):
   - If f(c) == 0, c is the root. Stop.
   - If f(a) * f(c) < 0, set b = c.
   - Else, set a = c.
5. Repeat steps 3-4 until (b - a) / 2 < tolerance (0.0005).
================================================================================
"""

def f(x): 
    return x**3 - 4*x - 9

a, b = 2.0, 3.0
tol = 0.0005

while (b - a) / 2.0 > tol:
    c = (a + b) / 2.0
    if f(c) == 0:
        break
    elif f(a) * f(c) < 0:
        b = c
    else:
        a = c

root = (a + b) / 2.0
print(f"Root = {root:.3f}")