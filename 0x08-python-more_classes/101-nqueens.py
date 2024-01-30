#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""


import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' ' for _ in range(n)] for _ in range(n)]


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r, row in enumerate(board) for c, cell in enumerate(row) if cell == "Q"]


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    n = len(board)
    for c in range(col + 1, n):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, n):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    for r, c in zip(range(row + 1, n), range(col + 1, n)):
        if c >= n:
            break
        board[r][c] = "x"
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if c < 0:
            break
        board[r][c] = "x"
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if c >= n:
            break
        board[r][c] = "x"
    for r, c in zip(range(row + 1, n), range(col - 1, -1, -1)):
        if c < 0:
            break
        board[r][c] = "x"


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    n = len(board)

    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for c in range(n):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
