#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    compute squares of all integers in a matrix
    Args:
        a 2D matrix of integers
    return:
        a new matrix with each integer squared
    """
    squar = []
    for line in matrix:
        squared_line = list(map(lambda c: c**2, line))
        squar.append(squared_line)
    return squar
