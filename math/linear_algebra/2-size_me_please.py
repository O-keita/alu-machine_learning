#!/usr/bin/env python3
"""
    Function that calculates the shape
    of a matrix
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a metric
    """

    shape = []
    while type(matrix) == list:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
