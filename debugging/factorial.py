#!/usr/bin/python3
"""
Factorial Calculator - Iterative Implementation

This module calculates the factorial of a number using an iterative approach.
The factorial of n (written as n!) is the product of all positive integers
from 1 to n. By mathematical convention, 0! = 1.

This implementation uses a while loop instead of recursion, making it
more memory-efficient for large numbers.

Author: Holberton School Student
Date: September 2025
"""

import sys

def factorial(n):
    """
    Calculate factorial of n using iterative approach.
    
    This function uses a while loop to multiply all integers from 1 to n.
    It's more memory-efficient than the recursive approach as it doesn't
    create multiple function call frames on the stack.
    
    Parameters:
        n (int): Non-negative integer for which to calculate factorial
        
    Returns:
        int: Factorial of n (n!)
        
    Raises:
        ValueError: If n is negative (factorial undefined for negative numbers)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Initialize result to 1 (handles case where n=0)
    result = 1
    
    # Multiply by each integer from n down to 2
    # (we stop at 2 because multiplying by 1 doesn't change the result)
    while n > 1:
        result *= n  # Multiply current result by n
        n -= 1       # Decrement n for next iteration
    
    return result

def main():
    """Main function with error handling for command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        print("Example: python3 factorial.py 5")
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