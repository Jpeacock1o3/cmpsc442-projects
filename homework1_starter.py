############################################################
# CMPSC 442: Uninformed Search
############################################################

student_name = "Jaden Peacock"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
from math import comb


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    return comb(n * n, n)

def num_placements_one_per_row(n):
    return n ** n

def n_queens_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            # Check for same column
            if board[i] == board[j]:
                return False
            # Check for same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def n_queens_solutions(n):
    def is_valid(board, row, col):
        # Check if placing a queen at (row, col) is valid
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row, board):
        if row == n:
            solutions.append(board[:])  # Store a copy of the valid board
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col  # Place queen at (row, col)
                solve(row + 1, board)  # Recur for the next row
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * n  # Initialize the board (-1 means no queen placed)
    solve(0, board)
    return solutions

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

if __name__ == "__main__":
    # Test cases for num_placements_all
    print("Testing num_placements_all:")
    print(f"n=2: {num_placements_all(2)} (Expected: 16)")
    print(f"n=3: {num_placements_all(3)}")

    # Test cases for num_placements_one_per_row
    print("\nTesting num_placements_one_per_row:")
    print(f"n=2: {num_placements_one_per_row(2)} (Expected: 4)")
    print(f"n=3: {num_placements_one_per_row(3)} (Expected: 27)")

    # Test cases for n_queens_valid
    print("\nTesting n_queens_valid:")
    print(f"[0, 3, 1]: {n_queens_valid([0, 3, 1])} (Expected: True)")
    print(f"[0, 1]: {n_queens_valid([0, 1])} (Expected: False)")

    # Test cases for n_queens_solutions
    print("\nTesting n_queens_solutions:")
    solutions_4 = n_queens_solutions(4)
    print(f"n=4: Number of solutions: {len(solutions_4)} (Expected: 2)")
    print(f"Solutions: {solutions_4}")
    solutions_8 = n_queens_solutions(8)
    print(f"n=8: Number of solutions: {len(solutions_8)} (Expected: 92)")