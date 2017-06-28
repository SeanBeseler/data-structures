import pytest
from dll import double_linked_list


@pytest.fixture
def dll():
    """Fixture for dll functionality"""
    new_dll = double_linked_list()
    return new_dll

@pytest.fixture
def dll_five_items(dll):
    dll.push(4)
    dll.append(5)
    dll.push(3)
    dll.push(2)
    dll.push(1)
    return dll



"""Checks the pop function is returning expected results"""
test_dll_pop_params_table = [
    (3, 3),
    (5, 5),
    ('o', 'o')
]

"""Checks the push function is returning expected results"""
test_dll_push_params_table = [
    (4, 4),
    (5, 5),
    ('H', 'H')
]

"""Checks the shift function is returning expected results"""
test_dll_shift_params_table = [
    (5, 5),
    (99, 99),
    ('oh hi', 'oh hi')
]

"""Checks the append function is returning expected results"""
test_dll_append_params_table = [
    (4, 4),
    (5, 5),
    ('H', 'H')
]


def test_init_dll(dll):
    assert dll.size == 0


@pytest.mark.parametrize('entered, result', test_dll_pop_params_table)
def test_pop_dll(entered, result, dll):
    dll.push(entered)
    assert dll.pop() == result


def test_five_items_dll_pop_from_end(dll_five_items):
    assert dll_five_items.pop() == 1


def test_five_items_dll_shift_from_end(dll_five_items):
    assert dll_five_items.shift() == 5


@pytest.mark.parametrize('entered, result', test_dll_push_params_table)
def test_push_dll(entered, result, dll):
    dll.push(entered)
    assert dll.pop() == result


@pytest.mark.parametrize('entered, result', test_dll_shift_params_table)
def test_shift_dll(entered, result, dll):
    dll.append(entered)
    assert dll.shift() == result


@pytest.mark.parametrize('entered, result', test_dll_append_params_table)
def test_append_dll(entered, result, dll):
    dll.append(entered)
    assert dll.pop() == result


def test_length_dll(dll):
    dll.append(8)
    dll.append(6)
    dll.push(4)
    dll.append(6)
    dll.push(3)
    dll.append(6)
    assert len(dll) == 6
    dll.pop()
    assert len(dll) == 5
    dll.append(618)
    dll.push(236)
    dll.shift()
    assert len(dll) == 6
