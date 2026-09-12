#!/usr/bin/env python3
"""Provides a helper function for calculating pagination index ranges."""


def index_range(page: int, page_size: int) -> tuple:
    """Return the start and end indexes for a given pagination page."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
