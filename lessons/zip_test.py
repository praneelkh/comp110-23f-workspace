"""Test my zip function."""

__author__ = "730663941"


from lessons.zip import zip 


def test_zip_with_empty_list():
    """Test the edge case when one of the input lists is empty."""
    key = []
    value = [1, 2, 3]
    expected = {}
    result = zip(key, value)
    assert result == expected


def test_zip_with_same_length_lists():
    """Test the use case when both lists have the same number of elements."""
    key = ["a", "b", "c"]
    value = [1, 2, 3]
    expected = {"a": 1, "b": 2, "c": 3}
    result = zip(key, value)
    assert result == expected


def test_zip_with_different_length_lists():
    """Test the use case when the lists have a different number of elements."""
    key = ["a", "b"]
    value = [1, 2, 3]
    expected = {}
    result = zip(key, value)
    assert result == expected