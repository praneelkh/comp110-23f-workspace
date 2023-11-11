"""Combining two lists into a dictionary."""

__author__ = "730663941"


def zip(key: list[str], value: list[int]) -> dict[str, int]:
    """Produces a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    if len(key) != len(value) or not key or not value:
        return {}
    dictionary: dict[str, int] = {}
    for i in range(len(key)):
        dictionary[key[i]] = value[i]
    return dictionary