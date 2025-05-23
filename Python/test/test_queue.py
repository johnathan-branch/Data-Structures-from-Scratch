from src.queue import Queue

TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)

def test_enqueue_and_dequeue():
    queue = Queue()

    for val in TEST_VALS:
        assert queue.enqueue(val) is None

    for val in TEST_VALS:
        assert queue.dequeue() == val

    del queue

def test_peek():
    queue = Queue()

    for val in TEST_VALS:
        queue.enqueue(val)
    
    for val in TEST_VALS:
        assert queue.peek() == val
        queue.dequeue()
        

    del queue

def test_is_empty():
    queue = Queue()

    assert queue.is_empty() is True
    queue.enqueue(1)
    assert queue.is_empty() is False

    del queue

def test__len__():
    queue = Queue()

    for val in TEST_VALS:
        queue.enqueue(val) == None

    assert len(queue) == len(TEST_VALS)

    del queue

def test__iter__():
    queue = Queue()

    for val in TEST_VALS:
        queue.enqueue(val)

    for idx, val in enumerate(queue):
        assert val == TEST_VALS[idx]

    del queue

def test__repr__():
    queue = Queue()

    assert type(repr(queue)) is str
    assert len(repr(queue)) > 0

    del queue