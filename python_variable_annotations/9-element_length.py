#!/usr/bin/env python3
"""Module containing a function for calculating element lengths."""

from typing import Iterable, List, Sequence, Tuple


def element_length(
        lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """Return each sequence and its length."""
    return [(i, len(i)) for i in lst]
