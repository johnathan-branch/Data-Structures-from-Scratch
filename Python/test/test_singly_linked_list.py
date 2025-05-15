from src.singly_linked_list import SinglyLinkedList

test_vals = (10, 20, 30)
extended_test_vals = (10, 20, 30, 40, 50, 60)

def test_append():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        assert linkedlist.append(val) == None

    for idx, val in enumerate(test_vals):
        assert linkedlist.get(idx) == val

    del linkedlist

def test__len__():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        linkedlist.append(val)

    assert len(linkedlist) == len(test_vals)

    del linkedlist

def test_to_list():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        linkedlist.append(val)

    list_from_linkedlist = linkedlist.to_list()

    assert type(list_from_linkedlist) is list
    assert len(list_from_linkedlist) == len(test_vals)

    del linkedlist
    
def test__iter__():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        linkedlist.append(val)

    for idx, node in enumerate(linkedlist):
        assert node.value == test_vals[idx]

    del linkedlist

def test__repr__():
    linkedlist = SinglyLinkedList()

    assert type(repr(linkedlist)) == str
    assert len(repr(linkedlist)) > 0

    del linkedlist

def test_prepend():
    linkedlist = SinglyLinkedList()
    local_test_vals = list(test_vals)

    for val in local_test_vals:
        assert linkedlist.prepend(val) == None
    
    local_test_vals.reverse()

    for idx, val in enumerate(local_test_vals):
        assert linkedlist.get(idx) == val

    del linkedlist

def test_insert():
    linkedlist = SinglyLinkedList()

    assert linkedlist.append("initial value") == None

    for idx, val in enumerate(test_vals):
        assert linkedlist.insert(idx, val) == None
    
    for idx, val in enumerate(test_vals):
        assert linkedlist.get(idx) == val
    
    del linkedlist

def test_remove():
    linkedlist = SinglyLinkedList()
    num_deletions = 0

    for val in extended_test_vals:
        linkedlist.append(val)

    # test condition 1: remove the first node in the list (index=0)
    assert linkedlist.remove(0) == None
    num_deletions += 1

    # test condition 2: remove an arbitrary located node (index = 2)
    assert linkedlist.remove(2) == None
    num_deletions += 1

    # test condition 3: remove the last node in the list 
    # index = len(vals) - (#of deletions) - 1
    assert linkedlist.remove( (len(extended_test_vals)-2-1) ) == None
    num_deletions += 1
    
    assert len(linkedlist) == len(extended_test_vals) - num_deletions

    del linkedlist

def test_set():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        linkedlist.append(val)
    
    for idx, val in enumerate(test_vals):
        assert linkedlist.set(idx, val+1) == None

    for idx, val in enumerate(test_vals):
        assert linkedlist.get(idx) == val+1

    del linkedlist

def test_find():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        linkedlist.append(val)

    for val in test_vals:
        assert linkedlist.find(val) > -1

    val_not_in_list = 0

    while (val_not_in_list in test_vals):
        val_not_in_list += 1

    assert linkedlist.find(val_not_in_list) == -1

    del linkedlist

def test_contains():
    linkedlist = SinglyLinkedList()

    for val in test_vals:
        linkedlist.append(val)

    for val in test_vals:
        assert linkedlist.contains(val) == True

    val_not_in_list = 0

    while (val_not_in_list in test_vals):
        val_not_in_list += 1

    assert linkedlist.contains(val_not_in_list) == False

    del linkedlist