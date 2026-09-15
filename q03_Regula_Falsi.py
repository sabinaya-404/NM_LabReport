"""
================================================================================
SECTION 3: REGULA-FALSI METHOD (FALSE POSITION)
================================================================================
INTRODUCTION:
The Regula-Falsi Method combines the bracketing safety of Bisection with linear 
interpolation to approximate roots by connecting points with a secant line.

QUESTION:
Find a real root of x^3 - x - 1 = 0 correct to 3 decimal places using the 
Regula-Falsi Method.

ALGORITHM:
1. Define f(x) = x^3 - x - 1.
2. Choose initial bounds [a, b] such that f(a) * f(b) < 0.
3. Compute c = (a*f(b) - b*f(a)) / (f(b) - f(a)).
4. Evaluate convergence: If |c_new - c_old| < 0.0005, stop.
5. If f(a) * f(c) < 0, set b = c; else set a = c. Repeat steps 3-4.
================================================================================
"""

def f(x): 
    return x**3 - x - 1

a, b = 1.0, 2.0
c = a

for i in range(100):
    c_prev = c
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if abs(c - c_prev) < 0.0005:
        break
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(f"Root = {c:.3f}")