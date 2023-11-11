
"""EX04 - Utils."""

__author__ = "730663941"


def all(num_list: list[int], target_num: int) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    if len(num_list) == 0:
        return False
    
    num_list_idx: int = 0
    while num_list_idx < len(num_list):
        if target_num != num_list[num_list_idx]:
            return False
        num_list_idx += 1
    return True


def max(int_list: list[int]) -> int: 
    """The max function is given a list of ints, max should return the largest in the List."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    int_list_idx: int = 0
    max_int: int = int_list[0]
    while int_list_idx < len(int_list):
        if int_list[int_list_idx] > max_int:
            max_int = int_list[int_list_idx]
        int_list_idx += 1
    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    if len(list1) != len(list2):
        return False
    list_idx: int = 0
    while list_idx < len(list1):
        if list1[list_idx] != list2[list_idx]:
            return False
        list_idx += 1
    return True