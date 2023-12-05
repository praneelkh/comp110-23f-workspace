"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730663941"


class Simpy:
    """Simpy object."""
    values: list[float]

    def __init__(self, vals: list[float]):
        """Constructing Simpy object."""
        self.values = vals

    def __str__(self) -> str:
        """Returns str in a format of Simpy(...)."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, num_vals: int) -> None:
        """Fills values of Simpy list."""
        self.values = [val] * num_vals
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills values similar to the range function."""
        assert step != 0.0
        next_val: float = start + step
        self.values.append(start)
        while next_val != stop:
            self.values.append(next_val)
            next_val += step
        return None
    
    def sum(self) -> float: 
        """Sums all the values in the list."""  
        sum: float = 0
        for val in self.values:
            sum += val
        return sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload addition."""
        new_simpy: Simpy = Simpy([])
        if type(rhs) is float:
            for val in self.values:
                new_simpy.values.append(val + rhs)
            return new_simpy
        else: 
            for i in range(len(rhs.values)):
                new_simpy.values.append(self.values[i] + rhs.values[i])
            return new_simpy
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload exponents."""
        new_simpy: Simpy = Simpy([])
        if type(rhs) is float:
            for val in self.values:
                new_simpy.values.append(val ** rhs)
            return new_simpy
        else: 
            for i in range(len(rhs.values)):
                new_simpy.values.append(self.values[i] ** rhs.values[i])
            return new_simpy
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload equality."""
        bool_list: list[bool] = []
        if type(rhs) is float:
            for val in self.values:
                if val == rhs:
                    bool_list.append(True)
                else: 
                    bool_list.append(False)
            return bool_list
        else: 
            for i in range(len(rhs.values)):
                if self.values[i] == rhs.values[i]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
        
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload greater than."""
        bool_list: list[bool] = []
        if type(rhs) is float:
            for val in self.values:
                if val > rhs:
                    bool_list.append(True)
                else: 
                    bool_list.append(False)
            return bool_list
        else: 
            for i in range(len(rhs.values)):
                if self.values[i] > rhs.values[i]:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload subscription notation."""
        if type(rhs) is int:
            return self.values[rhs]
        else:
            filter_simpy: Simpy = Simpy([])
            for i in range(len(rhs)):
                if rhs[i] is True:
                    filter_simpy.values.append(self.values[i])
            return filter_simpy