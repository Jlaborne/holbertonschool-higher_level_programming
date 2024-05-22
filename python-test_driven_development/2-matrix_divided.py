#!/usr/bin/python3
"""Function that divide integer"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number

    Args:
        matrix (list of lists): a list of lists of int or float
        div (int / float): the divisor

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   If each row of the matrix is not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Return:
        list of lists: A new matrix with elements divided by div round to 2.
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
