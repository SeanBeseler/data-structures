import pytest
from dll import double_linked_list

@pytest.fixture
def the_fixture():
    new_dll = double_linked_list()
    return new_dll


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

"""Checks the length function is returning expected results"""
test_dll_length_params_table = [
    ([1, 2, 3], 3),
    ([4, 5, 7, 5], 4),
    ('Hello', 5)
]


def test_init_dll(the_fixture):
    assert the_fixture.size == 0


@pytest.mark.parametrize('entered, result', test_dll_pop_params_table)
def test_pop_dll(entered, result, the_fixture):
    the_fixture.push(entered)
    assert the_fixture.pop() == result
