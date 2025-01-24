#!/usr/bin/env python3
import numpy as np


def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Parameters:
    - matrix: numpy.ndarray - the matrix to slice
    - axes: dict - keys are axes to slice along, and values are tuples representing the slice

    Returns:
    - numpy.ndarray: the sliced matrix
    """
    # Create a slicing object for all axes of the matrix
    slices = [slice(None)] * matrix.ndim

    # Update the slices based on the axes dictionary
    for axis, slc in axes.items():
        slices[axis] = slice(*slc)

    # Apply the slicing and return the result
    return matrix[tuple(slices)]
