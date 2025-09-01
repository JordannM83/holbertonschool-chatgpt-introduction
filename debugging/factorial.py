#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate factorial of n using iterative approach.
    
    Parameters:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
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