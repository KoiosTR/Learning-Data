import my_functions


def test_add():
    result = my_functions.add(1, 3)
    assert result == 5


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2