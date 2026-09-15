"""
================================================================================
SECTION 5: FIXED POINT ITERATION METHOD
================================================================================
INTRODUCTION:
Fixed Point Iteration reformulates f(x) = 0 into x = g(x), generating a sequence 
x_{n+1} = g(x_n) that converges when |g'(x)| < 1.

QUESTION:
Find a root of x^2 - 3x + 1 = 0 correct to 3 decimal places using Fixed Point Iteration.

ALGORITHM:
1. Rewrite x^2 - 3x + 1 = 0 into x = g(x) = (x^2 + 1) / 3.
2. Choose initial guess x0 = 0.0.
3. Compute x1 = g(x0).
4. Check convergence: If |x1 - x0| < 0.0005, stop.
5. Update x0 = x1 and repeat steps 3-4.
================================================================================
"""

def g(x): 
    return (x**2 + 1.0) / 3.0

x0 = 0.0

for i in range(100):
    x1 = g(x0)
    if abs(x1 - x0) < 0.0005:
        break
    x0 = x1

print(f"Root = {x1:.3f}")