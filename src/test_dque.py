"Test the functions in dequeue"
import pytest


@pytest.fixture
def dq():
    from dque import Dque
    new_dq = Dque()
    return new_dq


def test_init(dq):
    """Test init of dequeue."""
    assert dq.head is None
    assert dq.tail is None
    assert dq.next_node is None
    assert dq.pre_node is None
    assert dq.value is None
    assert dq.len == 0


def test_append(dq):
    """Test append adds to end of dequeue."""
    dq.append(293)
    assert dq.tail.value == 293
    dq.append(73)
    assert dq.tail.value == 73
    dq.append(83)
    dq.append(84)
    assert dq.tail.value == 84
    assert dq.len == 4


def test_pop(dq):
    """Test append removes and returns last item in dequeue."""
    dq.append(65)
    dq.append(34)
    dq.append(3453)
    dq.append(6442)
    assert dq.pop() == 6442
    assert dq.pop() == 3453
    assert dq.pop() == 34
    assert dq.len == 1


def test_appendleft(dq):
    """Test appendleft adds new value to head of dequeue."""
    dq.appendleft(293)
    assert dq.tail.value == 293
    dq.appendleft(73)
    assert dq.head.value == 73
    dq.appendleft(83)
    dq.appendleft(84)
    assert dq.head.value == 84
    assert dq.len == 4


def test_peek(dq):
    """Test peek displays value of tail of dequeue."""
    dq.append(293)
    assert dq.peek() == 293
    dq.append(73)
    assert dq.peek() == 73
    dq.append(83)
    dq.append(84)
    assert dq.peek() == 84
    dq.append(4)
    assert dq.peek() == 4


def test_popleft(dq):
    """Test popleft removes and returns value of head of dequeue"""
    dq.appendleft(65)
    dq.appendleft(34)
    dq.appendleft(3453)
    dq.appendleft(6442)
    assert dq.popleft() == 6442
    assert dq.popleft() == 3453
    assert dq.popleft() == 34
    assert dq.len == 1


def test_peekleft(dq):
    """Test peekleft displays the value of the head of dequeue."""
    dq.appendleft(293)
    assert dq.peekleft() == 293
    dq.appendleft(73)
    assert dq.peekleft() == 73
    dq.appendleft(83)
    dq.appendleft(84)
    assert dq.peekleft() == 84
    dq.appendleft(4)
    assert dq.peekleft() == 4


def test_size(dq):
    """Test the size (length) of the dequeue is properly tracked."""
    dq.appendleft(65)
    assert dq.size() == 1
    dq.append(34)
    assert dq.size() == 2
    dq.appendleft(3453)
    assert dq.size() == 3
    dq.appendleft(6442)
    assert dq.size() == 4
