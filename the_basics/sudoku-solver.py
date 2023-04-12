"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""
import time


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

# Sudoku solver's are a classic CS 101 problem that requires you to understand constraints
# and understand the difference between a brute force solution and a more efficient solution

# We're dealing with an array of arrays, so we need to nest two loops. Loop 1 will
# iterate through the rows, and loop 2 will iterate through the columns.

def main():
    for i in range (9):
        for j in range (9):
            # we need to check if the cell is empty and print the board
            # I want to do this first so my solving is animated.
            if j != 8:
                print(f"{board[i][j]}", end=" ")
                time.sleep(0.1)
            else:
                print(f"{board[i][j]}", end="\n")

            # now we need to actually do the game logic
            # if board[i][j] == ".":

def solver(board):
    print("bleh")


# if you aren't familiar, you do this so you can call the main function
# it checks 

if __name__ == '__main__':
    main()