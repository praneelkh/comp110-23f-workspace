"""Node Class."""

from __future__ import annotations

__author__ = "730663941"


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Returns the data of the first attribute of the list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Returns a linked list of every element except for the head."""
        if self.next is None: 
            return None
        else: 
            return self.next
    
    def last(self) -> int:
        """Returns the data of the last attribute in the list."""
        while self.next is not None:
            self = self.next
        return self.data