import pytest


test_check_pop_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 5),
    ('Hello', 'o')
]

test_check_push_params_table = [
    (4, 4),
    (5, 5),
    ('H', 'H')
]

test_check_size_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 4),
    ('Hello', 5)
]

test_check_search_params_table = [
    ([1, 2, 3], 3, 3),
    ([4, 5, 7, 5], 4, 4),
    ('Hello', 'l', 'l')
]

test_check_remove_params_table = [
    ([1, 2, 3], 3, '2, 1'),
    ([4, 5, 7, 5], 4, '5, 7, 5'),
    ('Hello', 'l', 'o, l, e, H')
]


test_check_display_params_table = [
    ([1, 2, 3], '3, 2, 1'),
    ([4, 5, 7, 5], '5, 7, 5, 4'),
    ('Hello', 'o, l, l, e, H')
]

test_check_print_params_table = [
    ([1, 2, 3], '3, 2, 1'),
    ([4, 5, 7, 5], '5, 7, 5, 4'),
    ('Hello', 'o, l, l, e, H')
]

test_check_length_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 4),
    ('Hello', 5)
]

test_check_init_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 5),
    ('Hello', 'o')
]


@pytest.mark.parametrize('val, result', test_check_pop_params_table)
def test_pop_function(val, result):
    """tests the pop function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.pop() == result


@pytest.mark.parametrize('val, result', test_check_push_params_table)
def test_push_function(val, result):
    """tests the push function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList([1, 2, 3])
    assert new_linked_list.push(val).data == result


@pytest.mark.parametrize('val, result', test_check_size_params_table)
def test_size_function(val, result):
    """tests the size function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.size() == result


@pytest.mark.parametrize('val, search_for, result', test_check_search_params_table)
def test_search_function(val, search_for, result):
    """tests the search function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.search(search_for).data == result


@pytest.mark.parametrize('val, removed, result', test_check_remove_params_table)
def test_remove_function(val, removed, result):
    """tests the remove function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.remove(new_linked_list.search(removed)).display() == result


@pytest.mark.parametrize('val, result', test_check_display_params_table)
def test_display_function(val, result):
    """tests the display function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.display() == result


@pytest.mark.parametrize('val, result', test_check_print_params_table)
def test_print_function(val, result):
    """tests the print function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.__repr__() == result


@pytest.mark.parametrize('val, result', test_check_length_params_table)
def test_length_function(val, result):
    """tests the length function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert len(new_linked_list) == result


@pytest.mark.parametrize('val, result', test_check_init_params_table)
def test_init_function(val, result):
    """tests the init function of the class Linked List"""
    from linked_list import LinkedList
    new_linked_list = LinkedList(val)
    assert new_linked_list.pop() == result
