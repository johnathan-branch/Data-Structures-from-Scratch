""" 
05/22/2025: J. BRANCH

The goal is to create an implementation for a double-ended Queue data structure from 'scratch'.

Plan:
    - Datamodel: 
        (composite class) Dequeue
        (composite class) DoublyLinkedList
        (class) Node
        
          Dequeue
            |
        DoublyLinkedList
            |
           head --> <--[prev][Node(value)][next]--> <--[prev][Node(value)][next]--> <--...--> <-- tail 
    
    - Node class (data-only class)
        - contains a member to store a node value 
        - contains a member to store a reference to the next node
    
    - DoublyLinkedList class
        - contains a head member that is either None or points to the first node in the linkedlist
        - contains a tail member that is either None or points to the last node in the linkedlist
        - contains a length member that keeps track of the current length of the linkedlist
        - read internal docs for API info

    -Deueue class
        -contains a DoublyLinkedList member used as the underlying data structure for the Dequeue

        - Public Methods:
            1. enqueue(self, value: Any): Adds an element to the back of the queue
                return: None 

            2. enqueue_front(self, value: Any): Adds an element to the front of the queue
                return: None 
            
            3. dequeue(self): Removes and returns the value from the front of the queue, raises IndexError if empty
                return: Any

            4. dequeue_back(self): Removes and returns the value from the back of the queue, raises IndexError if empty
                return: Any

            5. peek(self): Returns the value from the front of the queue without removing it, raises IndexError if empty
                return: Any

            6. peek_back(self): Returns the value from the back of the queue without removing it, raises IndexError if empty
                return: Any
    
            7. is_empty(self): Returns True if the queue is empty, otherwise returns False
                return: bool
    
            8. __len__(self): Dunder method to implement len(linkedlist obj) functionality
                return: int
    
            9. __iter__(self): Dunder method to make linkedlist objects iterable, e.g. allows object to be iterated over for-loops
                return: iterator
    
            10. __repr__(self): Dunder method to implement repr(linkedlist obj) functionality
                return: str
    
        - Internal Methods:
            11. _validate_not_empty(self): Internal helper method used to validate if queue is currently non-empty
                return: bool
"""
from typing import Any

if __name__ == "__main__":
    from doubly_linked_list import DoublyLinkedList
else:
    from src.doubly_linked_list import DoublyLinkedList

class Dequeue:
    def __init__(self):
        self.list = DoublyLinkedList()
    
    def enqueue(self, value: Any) -> None:
        """Adds an element to the back of the queue"""
        self.list.append(value)
        return None
    
    def enqueue_front(self, value: Any) -> None:
        """Adds an element to the front of the queue"""
        self.list.prepend(value)
        return None

    def dequeue(self) -> Any:
        """Removes and returns the value from the front of the queue, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot dequeue from an empty queue.")
        value : Any = self.list.get(0)
        self.list.remove(0)
        return value
    
    def dequeue_back(self) -> Any:
        """Removes and returns the value from the back of the queue, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot dequeue from an empty queue.")
        value : Any = self.list.get(self.list.length-1)
        self.list.remove(self.list.length-1)
        return value

    def peek(self) -> Any:
        """Returns the value from the front of the queue without removing it, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot peek from an empty queue.")
        value : Any = self.list.get(0)
        return value
    
    def peek_back(self) -> Any:
        """Returns the value from the back of the queue without removing it, raises IndexError if empty"""
        if not (self._validate_not_empty()):
            raise IndexError("Cannot peek from an empty queue.")
        value : Any = self.list.get(self.list.length-1)
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
        return f"class_name=Dequeue, id={id(self)}, length={len(self.list)}, front={self.list.get(0)}"

    def _validate_not_empty(self) -> bool:
        """Internal helper method used to validate if queue is currently non-empty"""
        return not (self.list._is_empty()) # True -> not empty

#--------------------------------------------------------
def _functional_test_script_01():
    print("------------", "This script tests the normal single-ended queue operations")

    TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)
    dequeue = Dequeue()

    print("\n", f"Is dequeue empty: {dequeue.is_empty()}")
    
    print(f"Attempting to enqueue value in the back: {123456}")
    dequeue.enqueue(123456)
    print(f"Value returned from dequeue.peek(): {dequeue.peek()}")
    print(f"Value returned from dequeue.dequeue(): {dequeue.dequeue()}", "\n")

    for val in TEST_VALS:
        print(f"Attempting to enqueue value in the back: {val}")
        dequeue.enqueue(val)   

    print("\n", repr(dequeue))
    print(f"Is dequeue empty: {dequeue.is_empty()}", "\n")
    
    for _ in dequeue:
        print(f"Attempting to dequeue value from the front: {dequeue.dequeue()}")

    print("test execution complete, cleaning up", "\n")
    del dequeue

    

def _functional_test_script_02():
    print("------------", "This script tests the double-ended queue operations")
    
    TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)
    dequeue = Dequeue()

    print("\n", f"Is dequeue empty: {dequeue.is_empty()}")
    
    print(f"Attempting to enqueue value in the front: {123456}")
    dequeue.enqueue_front(123456)
    print(f"Value returned from dequeue.peek_back(): {dequeue.peek_back()}")
    print(f"Value returned from dequeue.dequeue_back(): {dequeue.dequeue_back()}", "\n")

    for val in TEST_VALS:
        print(f"Attempting to enqueue value in the front: {val}")
        dequeue.enqueue_front(val)   

    print("\n", repr(dequeue))
    print(f"Is dequeue empty: {dequeue.is_empty()}", "\n")
    
    for _ in dequeue:
        print(f"Attempting to dequeue value from the back: {dequeue.dequeue_back()}")

    print("test execution complete, cleaning up", "\n")
    del dequeue

if __name__ == "__main__":
    _functional_test_script_01()
    _functional_test_script_02()