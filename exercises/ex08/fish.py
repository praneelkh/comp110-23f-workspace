"""File to define Fish class."""


class Fish:
    """Fish class."""
    age: int

    def __init__(self, age_init: int = 0) -> None:
        """Initializing Fish attributes."""
        self.age = age_init
        return None
    
    def one_day(self):
        """Changing fish attributes after one day."""
        self.age += 1
        return None