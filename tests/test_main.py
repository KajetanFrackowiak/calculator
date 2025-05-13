from main import add, subtraction, multiply

def test_add():
    assert add(1, 2) == 3

def test_subtraction():
    assert subtraction(5, 3) == 2

def test_multuply():
    assert multiply(5, 3) == 13
