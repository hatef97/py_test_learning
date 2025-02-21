import two

def test_add():
    assert two.add(3, 4) == 7
    assert two.add(-3, 5) == 2
    assert two.add(0, 6) == 6

def test_subtract():
    assert two.subtract(8, 4) == 4
    assert two.subtract(-9, 19) == -28

def test_multiply():
    assert two.multiply(3, 9) != 20

def test_division():
    assert two.division(25, 5) == 5
