from src.stack import Stack

TEST_VALS = (-100, -10, 0, 10, 20, 30, 40, 50, 60)

def test_push_and_pop():
    stack = Stack()
    local_test_vals = list(TEST_VALS)

    for val in TEST_VALS:
        assert stack.push(val) is None

    local_test_vals.reverse()

    for val in local_test_vals:
        assert stack.pop() == val

    del stack

def test_peek():
    stack = Stack()

    for val in TEST_VALS:
        assert stack.push(val) is None
        assert stack.peek() == val

    del stack

def test_is_empty():
    stack = Stack()

    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

    del stack

def test__len__():
    stack = Stack()

    for val in TEST_VALS:
        stack.push(val) == None

    assert len(stack) == len(TEST_VALS)

    del stack

def test__iter__():
    stack = Stack()
    local_test_vals = list(TEST_VALS)

    for val in TEST_VALS:
        stack.push(val)

    local_test_vals.reverse()

    for idx, val in enumerate(stack):
        assert val == local_test_vals[idx]

    del stack

def test__repr__():
    stack = Stack()

    assert type(repr(stack)) is str
    assert len(repr(stack)) > 0

    del stack