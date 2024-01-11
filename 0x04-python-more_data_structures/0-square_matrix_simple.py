#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return [[x * x for x in row] for row in matrix]
