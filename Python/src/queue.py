""" 
05/22/2025: J. BRANCH

The goal is to create an implementation for a Queue data structure from 'scratch'.

Plan:
    - Datamodel: 
        (composite class) Queue
        (composite class) SinglyLinkedList
        (class) Node
        
          Queue
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

    - Queue class
        -contains a SinglyLinkedList member used as the underlying data structure for the Queue

        - Public Methods:
            1. enqueue(self, value: Any): Adds an element to the end of the queue
                return: None 
            
            2. dequeue(self): Removes and returns the value from the front of the queue, raises IndexError if empty
                return: Any

            3. peek(self): Returns the value from the front of the queue without removing it, raises IndexError if empty
                return: Any
    
            4. is_empty(self): Returns True if the queue is empty, otherwise returns False
                return: bool
    
            5. __len__(self): Dunder method to implement len(linkedlist obj) functionality
                return: int
    
            6. __iter__(self): Dunder method to make linkedlist objects iterable, e.g. allows object to be iterated over for-loops
                return: iterator
    
            7. __repr__(self): Dunder method to implement repr(linkedlist obj) functionality
                return: str
    
        - Internal Methods:
            8. _validate_not_empty(self): Internal helper method used to validate if queue is currently non-empty
                return: bool
"""
from typing import Any

if __name__ == "__main__":
    from singly_linked_list import SinglyLinkedList
else:
    from src.singly_linked_list import SinglyLinkedList

class Queue:
    def __init__(self):
        self.list = SinglyLinkedList()
    
    def enqueue(self, value: Any) -> None:
        """Adds an element to the end of the queue"""
        self.list.append(value)
        return None

    def dequeue(self) -> Any:
        """Removes and returns the value from the front of the queue, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot dequeue from an empty queue.")
        value : Any = self.list.get(0)
        self.list.remove(0)
        return value

    def peek(self) -> Any:
        """Returns the value from the front of the queue without removing it, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot peek from an empty queue.")
        value : Any = self.list.get(0)
        return value

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, otherwise returns False"""
        return self.list._is_empty()

    def __len__(self) -> int:
        """Dunder method to implement len(obj) functionality"""
        return len(self.list)

    def __iter__(self):
        """
        Dunder method to make object iterable, e.g. allows object to be iterated over for-loops
        Note: Iteration implementation returns the element at the front of the queue first and iterates to the end of the queue
        """
        return (node.value for node in self.list) 
    
    def __repr__(self) -> str:
        """Dunder method to implement repr(obj) functionality"""
        return f"class_name=Queue, id={id(self)}, length={len(self.list)}, front={self.list.get(0)}"

    def _validate_not_empty(self) -> bool:
        """Internal helper method used to validate if queue is currently non-empty"""
        return not (self.list._is_empty()) # True -> not empty

#--------------------------------------------------------
def _functional_test_script():
    TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)
    queue = Queue()

    print("\n", f"Is queue empty: {queue.is_empty()}")
    
    print(f"Attempting to enqueue value: {123456}")
    queue.enqueue(123456)
    print(f"Value returned from queue.peek(): {queue.peek()}")
    print(f"Value returned from queue.dequeue(): {queue.dequeue()}")
    print()

    for val in TEST_VALS:
        print(f"Attempting to enqueue value: {val}")
        queue.enqueue(val)   

    print("\n", repr(queue))
    print(f"Is queue empty: {queue.is_empty()}", "\n")
    
    for _ in queue:
        print(f"Attempting to dequeue value: {queue.dequeue()}")

    del queue

if __name__ == "__main__":
    _functional_test_script()