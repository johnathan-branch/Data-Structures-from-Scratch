"""
04/03/2025: J. BRANCH

The goal is to create an implementation for a HashMap data structure from 'scratch'.

Plan:
    - List datatype used as the container for implementing the hashmap
        - data elements will be stored in an internal list of k-v pairs (tuples)
        - e.g., hashmap = [ [(k1,v1), (k1, v2), ...(k1, vn)], [(k2,v1), (k2, v2), ...(k2, vn)],... ]
    - Hash function will be taking the ASCII sum for the characters in the key and mod'ing it with the size of the list
    - Collisions will be handled with chaining (easy method since python's default mutable collection object is a list)
    - Will create a wrapper class with associated methods for implementing hash functionality

    - Public Methods:
        - add(self, key: ImmutableType, value: Any): Adds the k-v tuple, appends to the list of k-v tuples if entries already exist.
            return: None

        - get(self, key: ImmutableType): Returns the value for the key if it exists, else returns None.
            return: Value(Type: Any) or None(*if key is not found)

        - delete(self, key: ImmutableType, value(*optional)): Removes the key-value pair associated with the key passed into the function.
            If an argument for the optional value param is passed then the deletion only occurs if the value passed in matches the value of a k-v pair.
            Raises KeyError if the key isn't found. 
            return: None(*raises KeyError if key is not found)

        -print_kv_pairs(): Prints all k-v pairs currently in the hashmap.
            return: None

    - Internal Methods:
        - _hashify(self, key): Performs the hashing on the key and returns the hashed value. 
            return: Hash-key(Type: int)
"""
from typing import Union, Any

ImmutableType = Union[str, int, tuple]

class HashMap():

    def __init__(self, size: int = 10):
        self._size:int = size
        self._hashmap: list = [None for _ in range(self._size)] 
    
    def _hashify(self, key: ImmutableType) -> int: 
        if not isinstance(key, (str, int, tuple)):
            raise TypeError
        return (self._hashify_helper_to_ascii(key) % self._size)
        
    def _hashify_helper_to_ascii(self, value: ImmutableType) -> int:
        if isinstance(value, int):
            return ord(chr(value))
        elif isinstance(value, str):
            return sum([ord(char) for char in value])
        elif isinstance(value, tuple):
            intermediate_result = []

            for item in value:
                if isinstance(item, tuple):
                    intermediate_result.extend(self._hashify_helper_to_ascii(value=item))
                else:
                    intermediate_result.append(self._hashify_helper_to_ascii(value=item))
            return sum(intermediate_result)
        else:
            raise TypeError     
    
    def add(self, key: ImmutableType, value: Any) -> None:
        """Adds the k-v tuple, appends to the list of k-v tuples (chaining) if entries already exist for a particular key."""
        hash_key: int = self._hashify(key=key)
        
        if not value: 
            raise ValueError
        
        if self._hashmap[hash_key]:
            self._hashmap[hash_key].append((key,value))
        else:
            self._hashmap[hash_key] = [(key,value)]

        return None

    def get(self, key: ImmutableType) -> Any | None:
        """Returns the value for the key if it exists, else returns None."""
        target_hash_key: int = self._hashify(key=key)
        kv_pairs: Any | None = self._hashmap[target_hash_key] 
        
        if kv_pairs:
            if len(kv_pairs)==1:
                return kv_pairs[0][1]
            values = []    
            for kv in kv_pairs:
                values.append(kv[1])
            return values
        else:
            return None
    
    def delete(self, key: ImmutableType, target_value: Any | None = None) -> None:
        """Removes the key-value pair associated with the key passed into the function.
            If an argument for the optional target_value parameter is passed into the function, then deletion only occurs if the target_value passed in matches the value of a k-v pair.
            If multiple values are chained to a single key, the target_value parameter is required for a deletion to occur.
            This function raises a KeyError if the key is not found in the hashmap. 
        """
        target_hash_key: int = self._hashify(key=key)
        kv_pairs: Any | None = self._hashmap[target_hash_key] 
        target_kv_pair = (key, target_value)
        
        if not kv_pairs:
            raise KeyError
        
        if len(kv_pairs)==1:
            if not target_value:
                self._hashmap[target_hash_key] = None
            else:
                if kv_pairs[0][1] != target_value:
                    pass
                else:
                    kv_pairs = None
        else:
            if not target_value:
                pass
            else:
                if target_kv_pair in kv_pairs:
                    kv_pairs.pop(kv_pairs.index(target_kv_pair))
        return None
        
    def print_kv_pairs(self) -> None:
        for kv_pairs in self._hashmap:
            if kv_pairs:
                print(f"k: {kv_pairs[0][0]}, v: ", end="")
                for idx, kv in enumerate(kv_pairs):
                    if idx == len(kv_pairs)-1:
                        term_char = "\n"
                    else:
                        term_char = ", " 
                    print(kv[1], end=term_char)
        return None