#!/usr/bin/python3
"""
Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game
for two players (X and O).
"""


def print_board(board):
    """
    Print the current state of the game board.
    
    Parameters:
        board (list): 3x3 list representing the game board
    """
    print("\nCurrent board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print separator after last row
            print("-" * 9)
    print()


def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Parameters:
        board (list): 3x3 list representing the game board
        
    Returns:
        str: The winning player ('X' or 'O'), or None if no winner
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    """
    Check if the board is completely filled.
    
    Parameters:
        board (list): 3x3 list representing the game board
        
    Returns:
        bool: True if board is full, False otherwise
    """
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_input(prompt, valid_range):
    """
    Get valid integer input from user within specified range.
    
    Parameters:
        prompt (str): Message to display to user
        valid_range (list): List of valid integer values
        
    Returns:
        int: Valid integer input
    """
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Please enter a number between {min(valid_range)} and {max(valid_range)}")
        except ValueError:
            print("Please enter a valid number")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            exit()


def tic_tac_toe():
    """
    Main game function that runs the Tic-Tac-Toe game loop.
    """
    # Initialize game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Players will take turns. Enter row and column numbers (0, 1, or 2)")
    
    while True:
        print_board(board)
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print(f"🎉 Player {winner} wins! 🎉")
            break
            
        # Check for tie
        if is_board_full(board):
            print("It's a tie! The board is full.")
            break
        
        print(f"Player {player}'s turn")
        
        # Get player move with validation
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ", [0, 1, 2])
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ", [0, 1, 2])
        
        # Check if spot is available
        if board[row][col] == " ":
            board[row][col] = player
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")


if __name__ == "__main__":
    tic_tac_toe()