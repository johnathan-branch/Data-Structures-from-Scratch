""" 
05/19/2025: J. BRANCH

The goal is to create an implementation for a Stack data structure from 'scratch'.

Plan:
    - Datamodel: 
        (composite class) Stack
        (composite class) SinglyLinkedList
        (class) Node
        
          Stack
            |
        LinkedList
            |
           head --> Node[value|next --> Node[value|next --> ... --> Node[value|None] 
    
    - Node class (data-only class)
        - contains a member to store a node value 
        - contains a member to store a reference to the next node
    
    - SinglyLinkedList class
        - contains a head member that is either None or points to the first node in the linkedlist
        - contains a length member that keeps track of the current length of the linkedlist
        - read internal docs for API info

    - Stack class
        -contains a SinglyLinkedList member used as the underlying data structure for the Stack

        - Public Methods:
            1. push(self, value: Any): Creates and inserts a new value into the stack
                return: None 
            
            2. pop(self): Removes and returns the top value from the stack, raises IndexError if empty
                return: Any

            3. peek(self): Returns the top value without removing it from the stack, raises IndexError if empty
                return: Any
    
            4. is_empty(self): Returns True if the stack is empty, otherwise returns False
                return: bool
    
            5. __len__(self): Dunder method to implement len(linkedlist obj) functionality
                return: int
    
            6. __iter__(self): Dunder method to make linkedlist objects iterable, e.g. allows object to be iterated over for-loops
                return: iterator
    
            7. __repr__(self): Dunder method to implement repr(linkedlist obj) functionality
                return: str
    
        - Internal Methods:
            8. _validate_not_empty(self): Internal helper method used to validate if stack is currently non-empty
                return: bool
"""
from typing import Any
from src.singly_linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self.list = SinglyLinkedList()
    
    def push(self, value: Any) -> None:
        """Creates and inserts a new value into the stack"""
        self.list.prepend(value)
        return None

    def pop(self) -> Any:
        """Removes and returns the top value from the stack, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot pop from an empty stack.")
        value : Any = self.list.get(0)
        self.list.remove(0)
        return value

    def peek(self) -> Any:
        """Returns the top value without removing it from the stack, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot peek from an empty stack.")
        value : Any = self.list.get(0)
        return value

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, otherwise returns False"""
        return self.list._is_empty()

    def __len__(self) -> int:
        """Dunder method to implement len(obj) functionality"""
        return len(self.list)

    def __iter__(self):
        """
        Dunder method to make object iterable, e.g. allows object to be iterated over for-loops
        Note: Iteration implementation returns the element at the top of the stack first and iterates to the bottom of the stack
        """
        return (node.value for node in self.list) 
    
    def __repr__(self) -> str:
        """Dunder method to implement repr(obj) functionality"""
        return f"class_name=Stack, id={id(self)}, length={len(self.list)}, top={self.list.get(0)}"

    def _validate_not_empty(self) -> bool:
        """Internal helper method used to validate if stack is currently non-empty"""
        return not (self.list._is_empty()) # True -> not empty