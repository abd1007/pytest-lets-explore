def integer_to_binary(inputInteger, zeroPadLength=0):
    """
    Converts an integer to a zero-padded binary string.
    """
    return "{{:0{}b}}".format(zeroPadLength).format(inputInteger)


def test_my_converter():
    testCase = {"input": 8,
                "expectedResult": "1000"}
    assert integer_to_binary(testCase["input"]) == testCase["expectedResult"]

    # In the previous example, this was:
    # assert convert_integer_to_binary_string(8, 0) == "1000"
