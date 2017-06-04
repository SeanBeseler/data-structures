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


def test_init_with_tuple(bheap):
    """Test that the binary heap can be initialized with a tuple."""
    assert bheap(13, 7, 4, 15, 1) == [1, 4, 7, 15, 13]


def test_push_of_binary_heap(bheap):
    """Test push function for Binary Heap"""
    bheap.push(13)
    bheap.push(9)
    bheap.push(15.6)
    bheap.push(12)
    bheap.push(11)
    assert bheap == [9, 11, 15.6, 13, 12]
    bheap.push(4)
    assert bheap == [4, 11, 9, 15.6, 13, 12]
    bheap.push(10)
    assert bheap == [4, 11, 9, 15.6, 13, 12, 10]
    bheap.push(1)
    assert bheap == [1, 4, 9, 11, 12, 15.6, 10, 13]


def test_pop_of_binary_heap(bheap):
    """Test pop function for binary heap"""
    bheap.push(16)
    bheap.push(8.2)
    bheap.push(15)
    bheap.push(12)
    bheap.push(45)
    bheap.push(2)
    bheap.push(9)
    assert bheap == [2, 8.2, 9, 12, 45, 15, 16]
    bheap.pop()
    assert bheap == [8.2, 12, 9, 16, 45, 15]
    bheap.pop()
    assert bheap == [9, 12, 15, 16, 45]


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
    assert bheap == [2, 8, 9, 12, 45, 15, 16]
    assert bheap._get_parent(4) == 1
