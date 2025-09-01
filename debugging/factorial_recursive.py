#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function description:
    Calculates the factorial of a given number using recursive approach.
    The factorial of a number n is the product of all positive integers 
    less than or equal to n (n! = n × (n-1) × (n-2) × ... × 1).
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.
            Must be >= 0, where 0! = 1 by mathematical convention.
    
    Returns:
    int: The factorial of the input number n.
        Returns 1 if n is 0, otherwise returns n × factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    """Main function with error handling for command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python3 factorial_recursive.py <number>")
        print("Example: python3 factorial_recursive.py 5")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            print("Error: Please enter a non-negative integer")
            sys.exit(1)
        
        result = factorial(n)
        print(f"Factorial of {n} is: {result}")
    
    except ValueError:
        print("Error: Please enter a valid integer")
        sys.exit(1)

if __name__ == "__main__":
    main()