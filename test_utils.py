import utils


def test_add():
    assert utils.add(1, 2) == 3


def test_subtract():
    assert utils.subtract(10, 3) == 7


def test_multiply():
    assert utils.multiply(1, 5) == 5


def test_divide():
    assert utils.divide(6, 3) == 2
