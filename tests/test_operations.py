from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(4, 3) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(8, 2) == 4

def test_divide_zero():
    assert divide(5, 0) == "Error: Division by zero"