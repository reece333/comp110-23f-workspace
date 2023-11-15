"""File for simulating life in the river."""
from exercises.ex08.river import River

# Create a river with 10 Fish and 2 Bears
my_river = River(num_fish=10, num_bears=2)

# Simulate one day in the river
my_river.one_river_day()