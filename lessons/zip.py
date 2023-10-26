"""Combining 2 lists into a dictionary."""
__author__ = "730564969"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Zip 2 lists into a dictionary."""
    if len(str_list) != len(int_list):
        return {}
    else:
        result = {}
        idx = 0  # Initialize the index
        while idx < len(str_list):
            result[str_list[idx]] = int_list[idx]
            idx += 1  # Increment the index
        return result
    
    
example_usage = zip(["Happy", "Tuesday"], [1, 2])

print(example_usage)