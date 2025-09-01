#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of n using iterative approach.
    
    Fix applied: Added n -= 1 to decrement n in each iteration,
    preventing infinite loop.
    """
    result = 1
    while n > 1:
        result *= n  # Multiply current result by n
        n -= 1       # ✅ FIX: Decrement n to eventually exit loop
    return result

# Handle command line arguments safely
if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Error: Factorial is not defined for negative numbers")
        sys.exit(1)
    
    f = factorial(number)
    print(f)
    
except ValueError:
    print("Error: Please enter a valid integer")
    sys.exit(1)
