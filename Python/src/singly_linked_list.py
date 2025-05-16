""" 
05/03/2025: J. BRANCH

The goal is to create an implementation for a singly LinkedList data structure from 'scratch'.

Plan:
    - Datamodel: 
        (class) SinglyLinkedList 
        (class) Node
        
        LinkedList
            |
           head --> Node[value|next --> Node[value|next --> ... --> Node[value|None] 
    
    - Node class (data-only class)
        - contains a member to store a node value 
        - contains a member to store a reference to the next node
    
    - SinglyLinkedList class
        - contains a head member that is either None or points to the first node in the linkedlist
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
    
            5. get(self, index: int): Returns the value of the node at the specified index
                return: Any
    
            6. set(self, index: int, value: Any): Updates the value at the specified index
                return: None
    
            7. find(self, value: Any): Returns the index of the first occurence of value, if not found returns -1
                return: int
    
            8. contains(self, value: Any): Returns true if the specified value is in the linkedlist, otherwise returns False
                return: bool
    
            9. to_list(self, return_nodes: bool = False): Returns a Python list of the linkedlist node values (default) or nodes
                return: list[Any]
    
            10. __len__(self): Dunder method to implement len(linkedlist obj) functionality
                return: int
    
            11. __iter__(self): Dunder method to make linkedlist objects iterable, e.g. allows object to be iterated over for-loops
                return: iterator
    
            12. __repr__(self): Dunder method to implement repr(linkedlist obj) functionality
                return: str
    
        - Internal Methods:
            
            13. _get_node(self, index: int): Return the node specified at index
                return: Node
    
            14. _validate_index(self, index: int): Returns True if the Node is in valid bounds, otherwise returns False
                return: bool
    
            15. _is_empty(self): Returns True if the linkedlist is empty, otherwise returns False
                return: bool
    
            16. _get_last_node(self): Returns the last node in the linkedlist
                return: Node
"""

from typing import Any
import copy

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value: Any) -> None:
        """Creates and inserts a new node at the end of the linkedlist"""
        if (self._is_empty()):
            self.head = Node(value)
            self.length += 1
            return
        else:
            prev_node = self._get_last_node()
            prev_node.next = Node(value)
            self.length += 1
            return

    def prepend(self, value: Any) -> None:
        """Creates and inserts a new node at the beginning of the linkedlist"""
        if (self._is_empty()):
            self.head = Node(value)
            self.length += 1
            return
        else:
            new_head_node = Node(value)
            new_head_node.next = self.head
            self.head = new_head_node
            self.length += 1 
            return
        
    def insert(self, index: int, value: Any) -> None:
        """Creates and inserts a new node at the specified index (note - use append method to insert new node at the end)"""
        if (not self._validate_index(index)):
            raise IndexError("Invalid index")
        
        if (index == 0):
            self.prepend(value)
            return
        else:
            prev_node = self._get_node(index-1)
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1
            return
        
    def remove(self, index: int) -> None: 
        """Removes node at specified index"""
        if (not self._validate_index(index)):
            raise IndexError("Error, invalid index specified")
        
        if (index == 0):
            node_to_delete = self.head
            self.head = self.head.next
            del node_to_delete
            self.length -= 1
            return
        elif (index < self.length - 1):
            prev_node = self._get_node(index-1)
            node_to_delete = self._get_node(index)
            next_node = self._get_node(index+1)
            prev_node.next = next_node
            del node_to_delete
            self.length -= 1
            return
        else:
            prev_node = self._get_node(index-1)
            node_to_delete = self._get_node(index)
            prev_node.next = None
            del node_to_delete
            self.length -= 1
            return
        
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
        return f"class_name=SinglyLinkedList, id={id(self)}, length={self.length}, head={self.head}"

    def _get_node(self, index: int) -> Node | None:
        """Return the node specified at index"""
        if (not self._validate_index(index)):
            return None
        
        retrieved_node = self.head

        for _ in range(index):
            retrieved_node = retrieved_node.next

        return retrieved_node

    def _validate_index(self, index: int) -> bool:
        """Returns True if the Node is in valid bounds, otherwise returns False"""
        if (index > -1 and index < self.length):
            return True
        else:
            return False

    def _is_empty(self) -> bool:
        """Returns True if the linkedlist is empty, otherwise returns False"""
        if (self.head is None):
            if (self.length == 0):
                return True
            else:
                raise ValueError("Error, head is assigned to None but length is non-zero")
        else:
            if (self.length > 0):
                return False
            else:
                raise ValueError("Error, head is not None but length is less than or equal to zero")

    def _get_last_node(self) -> Node | None:
        """ Returns the last node in the linkedlist"""
        if (self._is_empty()):
            return None
        else:
            return self._get_node(index=self.length-1)