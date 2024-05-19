def is_valid(board, row, col, num):
    # Check the number in the row
    if num in board[row]:
        return False

    # Check the number in the column
    if num in [board[r][col] for r in range(9)]:
        return False

    # Check the number in the box
    start_row, start_col = row - row % 3, col - col % 3
    if num in [board[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]:
        return False

    return True


def solve_sudoku(board, row=0, col=0):
    # If we are at the end of the board move along
    if row == 9:
        return True

    # If we are at the end, move to the next row
    if col == 9:
        return solve_sudoku(board, row + 1, 0)

    # If the current cell is not empty, move to the next cell
    if board[row][col] != 0:
        return solve_sudoku(board, row, col + 1)

    # Try numbers from 1 to9
    def try_numbers(num):
        if num > 9:
            return False
        if is_valid(board, row, col, num):
            # If the number is valid, place it in the cell
            board[row][col] = num
            # Recursively try to fill the rest of the board
            if solve_sudoku(board, row, col + 1):
                return True
            # If it doesn't work, reset
            board[row][col] = 0
        return try_numbers(num + 1)

    return try_numbers(1)


def print_board(board):
    # Print the board
    def print_rows(row):
        if row == 9:
            return
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        def print_cols(col):
            if col == 9:
                print()
                return
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(str(board[row][col]) + " ", end="")
            print_cols(col + 1)
        print_cols(0)
        print_rows(row + 1)

    print_rows(0)


# Test
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(board):
    print_board(board)
else:
    print("Bad board. No solution")