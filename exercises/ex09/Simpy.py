"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730564969"


class Simpy:
    """A utility class for numerical operations."""
    
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initialize Simpy object with a list of floats."""
        self.values = values

    def __str__(self) -> str:
        """Return string representation of Simpy object."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, count: int) -> None:
        """Fill Simpy object's values with a specific number of repeating values."""
        self.values = [value] * count
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill Simpy object's values with a range of values."""
        assert step != 0.0, "Step cannot be 0.0"

        current_value = start
        while (step > 0 and current_value < stop) or (step < 0 and current_value > stop):
            self.values.append(current_value)
            current_value += step
    
    def sum(self) -> float:
        """Compute and return the sum of all values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Implement the addition operator for Simpy objects and floats."""
        result = Simpy([])

        if isinstance(rhs, float):
            result.values = [item + rhs for item in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Objects must have equal lengths for addition"
            result.values = [self.values[i] + rhs.values[i] for i in range(len(self.values))]

        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Implement the power operator for Simpy objects and floats."""
        result = Simpy([])

        if isinstance(rhs, float):
            result.values = [self.values[i] ** rhs for i in range(len(self.values))]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Objects must have equal lengths for exponentiation"
            result.values = [self.values[i] ** rhs.values[i] for i in range(len(self.values))]

        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Implement the equality operator for Simpy objects and floats."""
        result = []

        if isinstance(rhs, float):
            result = [item == rhs for item in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Objects must have equal lengths for equality comparison"
            result = [self.values[i] == rhs.values[i] for i in range(len(self.values))]

        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Implement the greater than operator for Simpy objects and floats."""
        result = []

        if isinstance(rhs, float):
            result = [item > rhs for item in self.values]
        elif isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Objects must have equal lengths for greater than comparison"
            result = [self.values[i] > rhs.values[i] for i in range(len(self.values))]

        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Implement the subscription operator for reading specific items or filtering with a mask."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list):
            assert len(self.values) == len(rhs), "Simpy object and mask must have equal lengths"
            return Simpy([self.values[i] for i in range(len(self.values)) if rhs[i]])