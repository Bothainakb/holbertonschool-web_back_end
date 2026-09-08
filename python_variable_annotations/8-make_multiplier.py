#!/usr/bin/env python3
"""Module containing a function that creates a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """Multiply a float by the given multiplier."""
        return n * multiplier

    return multiply
