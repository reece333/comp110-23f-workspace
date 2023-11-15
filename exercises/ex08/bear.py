"""File to define Bear class."""


class Bear:
    """Bear class."""
    
    def __init__(self):
        """Bear constructor."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Simulate one day of bear's life."""
        self.age += 1
        self.hunger_score -= 1  # Decrease the hunger score by 1

    def eat(self, num_fish: int):
        """Update the Bear's hunger_score based on the number of fish eaten."""
        self.hunger_score += num_fish