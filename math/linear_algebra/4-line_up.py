#!/usr/bin/env python3
"""
Line Up
"""


def add_arrays(arr1, arr2):
    """Add arr1 and arr2"""

    if len(arr1) != len(arr2):
        return None
    else:
        return [arr1[i] + arr2[i] for i in range(len(arr1))]
