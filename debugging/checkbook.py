#!/usr/bin/python3
"""
Checkbook Manager Application

This module implements a simple checkbook management system that allows users
to perform basic banking operations such as deposits, withdrawals, and balance inquiries.
The application includes robust error handling to prevent crashes from invalid user input.

Author: Holberton School Student
Date: September 2025
"""


class Checkbook:
    """
    A simple checkbook management system for tracking financial transactions.
    
    This class provides functionality to manage a personal checking account
    with basic operations like deposits, withdrawals, and balance inquiries.
    All amounts are handled as floating-point numbers with two decimal precision.
    
    Attributes:
        balance (float): The current account balance, initialized to 0.0
    """
    
    def __init__(self):
        """
        Initialize a new Checkbook instance.
        
        Creates a new checkbook with an initial balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add money to the account balance.
        
        Validates that the deposit amount is positive before adding it to the balance.
        Prints confirmation messages showing the deposited amount and new balance.
        
        Parameters:
            amount (float): The amount of money to deposit (must be positive)
            
        Returns:
            bool: True if deposit was successful, False if amount was invalid
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))
        return True

    def withdraw(self, amount):
        """
        Remove money from the account balance.
        
        Validates that the withdrawal amount is positive and that sufficient funds
        are available before processing the withdrawal. Prints confirmation messages
        or error messages as appropriate.
        
        Parameters:
            amount (float): The amount of money to withdraw (must be positive)
            
        Returns:
            bool: True if withdrawal was successful, False if amount was invalid or insufficient funds
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return False
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
            return True

    def get_balance(self):
        """
        Display the current account balance.
        
        Prints the current balance formatted to two decimal places with currency symbol.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """
    Prompts user for a valid positive number and handles input validation.
    
    Parameters:
    prompt (str): The message to display to the user
    
    Returns:
    float: A valid positive number, or None if user wants to cancel
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() in ['cancel', 'exit', 'quit']:
                return None
            amount = float(user_input)
            if amount <= 0:
                print("Error: Amount must be a positive number. Enter 'cancel' to go back.")
                continue
            return amount
        except ValueError:
            print("Error: Please enter a valid number. Enter 'cancel' to go back.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def main():
    """
    Main application loop for the Checkbook Manager.
    
    Provides an interactive command-line interface for users to manage their checkbook.
    Supports the following commands:
    - deposit: Add money to the account
    - withdraw: Remove money from the account  
    - balance: Display current balance
    - help: Show available commands
    - exit: Quit the application
    
    The function includes comprehensive error handling to prevent crashes from:
    - Invalid command inputs
    - Keyboard interruptions (Ctrl+C)
    - Unexpected exceptions
    
    The application will continue running until the user chooses to exit.
    """
    # Create a new checkbook instance
    cb = Checkbook()
    
    # Display welcome message and instructions
    print("Welcome to your Checkbook Manager!")
    print("Commands: deposit, withdraw, balance, exit")
    print("You can type 'cancel' when entering amounts to go back to the main menu.\n")
    
    # Main application loop
    while True:
        try:
            # Get user command and normalize it (strip whitespace, convert to lowercase)
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            
            if action == 'exit':
                print("Thank you for using Checkbook Manager. Goodbye!")
                break
            elif action == 'deposit':
                # Handle deposit operation with input validation
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:  # User didn't cancel
                    cb.deposit(amount)
            elif action == 'withdraw':
                # Handle withdrawal operation with input validation
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:  # User didn't cancel
                    cb.withdraw(amount)
            elif action == 'balance':
                # Display current balance
                cb.get_balance()
            elif action in ['help', '?']:
                # Display help information
                print("Available commands:")
                print("  deposit  - Add money to your account")
                print("  withdraw - Remove money from your account") 
                print("  balance  - Check your current balance")
                print("  exit     - Quit the program")
            else:
                # Handle invalid commands
                print("Invalid command. Please try again. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nExiting Checkbook Manager. Goodbye!")
            break
        except Exception as e:
            # Handle any unexpected errors
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    """
    Entry point of the Checkbook Manager application.
    
    This block ensures that the main() function is only called when the script
    is run directly, not when it's imported as a module. This is a Python
    best practice for creating reusable modules.
    """
    main()