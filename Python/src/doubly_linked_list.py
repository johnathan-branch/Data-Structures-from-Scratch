""" 
05/15/2025: J. BRANCH

The goal is to create an implementation for a doubly LinkedList data structure from 'scratch'.

Plan:
    - Datamodel: 
        (class) DoublyLinkedList 
        (class) Node
        
        DoublyLinkedList
            |
           head --> <--[prev][Node(value)][next]--> <--[prev][Node(value)][next]--> <--...--> <-- tail 
    
    - Node class (data-only class)
        - contains a member to store a node value 
        - contains a memeber to store a reference to the prev node
        - contains a memeber to store a reference to the next node
    
    - DoublyLinkedList class
        - contains a head member that is either None or points to the first node in the linkedlist
        - contains a tail member that is either None or points to the last node in the linkedlist
        - contains a length member that keeps track of the current length of the linkedlist

    - Public Methods:
        1. append(self, value: Any): Creates and inserts a new node at the end of the linkedlist
            return: None 
        
        2. prepend(self, value: Any): Creates and inserts a new node at the beginning of the linkedlist
            return: None

        3. insert(self, index: int, value: Any): Creates and inserts a new node at the specified index
            return: None

        4. remove(self, index: int): Removes node at specified index
            return: None

        5. pop(self): Removes and returns the last element in the linkedlist
            return: Any or None

        6. pop_first(self): Removes and returns the first element in the linkedlist
            return: Any or None
        
        7. get(self, index: int): Returns the value of the node at the specified index
            return: Any

        8. set(self, index: int, value: Any): Updates the value at the specified index
            return: None

        9. find(self, value: Any): Returns the index of the first occurence of value, if not found returns -1
            return: int

        10. contains(self, value: Any): Returns true if the specified value is in the linkedlist, otherwise returns False
            return: bool

        11. to_list(self, return_nodes: bool = False): Returns a Python list of the linkedlist node values (default) or nodes
            return: list[Any]

        12. __len__(self): Dunder method to implement len(linkedlist obj) functionality
            return: int

        13. __iter__(self): Dunder method to make linkedlist objects iterable, e.g. allows object to be iterated over for-loops
            return: iterator

        14. __repr__(self): Dunder method to implement repr(linkedlist obj) functionality
            return: str

    - Internal Methods:
        
        15. _get_node(self, index: int): Return the node specified at index
            return: Node

        16. _validate_index(self, index: int): Returns True if the Node is in valid bounds, otherwise returns False
            return: bool

        17. _is_empty(self): Returns True if the linkedlist is empty, otherwise returns False
            return: bool
"""

from typing import Any
import copy

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: Any) -> None:
        """Creates and inserts a new node at the end of the linkedlist"""
        new_node = Node(value)

        if (self._is_empty()):
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
        return

    def prepend(self, value: Any) -> None:
        """Creates and inserts a new node at the beginning of the linkedlist"""
        new_node = Node(value)

        if (self._is_empty()):
            self.head = self.tail = new_node
        else:    
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        return
        
    def insert(self, index: int, value: Any) -> None:
        """Creates and inserts a new node at the specified index"""
        if (not self._validate_index(index, allow_last_index=True)):
            raise IndexError("Invalid index")
        
        if (index == 0):
            self.prepend(value)
        elif(index == self.length):
            self.append(value)
        else:
            new_node = Node(value)
            prev_node = self._get_node(index-1)
            new_node.prev = prev_node
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.next.prev = new_node
            self.length += 1 
        return

    def remove(self, index: int) -> None: 
        """Removes node at specified index"""
        if (not self._validate_index(index)):
            raise IndexError("Error, invalid index specified")
        
        if (index == 0):
            node_to_delete = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif (index < self.length - 1):
            node_to_delete = self._get_node(index)
            prev_node = node_to_delete.prev
            next_node = node_to_delete.next
            prev_node.next = next_node
            next_node.prev = prev_node
        else:
            node_to_delete = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        del node_to_delete
        self.length -= 1
        return

    def pop(self) -> Any | None:
        """Removes and returns the last element in the linkedlist"""
        if self._is_empty():
            return None
        value = self.tail.value
        self.remove(self.length-1)
        return value
        
    def pop_first(self) -> Any | None:
        """Removes and returns the first element in the linkedlist"""
        if self._is_empty():
            return None
        value = self.head.value
        self.remove(0)
        return value

    def get(self, index: int) -> Any | None:
        """Returns the value of the node at the specified index"""
        retrieved_node = self._get_node(index)
        
        if retrieved_node is None:
            return None
        return retrieved_node.value

    def set(self, index: int, value: Any) -> None:
        """Updates the value at the specified index"""
        if (not self._validate_index(index)):
            raise IndexError("Error, invalid index specified")
        
        retrieved_node = self._get_node(index)
        retrieved_node.value = value
        return

    def find(self, value: Any) -> int:
        """Returns the index of the first occurence of value, if not found returns -1"""
        try:
            return self.to_list().index(value)
        except ValueError:
            return -1

    def contains(self, value: Any) -> bool:
        """Returns true if the specified value is in the linkedlist, otherwise returns False"""
        return (value in self.to_list()) 

    def to_list(self, return_nodes: bool = False) -> list[Any]:
        """Returns a Python list of the linkedlist node values"""
        return_list : list[Any] = []

        for i in range(self.length):
            if (return_nodes):
                return_list.append(copy.deepcopy(self._get_node(index=i)))
            else:
                return_list.append(copy.deepcopy(self._get_node(index=i).value))
        return return_list

    def __len__(self) -> int:
        """Dunder method to implement len(linkedlist obj) functionality"""
        return self.length

    def __iter__(self):
        """Dunder method to make linkedlist objects iterable, e.g. allows object to be iterated over for-loops"""
        return iter(self.to_list(return_nodes=True))

    def __repr__(self) -> str:
        """Dunder method to implement repr(linkedlist obj) functionality"""
        return f"class_name=DoublyLinkedList, id={id(self)}, length={self.length}, head={self.head}, tail={self.tail}"

    def _get_node(self, index: int) -> Node | None:
        """Return the node specified at index"""
        if (not self._validate_index(index)):
            return None
        
        if index < (self.length // 2):
            retrieved_node = self.head 
            for _ in range(index):
                retrieved_node = retrieved_node.next
        else:
            retrieved_node = self.tail 
            for _ in range( (self.length - index - 1) ):
                retrieved_node = retrieved_node.prev
        return retrieved_node

    def _validate_index(self, index: int, allow_last_index = False) -> bool:
        """Returns True if the Node is in valid bounds, otherwise returns False"""
        upper_constraint = self.length

        if allow_last_index: upper_constraint += 1

        if (index > -1 and index < upper_constraint):
            return True
        else:
            return False

    def _is_empty(self) -> bool:
        """Returns True if the linkedlist is empty, otherwise returns False"""
        if (self.head is None and self.tail is None):
            if (self.length == 0):
                return True
            else:
                raise ValueError("Error, either head or tail is assigned to None but length is non-zero")
        else:
            if (self.length > 0):
                return False
            else:
                raise ValueError("Error, either head or tail is not None but length is less than or equal to zero")