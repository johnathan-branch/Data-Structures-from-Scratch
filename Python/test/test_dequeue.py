from src.dequeue import Dequeue

TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)

def test_enqueue_and_dequeue():
    dequeue = Dequeue()

    for val in TEST_VALS:
        assert dequeue.enqueue(val) is None

    for val in TEST_VALS:
        assert dequeue.dequeue() == val

    del dequeue


def test_peek():
    dequeue = Dequeue()

    for val in TEST_VALS:
        dequeue.enqueue(val)
    
    for val in TEST_VALS:
        assert dequeue.peek() == val
        dequeue.dequeue()
        
    del dequeue

def test_enqueue_front_and_dequeue_back():
    dequeue = Dequeue()

    for val in TEST_VALS:
        assert dequeue.enqueue_front(val) is None
    
    for val in TEST_VALS:
        assert dequeue.dequeue_back() == val

    del dequeue

def test_peek_back():
    dequeue = Dequeue()

    for val in TEST_VALS:
        dequeue.enqueue_front(val)
    
    for val in TEST_VALS:
        assert dequeue.peek_back() == val
        dequeue.dequeue_back()
        
    del dequeue

def test_is_empty():
    dequeue = Dequeue()

    assert dequeue.is_empty() is True
    dequeue.enqueue(1)
    assert dequeue.is_empty() is False

    del dequeue

def test__len__():
    dequeue = Dequeue()

    for val in TEST_VALS:
        dequeue.enqueue(val) == None

    assert len(dequeue) == len(TEST_VALS)

    del dequeue

def test__iter__():
    dequeue = Dequeue()

    for val in TEST_VALS:
        dequeue.enqueue(val)

    for idx, val in enumerate(dequeue):
        assert val == TEST_VALS[idx]

    del dequeue

def test__repr__():
    dequeue = Dequeue()

    assert type(repr(dequeue)) is str
    assert len(repr(dequeue)) > 0

    del dequeue