#!/usr/bin/env python3
"""
Adding two metrices element-wise
"""


def add_matrices2D(mat1, mat2):
    """Adding two metrices element wise"""

    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    else:
        return [[mat1[i][j] + mat2[i][j] 
            for j in range(len(mat1[0]))]
            for i in range(len(mat1))
            ]
