"""File to define River class."""

__author__ = "730663941"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River: 
    """River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
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

    def check_ages(self) -> None:
        """Checks ages for fish and bear."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Method for removing fish."""
        for i in range(amount):
            self.fish.pop(i)  
        return None

    def bears_eating(self):
        """Method for bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self) -> None:
        """Checks hunger of bears."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears 
        return None
        
    def repopulate_fish(self):
        """Method for repopulating fish."""
        for i in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Method for repopulating bears."""
        for i in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Method to view river simulation."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
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
    
    def one_river_week(self) -> None:
        """Simulates seven river days."""
        for i in range(1, 8):
            self.one_river_day()