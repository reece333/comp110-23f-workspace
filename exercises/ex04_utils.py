"""Exercise 4 - List Utility Functions."""
__author__ = "730564969"

def all(int_list, num) -> bool:
    if len(int_list) == 0:
        return False

    index = 0
    while index < len(int_list):
        if int_list[index] - num != 0:
            return False
        index += 1
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max_value = input[0]
    index = 1

    while index < len(input):
        current_value = input[index]
        if current_value - max_value > 0:
            max_value = current_value
        elif current_value - max_value < 0:
            max_value = max_value
        index += 1

    return max_value

def is_equal(int_list1, int_list2) -> bool:
    if len(int_list1) != len(int_list2):
        return False

    index = 0
    while index < len(int_list1):
        if int_list1[index] != int_list2[index]:
            return False
        index += 1

    return True