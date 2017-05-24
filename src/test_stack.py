import pytest


"""Checks the init function is returning expected results"""
test_stack_init_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 5),
    ('Hello', 'o')
]

"""Checks the pop function is returning expected results"""
test_stack_pop_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 5),
    ('Hello', 'o')
]

"""Checks the push function is returning expected results"""
test_stack_push_params_table = [
    (4, 4),
    (5, 5),
    ('H', 'H')
]

"""Checks the length function is returning expected results"""
test_stack_length_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 4),
    ('Hello', 5)
]


@pytest.mark.parametrize('val, result', test_stack_pop_params_table)
def test_pop_function(val, result):
    """tests the pop function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.pop() == result


@pytest.mark.parametrize('val, result', test_stack_push_params_table)
def test_push_function(val, result):
    """tests the push function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList([1, 2, 3])
    assert new_linked_list.push(val).data == result


@pytest.mark.parametrize('val, result', test_stack_length_params_table)
def test_length_function(val, result):
    """tests the length function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert len(new_linked_list) == result


@pytest.mark.parametrize('val, result', test_stack_init_params_table)
def test_init_function(val, result):
    """tests the init function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.pop() == result
