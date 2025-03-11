import sys
import math
import os

def solve_quadratic(a: float, b: float, c: float):
    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")


    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print("There are 1 roots")
        print(f"x1 = {x}")
    else:
        print("There are 0 roots")