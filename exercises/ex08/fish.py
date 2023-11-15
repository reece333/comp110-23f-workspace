"""File to define Fish class."""


class Fish:
    """Fish class."""
    
    def __init__(self):
        """Fish contructor."""
        self.age = 0
    
    def one_day(self):
        """Simulate one day of fish life."""
        self.age += 1