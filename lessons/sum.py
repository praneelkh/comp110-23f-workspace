"""Summing the elements of a list using different loops."""

__author__ = "730663941"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements using a while loop."""
    if len(vals) == 0:
        return 0.0
    i: int = 0 
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all elements using a for loop."""
    if len(vals) == 0:
        return 0.0
    sum: float = 0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements using a for loop with range keyword."""
    if len(vals) == 0:
        return 0.0
    sum: float = 0
    for val in range(len(vals)):
        sum += vals[val]
    return sum