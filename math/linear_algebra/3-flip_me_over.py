#!/usr/bin/env python3
"""
    flipping a matrix
    (Tranpose)
"""


def matrix_transpose(matrix):
    """Trasposing Matrix"""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
