def greater_than_zero(number):
    return number > 0


def test_greater_than_zero():
    assert greater_than_zero(5) is True
    assert greater_than_zero(2) is True
    assert greater_than_zero(-1) is False
    assert greater_than_zero(0) is False
