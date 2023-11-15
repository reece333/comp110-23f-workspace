"""File to define River class."""
__author__ = "730564969"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River class."""
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove old Fish and Bears from the River."""
        surviving_bears = []
        surviving_fish = []

        # Check the age of each Bear
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)

        # Check the age of each Fish
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)

        # Update the river's bear and fish populations
        self.bears = surviving_bears
        self.fish = surviving_fish

    def remove_fish(self, amount: int):
        """Remove amount many Fish from the River."""
        # Remove the FRONTMOST Fish (at index 0)
        self.fish = self.fish[amount:]

    def bears_eating(self):
        """Bears eat fish from the river."""
        for bear in self.bears:
            # If there are at least 5 fish in the river, the bear will eat 3 fish
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """Remove hungry Bears from the river."""
        surviving_bears = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)

        # Update the river's bear population
        self.bears = surviving_bears
        
    def repopulate_fish(self):
        """Repopulate fish in the river."""
        num_fish = len(self.fish)
        num_new_fish = (num_fish // 2) * 4

        for _ in range(num_new_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
    
    def repopulate_bears(self):
        """Repopulate bears in the river."""
        num_bears = len(self.bears)
        num_new_bears = num_bears // 2

        for _ in range(num_new_bears):
            new_bear = Bear()
            self.bears.append(new_bear)
    
    def view_river(self):
        """View daily populations of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()