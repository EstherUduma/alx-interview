#!/usr/bin/python3
import sys
"""Solves the nqueens problem"""


def is_safe(board, row, col, N):
    """Document later"""
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row, N):
    """Document later"""
    if row == N:
        return [board[:]]

    solutions = []
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solutions += solve_nqueens_util(board, row + 1, N)
            board[row] = -1

    return solutions


def solve_nqueens(N):
    """Document later"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = solve_nqueens_util(board, 0, N)
    if not solutions:
        print("No solution exists")
        return

    for sol in solutions:
        print_solution(sol)


def print_solution(board):
    """Document later"""
    print("[", end="")
    for i, col in enumerate(board):
        print(f"[{i}, {col}]", end="")
        if i != len(board) - 1:
            print(", ", end="")
    print("]", end=" ")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)