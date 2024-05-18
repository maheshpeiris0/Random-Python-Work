import pytest
from add_numbers import add_numbers

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])


def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected