#!/usr/bin/env python3
"""Module containing a function to sum a mixed list of numbers."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all integers and floats in a list."""
    return sum(mxd_lst)
