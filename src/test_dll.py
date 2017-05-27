import pytest
from dll import double_linked_list


@pytest.fixture
def the_fixture():
    """Fixture for dll functionality"""
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


def test_init_dll(the_fixture):
    assert the_fixture.size == 0


@pytest.mark.parametrize('entered, result', test_dll_pop_params_table)
def test_pop_dll(entered, result, the_fixture):
    the_fixture.push(entered)
    assert the_fixture.pop() == result


@pytest.mark.parametrize('entered, result', test_dll_push_params_table)
def test_push_dll(entered, result, the_fixture):
    the_fixture.push(entered)
    assert the_fixture.pop() == result


@pytest.mark.parametrize('entered, result', test_dll_shift_params_table)
def test_shift_dll(entered, result, the_fixture):
    the_fixture.append(entered)
    assert the_fixture.shift() == result


@pytest.mark.parametrize('entered, result', test_dll_append_params_table)
def test_append_dll(entered, result, the_fixture):
    the_fixture.append(entered)
    assert the_fixture.pop() == result


def test_length_dll(the_fixture):
    the_fixture.append(8)
    the_fixture.append(6)
    the_fixture.push(4)
    the_fixture.append(6)
    the_fixture.push(3)
    the_fixture.append(6)
    assert len(the_fixture) == 6
    the_fixture.pop()
    assert len(the_fixture) == 5
    the_fixture.append(618)
    the_fixture.push(236)
    the_fixture.shift()
    assert len(the_fixture) == 6
