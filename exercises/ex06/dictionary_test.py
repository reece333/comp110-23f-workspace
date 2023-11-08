"""EX 07 - 'dict' Unit Tests."""
__author__ = "730564969"

import pytest
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Testing invert function
def test_invert_usual_case():
    """Test invert with typical dict."""
    original_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
    inverted = invert(original_dict)
    assert inverted == {'apple': 'a', 'banana': 'b', 'cherry': 'c'}


def test_invert_empty_dict():
    """Test invert with empty dict."""
    original_dict = {}
    inverted = invert(original_dict)
    assert inverted == {}


def test_invert_key_error():
    """Test if invert function raises KeyError for dict with duplicate values."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


# Testing favorite_color function
def test_favorite_color_usual_case():
    """Test favorite_color with typical dict."""
    colors = {'Alice': 'blue', 'Bob': 'green', 'Charlie': 'blue'}
    popular_color = favorite_color(colors)
    assert popular_color == 'blue'


def test_favorite_color_no_colors():
    """Test favorite_color with empty dict."""
    colors = {}
    popular_color = favorite_color(colors)
    assert popular_color == ''


def test_favorite_color_edge_case():
    """Test favorite_color function with a dict having a single color."""
    colors = {'Alice': 'red'}
    popular_color = favorite_color(colors)
    assert popular_color == 'red'


# Testing count function
def test_count_usual_case():
    """Test count with list of repeated elements."""
    items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    counted = count(items)
    assert counted == {'apple': 3, 'banana': 2, 'cherry': 1}


def test_count_empty_list():
    """Test count with empty list."""
    items = []
    counted = count(items)
    assert counted == {}


def test_count_edge_case():
    """Test count with list containing a single element."""
    items = ['apple']
    counted = count(items)
    assert counted == {'apple': 1}


# Testing alphabetizer function
def test_alphabetizer_usual_case():
    """Test alphabetizer with list of words."""
    words = ['apple', 'banana', 'cherry', 'blueberry']
    categorized = alphabetizer(words)
    assert categorized == {'a': ['apple'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}


def test_alphabetizer_empty_list():
    """Test alphabetizer with empty list."""
    words = []
    categorized = alphabetizer(words)
    assert categorized == {}


def test_alphabetizer_edge_case():
    """Test alphabetizer with words starting with the same letter."""
    words = ['apple', 'avocado', 'apricot']
    categorized = alphabetizer(words)
    assert categorized == {'a': ['apple', 'avocado', 'apricot']}


# Testing update_attendance function
def test_update_attendance_usual_case():
    """Test update_attendance with normal attendance update."""
    attendance = {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Charlie']}
    updated_attendance = update_attendance(attendance, 'Monday', 'David')
    assert updated_attendance == {'Monday': ['Alice', 'Bob', 'David'], 'Tuesday': ['Charlie']}


def test_update_attendance_empty_attendance():
    """Test update_attendance with empty attendance dict."""
    attendance = {}
    updated_attendance = update_attendance(attendance, 'Wednesday', 'Alice')
    assert updated_attendance == {'Wednesday': ['Alice']}


def test_update_attendance_edge_case():
    """Test update_attendance with an existing day but no students."""
    attendance = {'Monday': []}
    updated_attendance = update_attendance(attendance, 'Monday', 'Alice')
    assert updated_attendance == {'Monday': ['Alice']}