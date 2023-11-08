class Point:
    """A class representing a point with x and y coordinates."""

    def __init__(self, x_init: float, y_init: float):
        """Initializes the Point with x and y coordinates."""
        self.x: float = x_init
        self.y: float = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the point's coordinates by a given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> 'Point':
        """Returns a new Point with scaled coordinates."""
        return Point(self.x * factor, self.y * factor)