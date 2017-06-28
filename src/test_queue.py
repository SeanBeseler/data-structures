import pytest
from que_ import our_queue


@pytest.fixture
def queue_fixture():
    """Fixture for our_queue functionality"""
    new_queue = our_queue()
    return new_queue


def test_queue_init(queue_fixture):
    assert queue_fixture.size == 0


def test_queue_enqueue(queue_fixture):
    queue_fixture.enqueue(4534)
    assert queue_fixture.peek() == 4534


def test_queue_peek(queue_fixture):
    queue_fixture.enqueue(90093)
    queue_fixture.enqueue(323)
    assert queue_fixture.peek() == 90093


def test_queue_dequeue(queue_fixture):
    queue_fixture.enqueue(18)
    assert queue_fixture.dequeue() == 18


def test_queue_length(queue_fixture):
    queue_fixture.enqueue(2342)
    queue_fixture.enqueue(47)
    queue_fixture.enqueue(277)
    assert len(queue_fixture) == 3
