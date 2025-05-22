from src.doubly_linked_list import DoublyLinkedList

TEST_VALS = (10, 20, 30, 40, 50, 60)

def test_append():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        assert linkedlist.append(val) is None

    for idx, val in enumerate(TEST_VALS):
        assert linkedlist.get(idx) == val

    del linkedlist

def test__len__():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        linkedlist.append(val)

    assert len(linkedlist) == len(TEST_VALS)

    del linkedlist

def test_to_list():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        linkedlist.append(val)

    list_from_linkedlist = linkedlist.to_list()

    assert type(list_from_linkedlist) is list
    assert len(list_from_linkedlist) == len(TEST_VALS)

    del linkedlist
    
def test__iter__():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        linkedlist.append(val)

    for idx, node in enumerate(linkedlist):
        assert node.value == TEST_VALS[idx]

    del linkedlist

def test__repr__():
    linkedlist = DoublyLinkedList()

    assert type(repr(linkedlist)) is str
    assert len(repr(linkedlist)) > 0

    del linkedlist

def test_prepend():
    linkedlist = DoublyLinkedList()
    local_TEST_VALS = list(TEST_VALS)

    for val in local_TEST_VALS:
        assert linkedlist.prepend(val) is None
    
    local_TEST_VALS.reverse()

    for idx, val in enumerate(local_TEST_VALS):
        assert linkedlist.get(idx) == val

    del linkedlist

def test_insert():
    linkedlist = DoublyLinkedList()

    assert linkedlist.append("initial value") is None

    for idx, val in enumerate(TEST_VALS):
        assert linkedlist.insert(idx, val) is None
    
    for idx, val in enumerate(TEST_VALS):
        assert linkedlist.get(idx) == val
    
    del linkedlist

def test_remove():
    linkedlist = DoublyLinkedList()
    num_deletions = 0

    for val in TEST_VALS:
        linkedlist.append(val)

    # test condition 1: remove the first node in the list (index=0)
    assert linkedlist.remove(0) is None
    num_deletions += 1

    # test condition 2: remove an arbitrary located node (index = 2)
    assert linkedlist.remove(2) is None
    num_deletions += 1

    # test condition 3: remove the last node in the list 
    # index = len(vals) - (#of deletions) - 1
    assert linkedlist.remove( (len(TEST_VALS)-2-1) ) is None
    num_deletions += 1
    
    assert len(linkedlist) == len(TEST_VALS) - num_deletions

    del linkedlist

def test_set():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        linkedlist.append(val)
    
    for idx, val in enumerate(TEST_VALS):
        assert linkedlist.set(idx, val+1) is None

    for idx, val in enumerate(TEST_VALS):
        assert linkedlist.get(idx) == val+1

    del linkedlist

def test_find():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        linkedlist.append(val)

    for val in TEST_VALS:
        assert linkedlist.find(val) > -1

    val_not_in_list = 0

    while (val_not_in_list in TEST_VALS):
        val_not_in_list += 1

    assert linkedlist.find(val_not_in_list) == -1

    del linkedlist

def test_contains():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        linkedlist.append(val)

    for val in TEST_VALS:
        assert linkedlist.contains(val) is True

    val_not_in_list = 0

    while (val_not_in_list in TEST_VALS):
        val_not_in_list += 1

    assert linkedlist.contains(val_not_in_list) is False

    del linkedlist

def test_pop():
    linkedlist = DoublyLinkedList()
    local_TEST_VALS = list(TEST_VALS)

    for val in local_TEST_VALS:
        assert linkedlist.append(val) is None
    
    local_TEST_VALS.reverse()

    for val in local_TEST_VALS:
        assert linkedlist.pop() == val

    assert linkedlist.pop() is None

    del linkedlist

def test_pop_first():
    linkedlist = DoublyLinkedList()

    for val in TEST_VALS:
        assert linkedlist.append(val) is None

    for val in TEST_VALS:
        assert linkedlist.pop_first() == val

    assert linkedlist.pop_first() is None

    del linkedlist