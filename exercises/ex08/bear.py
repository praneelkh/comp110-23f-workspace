"""File to define Bear class."""


class Bear:
    """Bear class."""
    age: int
    hunger_score: int

    def __init__(self, age_init: int = 0, hunger_score: int = 0) -> None:
        """Initializing Bear attributes."""
        self.age = age_init
        self.hunger_score = hunger_score
        return None
    
    def one_day(self) -> None:
        """Changing bear attributes after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Changing bear attributes when bear eats."""
        self.hunger_score += num_fish
        return None