#!/usr/bin/env python3
"""
    concatenates two matrices along a specific axis:
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
        concatenate two  metrices along a specific axis
    """

    if axis == 0:
        if len(mat1) != len(mat2):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    if axis == 1 and len(mat1) != len(mat2):
        return None
    elif axis == 0:
        if len(mat1) != len(mat2):
            return None
        return [row1[:] + row2[:] for row1, row2 in zip(mat1, mat2)]
    return None

