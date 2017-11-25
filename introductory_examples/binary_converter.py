def convert_integer_to_binary_string(inputInteger, zeroPadLength=0):
    """
    Converts an integer to a zero-padded binary string.
    """
    return "{{:0{}b}}".format(zeroPadLength).format(inputInteger)


def test_my_converter():
    assert convert_integer_to_binary_string(0, 3) == "000"
    assert convert_integer_to_binary_string(8, 5) == "01000"
    assert convert_integer_to_binary_string(7, 1) == "111"

def test_even_more():
    assert convert_integer_to_binary_string(191, 0) == "11111111"
    assert convert_integer_to_binary_string(0, 0) == "0"
