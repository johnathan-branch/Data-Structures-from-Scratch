from src.hashmap import HashMap

def test_hashmap_add_get_delete():
    hashmap = HashMap()
    kv_pairs = [
        ("key1", 1000),
        (12, "John Doe"),
        ((3, 4), "Tony Stark"),
        ("key1", [234, 456, 789, "JB"])
    ]

    # Add key-value pairs
    print("\n-------------------- Adding k-v pairs to hashmap --------------------")
    for key, value in kv_pairs:
        hashmap.add(key=key, value=value)
        print(f"key={key}, value={value}")

    print("\n-------------------- Printing out k-v pairs --------------------")
    hashmap.print_kv_pairs()

    # Test retrieval
    print("\nValidating retrieval from hashmap...")
    assert hashmap.get("nonexistent") is None
    assert hashmap.get(kv_pairs[0][0]) == [kv_pairs[0][1], kv_pairs[3][1]]
    assert hashmap.get(kv_pairs[1][0]) == kv_pairs[1][1]
    assert hashmap.get(kv_pairs[2][0]) == kv_pairs[2][1]

    print("\n-------------------- Deleting values from hashmap --------------------")
    
    # Try deleting a non-matching value
    hashmap.delete(kv_pairs[0][0], target_value=9999)
    print(f"Attempting to delete k-v pair associated with key={kv_pairs[0][0]}, value={9999}... this should not result in a succesful deletion")
    assert hashmap.get(kv_pairs[0][0]) == [kv_pairs[0][1], kv_pairs[3][1]]
    print("\n-------------------- Printing out k-v pairs --------------------")
    hashmap.print_kv_pairs()

    # Delete specific value
    hashmap.delete(kv_pairs[0][0], target_value=kv_pairs[0][1])
    print(f"Attempting to delete k-v pair associated with key={kv_pairs[0][0]}, value={kv_pairs[0][1]}... this should result in a successful deletion")
    assert hashmap.get(kv_pairs[0][0]) == kv_pairs[3][1]

    # Delete the rest
    print(f"Attempting to delete k-v pair associated with key={kv_pairs[1][0]}... this should result in a successful deletion")
    hashmap.delete(kv_pairs[1][0])

    print(f"Attempting to delete k-v pair associated with key={kv_pairs[2][0]}... this should result in a successful deletion")
    hashmap.delete(kv_pairs[2][0])

    print(f"Attempting to delete k-v pair associated with key={kv_pairs[3][0]}... this should result in a successful deletion")
    hashmap.delete(kv_pairs[3][0])

    print("\n-------------------- Printing out k-v pairs --------------------")
    hashmap.print_kv_pairs()