"""
04/03/2025: J. BRANCH

Goal is to create an implementation for a simple HashMap data structure from 'scratch'.

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


def main() -> None:
    hashmap = HashMap()
    kv_pairs = [("key1", 1000), (12, "John Doe"), ((3,4), "Tony Stark"), ("key1", [234, 456, 789, "JB"])]

    print("\n-------------------- Adding k-v pairs to hashmap --------------------")
    print(f"Adding key={kv_pairs[0][0]}, value={kv_pairs[0][1]})...")
    hashmap.add(key=kv_pairs[0][0], value=kv_pairs[0][1])

    print(f"Adding key={kv_pairs[1][0]}, value={kv_pairs[1][1]})...")
    hashmap.add(key=kv_pairs[1][0], value=kv_pairs[1][1])

    print(f"Adding key={kv_pairs[2][0]}, value={kv_pairs[2][1]})...")
    hashmap.add(key=kv_pairs[2][0], value=kv_pairs[2][1])

    print(f"Adding key={kv_pairs[3][0]}, value={kv_pairs[3][1]})...")
    hashmap.add(key=kv_pairs[3][0], value=kv_pairs[3][1])


    print("\n-------------------- Printing out k-v pairs --------------------")
    hashmap.print_kv_pairs()

    print("\n-------------------- Getting values from hashmap --------------------")
    print(f"Searching hashmap for key={34}, this should return None... {hashmap.get(key=34)}", # should return None
        f"Searching hashmap for key={kv_pairs[0][0]}... {hashmap.get(key=kv_pairs[0][0])}",
        f"Searching hashmap for key={kv_pairs[1][0]}... {hashmap.get(key=kv_pairs[1][0])}",
        f"Searching hashmap for key={kv_pairs[2][0]}... {hashmap.get(key=kv_pairs[2][0])}",
        f"Searching hashmap for key={kv_pairs[3][0]}... {hashmap.get(key=kv_pairs[3][0])}",
        sep="\n"
    )

    print("\n-------------------- Deleting values from hashmap --------------------")
    print(f"Attempting to delete k-v pair associated with key={kv_pairs[0][0]}, value={34}... this should not result in a succesful deletion")
    hashmap.delete(key=kv_pairs[0][0], target_value=34)
    hashmap.print_kv_pairs()

    print(f"Attempting to delete k-v pair associated with key={kv_pairs[0][0]}, value={kv_pairs[0][1]}... this should result in a successful deletion")
    hashmap.delete(key=kv_pairs[0][0], target_value=kv_pairs[0][1])
    hashmap.print_kv_pairs()

    print(f"Attempting to delete k-v pair associated with key={kv_pairs[1][0]}... this should result in a successful deletion")
    hashmap.delete(key=kv_pairs[1][0])
    hashmap.print_kv_pairs()

    print(f"Attempting to delete k-v pair associated with key={kv_pairs[2][0]}... this should result in a successful deletion")
    hashmap.delete(key=kv_pairs[2][0])
    hashmap.print_kv_pairs()

    print(f"Attempting to delete k-v pair associated with key={kv_pairs[3][0]}... this should result in a successful deletion")
    hashmap.delete(key=kv_pairs[3][0])
    hashmap.print_kv_pairs()


if __name__ == "__main__":
    main()