import os
import pytest
import simulation_library


@pytest.fixture(params=range(10))
def inputData(request):
    return request.param


def test_postprocess(inputData):
    with open("parameters.txt", "w") as parameterFile:
        parameterFile.write(str(inputData))
    output = simulation_library.run_simulation()
    os.remove("parameters.txt")
    assert output == inputData * 5
