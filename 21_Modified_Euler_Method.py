"""
================================================================================
SECTION D: MODIFIED EULER'S METHOD
================================================================================
INTRODUCTION:
Modified Euler's Method improves accuracy using predictor-corrector steps by averaging 
slopes at the start and end of step intervals.

QUESTION:
Find y(0.2) given dy/dx = (y - x)/(y + x) with y(0) = 1 and step size h = 0.1.

ALGORITHM:
1. Predict initial slope y_prime = f(x, y).
2. Predict next state y_pred = y + h * y_prime.
3. Correct state: y = y + (h/2) * [y_prime + f(x + h, y_pred)].
4. Increment x += h and repeat.
================================================================================
"""

def f(x, y): 
    return (y - x) / (y + x)

x, y, h = 0.0, 1.0, 0.1
steps = int(0.2 / h)

for _ in range(steps):
    y_prime = f(x, y)
    y_pred = y + h * y_prime
    y = y + (h / 2.0) * (y_prime + f(x + h, y_pred))
    x += h

print(f"y(0.2) = {y:.4f}")