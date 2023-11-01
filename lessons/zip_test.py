"""Test my zip function."""
__author__ = "730564969"

from lessons.zip import zip


def test_zip_empty_lists():
    """Test zip with empty lists, should return empty dict. (Edge case)"""
    str_list = []
    int_list = []
    result = zip(str_list, int_list)
    assert result == {}


def test_zip_str_int():
    """Test zip with str and int lists, should combine lists. (Use case)"""
    str_list = ["Happy", "Tuesday", "Python"]
    int_list = [1, 2, 3]
    result = zip(str_list, int_list)
    assert result == {"Happy": 1, "Tuesday": 2, "Python": 3}


def test_zip_unequal_lists():
    """Test zip with unequal len lists, should return empty dict. (Use case)"""
    str_list = ["Apple", "Orange"]
    int_list = [10, 20, 30]
    result = zip(str_list, int_list)
    assert result == {}