"""CQ07."""
from __future__ import annotations

__author__ = "730663941"


class Point:
    """Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Assigns the initial values for the attributes x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None: 
        """Updates the x and y attributes by the factor."""
        self.x *= factor
        self.y *= factor
        
    def scale(self, factor: int) -> Point:
        """Returns a new Point with updated x and y attributes."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Magic method to print out points in a readable way!"""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Method to overload the multiplication * operator!"""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point: 
        """Method to overload the addition + operator!"""
        return Point(self.x + factor, self.y + factor)