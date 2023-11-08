"""EX 06 - Dictionary Functions."""
__author__ = "730564969"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of given dict."""
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            raise KeyError("Encountered duplicate key!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Given dict containing names and favorite colors, return most popular color."""
    color_count = {} 
    max_count = 0
    most_popular_color = ''

    for name, color in colors.items():
        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1

        if color_count[color] > max_count or (color_count[color] == max_count and most_popular_color == ''):
            most_popular_color = color
            max_count = color_count[color]

    return most_popular_color


def count(items: list[str]) -> dict[str, int]:
    """Count the number of times a value appeared in the input list."""
    count_dict = {}

    for item in items:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetize words into a dict of the letters and the lists of words that belong to that letter."""
    categorized_words = {}

    for word in words:
        initial_letter = word[0].lower()  # Get the initial letter of each word in lowercase
        if initial_letter not in categorized_words:
            categorized_words[initial_letter] = [word]
        else:
            categorized_words[initial_letter].append(word)

    return categorized_words


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Create a dictionary containing days of the week as keys and list of present students as values"""
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
        else:
            print(f"{student} is already marked as present on {day}.")
    else:
        attendance[day] = [student]

    return attendance