"""EX07 - Dictionary Unit Tests."""

__author__ = "730663941"


import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# invert unit tests
def test_invert_with_unique_values():
    """USE CASE: Testing on a dictionary with unique key-value pairs."""
    test_dict: dict = {"a": "z", "b": "y", "c": "x"}
    assert invert(test_dict) == {"z": "a", "y": "b", "x": "c"}


def test_invert_with_duplicate_values():
    """USE CASE: Testing on a dictionary to raise a KeyError."""
    with pytest.raises(KeyError):     
        test_dict = {"alyssa": "byrnes", "adam": "byrnes"}
        invert(test_dict)


def test_invert_with_empty_dict():
    """EDGE CASE: Testing on an empty dictionary."""
    test_dict: dict = {}
    assert invert(test_dict) == {}


# favorite_color unit tests
def test_favorite_color_with_winner():
    """USE CASE: Testing when there is a single winner."""
    test_dict: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_with_tie():
    """USE CASE: Testing when there is a tie."""
    test_dict: dict = {"Marc": "yellow", "Ezri": "blue", "Kris": "yellow", "Sam": "blue"}
    assert favorite_color(test_dict) == "yellow"


def test_favorite_color_with_empty_dict():
    """EDGE CASE: Testing when there is a clear winner."""
    test_dict: dict = {}
    assert favorite_color(test_dict) == ""


# count unit tests
def test_count_with_multiple_occurrences():
    """USE CASE: Testing with multiple occurrences of multiple items."""
    test_list: list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    assert count(test_list) == {"apple": 3, "banana": 2, "orange": 1}


def test_count_with_unique_items():
    """USE CASE: Testing with a list of unique items."""
    test_list: list = ["apple", "banana", "orange"]
    assert count(test_list) == {"apple": 1, "banana": 1, "orange": 1}


def test_count_with_empty_list():
    """EDGE CASE: Testing with an empty list."""
    test_list: list = []
    assert count(test_list) == {}


# alphabetizer unit tests
def test_alphabetizer_with_multiple_words():
    """USE CASE: Test with a list of all lowercase words to categorize under multiple keys."""
    test_list: list = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test_list) == {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "bad"]}


def test_alphabetizer_with_mixed_cases():
    """USE CASE: Test with a list of words starting with both uppercase and lowercase letters."""
    test_list: list = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(test_list) == {"p": ["Python", "party"], "s": ["sugar"], "t": ["Turtle", "table"]}


def test_alphabetizer_with_empty_list():
    """EDGE CASE: Test with an empty list."""
    test_list: list = []
    assert alphabetizer(test_list) == {}


# update_attendance unit tests
def test_update_attendance_existing_day():
    """USE CASE: Test updating an existing day with an additional student."""
    test_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_log, "Tuesday", "Vrinda") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}


def test_update_attendance_new_day():
    """USE CASE: Test adding a new day and a student."""
    test_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(test_log, "Wednesday", "Kaleb") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Kaleb"]}


def test_update_attendance_duplicate_student():
    """EDGE CASE: Test that the same student is not added twice for the same day."""
    test_log = {"Monday": ["Vrinda", "Kaleb"]}
    assert update_attendance(test_log, "Monday", "Kaleb") == {"Monday": ["Vrinda", "Kaleb"]}