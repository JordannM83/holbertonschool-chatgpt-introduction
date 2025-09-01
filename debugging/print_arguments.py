#!/usr/bin/python3
"""
Command Line Arguments Printer

This script demonstrates how to handle and print command-line arguments in Python.
It prints each argument passed to the script (excluding the script name itself).

Usage: python3 print_arguments.py <arg1> <arg2> <arg3> ...
Example: python3 print_arguments.py hello world 123

Author: Holberton School Student
Date: September 2025
"""

import sys

def main():
    """
    Main function that prints all command-line arguments.
    
    The script iterates through sys.argv starting from index 1 
    (skipping index 0 which contains the script name) and prints
    each argument on a separate line.
    """
    # Check if any arguments were provided
    if len(sys.argv) == 1:
        print("No arguments provided.")
        print("Usage: python3 print_arguments.py <arg1> <arg2> ...")
        return
    
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]}")

if __name__ == "__main__":
    main()