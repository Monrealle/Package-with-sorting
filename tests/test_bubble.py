import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from bubble import bubble_sort

@pytest.mark.parametrize("input,expected", [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, -3, 2, -8], [-8, -3, 2, 5])
])
def test_bubble_sort(input, expected):
    assert bubble_sort(input) == expected
