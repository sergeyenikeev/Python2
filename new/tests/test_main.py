import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 5, 7),
    (-1, 1, 0),
    (-1, 1, 0),
    (0, 0, 0),
    (1000, 1000, 2000),
])
def test_add(a, b, expected):
    assert a + b == expected