"""Test the functions of our Binary Heap data structure"""
import pytest


@pytest.fixture
def bheap():
    """Fixture for empty binary heap"""
    from binaryheap import Binary_heap
    new_bheap = Binary_heap()
    return new_bheap


def test_init_of_binary_heap(bheap):
    """Testing the binary heap is successfully initialized"""
    assert bheap.size == 0


def test_init_with_tuple():
    """Test that the binary heap can be initialized with a tuple."""
    from binaryheap import Binary_heap
    bheap = Binary_heap([13, 7, 4, 15, 1])
    assert bheap.list == [1, 4, 7, 15, 13]


def test_push_of_binary_heap(bheap):
    """Test push function for Binary Heap"""
    bheap.push(13)
    bheap.push(9)
    bheap.push(15.6)
    bheap.push(12)
    bheap.push(11)
    assert bheap.list == [9, 11, 15.6, 13, 12]
    bheap.push(4)
    assert bheap.list == [4, 11, 9, 13, 12, 15.6]
    bheap.push(10)
    assert bheap.list == [4, 11, 9, 13, 12, 15.6, 10]
    bheap.push(1)
    assert bheap.list == [1, 4, 9, 11, 12, 15.6, 10, 13]


def test_pop_of_binary_heap(bheap):
    """Test pop function for binary heap"""
    bheap.push(16)
    bheap.push(8.2)
    bheap.push(15)
    bheap.push(12)
    bheap.push(45)
    bheap.push(2)
    bheap.push(9)
    assert bheap.list == [2, 12, 8.2, 16, 45, 15, 9]
    bheap.pop()
    assert bheap.list == [8.2, 12, 9, 16, 45, 15]
    bheap.pop()
    assert bheap.list == [9, 12, 15, 16, 45]


def test_pop_empty_list_returns_error(bheap):
    """Test pop functions returns error on empty heap"""
    assert bheap.pop() is None


def test_get_parent(bheap):
    """Tests that the get parent function finds the appropriate
    parent index of a specified index.
    """
    bheap.push(16)
    bheap.push(8)
    bheap.push(15)
    bheap.push(12)
    bheap.push(45)
    bheap.push(2)
    bheap.push(9)
    assert bheap.list == [2, 12, 8, 16, 45, 15, 9]
    assert bheap._get_parent(4) == 1
