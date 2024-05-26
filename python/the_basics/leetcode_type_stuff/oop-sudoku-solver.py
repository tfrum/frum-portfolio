# Basically Steve Balmer's first python project lbh

class Board:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self, row, col, num):
        # Check the number in the row
        if num in self.grid[row]:
            return False

        # Check the number in the column
        if num in [self.grid[r][col] for r in range(9)]:
            return False

        # Check the number in the box
        start_row, start_col = row - row % 3, col - col % 3
        if num in [self.grid[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]:
            return False

        return True

    def get_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col
        return None


class Solver:
    @staticmethod
    def solve(board):
        empty_cell = board.get_empty_cell()
        if not empty_cell:
            return board

        row, col = empty_cell

        for num in range(1, 10):
            if board.is_valid(row, col, num):
                board.grid[row][col] = num
                solution = Solver.solve(board)
                if solution:
                    return solution
                board.grid[row][col] = 0

        return None


class Solution:
    def __init__(self, board):
        self.board = board


class Display:
    @staticmethod
    def print_board(solution):
        for row in range(9):
            if row % 3 == 0 and row != 0:
                print("- - - - - - - - - - -")
            for col in range(9):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")
                print(str(solution.board.grid[row][col]) + " ", end="")
            print()


# Test
grid = [
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

board = Board(grid)
solution = Solver.solve(board)

if solution:
    display = Display()
    display.print_board(Solution(solution))
else:
    print("Bad board. No solution")