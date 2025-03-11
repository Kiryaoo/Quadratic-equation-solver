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

def interactive_mode():
    """Інтерактивний режим: введення користувачем"""
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError as e:
                print(f"Error. Expected a valid real number, got {e.args[0]} instead")

    a = get_float("a = ")
    while a == 0:
        print("Error. a cannot be 0")
        a = get_float("a = ")

    b = get_float("b = ")
    c = get_float("c = ")

    solve_quadratic(a, b, c)

def file_mode(filename):
    """Неінтерактивний режим: зчитування з файлу"""
    if not os.path.exists(filename):
        print(f"file {filename} does not exist")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            line = file.readline().strip()
            parts = line.split()

            if len(parts) != 3:
                raise ValueError("invalid file format")

            a, b, c = map(float, parts)
            solve_quadratic(a, b, c)

    except ValueError as e:
        print("invalid file format")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: python solver.py [file]")
        sys.exit(1)