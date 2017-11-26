import pytest

def integer_to_binary(inputInteger, zeroPadLength=0):
    """
    Converts an integer to a zero-padded binary string.
    """
    return "{{:0{}b}}".format(zeroPadLength).format(inputInteger)


@pytest.fixture()
def testCase(request):
    testCase = {"input": 8,
                "expectedResult": "1000"}
    return testCase


def test_my_converter(testCase):
    result = integer_to_binary(testCase["input"])
    assert result == testCase["expectedResult"]
