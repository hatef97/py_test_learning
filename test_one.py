import one
import pytest

def test_add():
    assert one.add(3, 4) == 7
    assert one.add(-3, 5) == 2
    assert one.add(0, 6) == 6

def test_subtract():
    assert one.subtract(8, 4) == 4
    assert one.subtract(-9, 19) == -28

def test_multiply():
    assert one.multiply(3, 9) != 20

def test_division():
    assert one.division(25, 5) == 5
    with pytest.raises(ZeroDivisionError):
        one.division(3, 0)
