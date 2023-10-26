"""Summing the elements of a list using different loops."""
__author__ = "730564969"


def w_sum(vals: list[float]) -> float:
    """Version A: while loop."""
    sum = 0.0
    idx = 0
    while idx < len(vals):
        sum += vals[idx]  
        idx += 1  
    return sum


def f_sum(vals: list[float]) -> float: 
    """Version B: for... in... loop."""
    sum = 0.0
    for val in vals:
        sum += val
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Version C: for... in range loop."""
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum