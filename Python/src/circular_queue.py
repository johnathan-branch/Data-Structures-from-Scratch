""" 
05/23/2025: J. BRANCH

The goal is to create an implementation for a CircularQueue data structure from 'scratch'.

Plan:
    - Datamodel: 
        (class) CircularQueue
        
        
        CircularQueue
            |
        Python list
            |
   list[0] ... list[capacity-1]

    - CircularQueue class
        - contains a Python list member used as the underlying data structure for the CircularQueue
        - contains a front and rear index pointer for tracking the current front and rear elements of the CircularQueue
        - contains a capacity member tracking the maximum number of elements allowed in the CircularQueue
        - contains a size member tracking the current number of elements enqueued
        - contains an overwrite_if_full member to allow the user to specify if the CircularQueue should overwrite elements if already full

        - Public Methods:
            1. enqueue(self, value: Any): Adds an element at the current index specified by rear
                If overwrite_if_full is True and the end is reached, then rear will wrap around and overwrite the oldest elements first
                If overwrite_if_full is False and the end is reached, then an Overflow error is raised
                return: None 
            
            2. dequeue(self): Removes and returns the element at the current index specified by front
                If empty raised IndexError
                return: Any

            3. peek(self): Returns the value from the front without removing it, raises IndexError if empty
                return: Any
    
            4. is_empty(self): Returns True if empty, otherwise returns False
                return: bool
    
            5. __len__(self): Dunder method to implement len(*obj) functionality
                return: int
    
            6. __iter__(self): Dunder method to make object instances iterable, e.g. allows object instance to be iterated over for-loops
                return: iterator
    
            7. __repr__(self): Dunder method to implement repr(*obj) functionality, e.g. displays size, capacity, front, rear
                return: str
"""
from typing import Any

class CircularQueue:
    def __init__(self, capacity: int, overwrite_if_full: bool = False):
        if (type(capacity) is not int):
            raise TypeError("capacity for the CircularQueue object must be specified as int.")
        if capacity < 1: 
            raise ValueError("capacity for CircularQueue must be non-negative and greater than 0.")
        self.list: list[Any] = [None for _ in range(capacity)] # preallocation of list 
        self.front: int = 0
        self.rear: int = 0
        self.capacity: int = capacity
        self.size: int = 0
        self.overwrite_if_full: bool = overwrite_if_full

    def enqueue(self, value: Any) -> None:
        """Adds an element to the end of the queue"""
        if (value is None):
            raise ValueError("Cannot enqueue None as a value in CircularQueue.")
        if (self.size == self.capacity) and (not self.overwrite_if_full):
            raise OverflowError("Enqueue attempted after size has reached capacity.")
        if (self.list[self.rear] is not None) and (not self.overwrite_if_full):
            raise RuntimeError("Internal error in CircularQueue instance when attempting to enqueue.")
        self.list[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size = min((self.size + 1), self.capacity)
        return None

    def dequeue(self) -> Any:
        """Removes and returns the value from the front of the queue, raises IndexError if empty"""
        if (self.size == 0):
            raise IndexError("Cannot dequeue from an empty queue.")
        value: Any = self.list[self.front]
        self.list[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size = max((self.size - 1), 0)
        return value

    def peek(self) -> Any:
        """Returns the value from the front of the queue without removing it, raises IndexError if empty"""
        if (self.size == 0):
            raise IndexError("Cannot peek from an empty queue.")
        value: Any = self.list[self.front]
        return value

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, otherwise returns False"""
        return self.size == 0

    def __len__(self) -> int:
        """Dunder method to implement len(obj) functionality"""
        return self.size

    def __iter__(self):
        """
        Dunder method to make object iterable, e.g. allows object to be iterated over for-loops
        Note: Iteration implementation returns the element at the front of the queue first and iterates to the end of the queue
        """
        count: int = 0
        current_idx: int = self.front
        upper_limit: int = self.size
        while (count < upper_limit):
            yield self.list[current_idx]
            current_idx = (current_idx + 1) % self.capacity
            count += 1
    
    def __repr__(self) -> str:
        """Dunder method to implement repr(obj) functionality"""
        front_element: Any
        rear_element: Any
        if (self.size == 0):
            front_element = rear_element = None
        else:
            front_element = self.list[self.front]
            if (self.rear == 0):
                rear_element = self.list[self.capacity - 1]
            else:
                rear_element = self.list[self.rear - 1]
        repr_str: str = "class_name=CircularQueue," \
        f" id={id(self)}," \
        f" size={self.size}," \
        f" capacity={self.capacity}," \
        f" front_element={front_element}," \
        f" rear_element={rear_element}"
        return repr_str
    
#--------------------------------------------------------
def _functional_test_script():
    TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)
    capacity_test_tuple = (len(TEST_VALS)-1, len(TEST_VALS), len(TEST_VALS)+1) # cases worth exploring: cap < len(TEST_VALS), cap == len(TEST_VALS) and cap > len(TEST_VALS) 
    overwrite_bool_test_tuple = (False, True)
    
    queue = CircularQueue(capacity=capacity_test_tuple[1], overwrite_if_full=overwrite_bool_test_tuple[0])

    print("\n", f"Is queue empty: {queue.is_empty()}", "\n", f"Attempting to enqueue value: {123456}")
    queue.enqueue(123456)
    print(f"Value returned from queue.peek(): {queue.peek()}", "\n", f"Value returned from queue.dequeue(): {queue.dequeue()}", "\n", repr(queue), "\n")

    for val in TEST_VALS:
        print(f"Attempting to enqueue value: {val}")
        queue.enqueue(val) 
    
    print("\n", f"Is queue empty: {queue.is_empty()}", "\n", repr(queue), "\n")
    
    for _ in queue:
        print(f"Attempting to dequeue value: {queue.dequeue()}")
    
    print("\n", f"Is queue empty: {queue.is_empty()}", "\n", repr(queue))
    del queue

if __name__ == "__main__":
    _functional_test_script()