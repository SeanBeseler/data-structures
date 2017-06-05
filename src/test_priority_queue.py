"""Test the functions for the priority queue data structure"""
import pytest



def test_init_of_priority_queue():
    """Test priority queue is successfully initialized"""
    from pque import Pque
    new_pque = Pque()
    assert new_pque.value is None
    assert new_pque.priority is 0
    assert new_pque.next_node is None


def test_insert_function_priority_queue():
    from pque import Pque
    new_pque = Pque()
    new_pque.insert(23, -20)
    assert new_pque.peek() == 23
    new_pque.insert(34, -14)
    assert new_pque.peek() == 34
    new_pque.insert(21, -10)
    assert new_pque.peek() == 21
    new_pque.insert(32, -14)
    assert new_pque.peek() == 21


def test_peek_priority_queue():
    from pque import Pque
    new_pque = Pque()
    new_pque.insert(23, -20)
    assert new_pque.peek() == 23
    new_pque.insert(34, -14)
    assert new_pque.peek() == 34
    new_pque.insert(21, -10)
    assert new_pque.peek() == 21
    new_pque.insert(32, -14)
    assert new_pque.peek() == 21


def test_pop_priority_queue():
    from pque import Pque
    new_pque = Pque()
    new_pque.insert(2, -40)
    assert new_pque.pop() == 2
    new_pque.insert(45, -34)
    new_pque.insert(46, -30)
    assert new_pque.pop() == 46
    assert new_pque.pop() == 45
