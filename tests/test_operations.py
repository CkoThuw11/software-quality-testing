from calculator.operations import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(4, 3) == 1

def test_multiply():
    assert multiply(2, 3) == 6