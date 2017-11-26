import pytest
import simulation_library


@pytest.fixture(params=range(10))
def inputData(request):
    return request.param


def test_postprocess(inputData, mocker):
    mocker.patch("simulation_library.read_parameters",
                 side_effect=lambda: inputData)
    output = simulation_library.run_simulation()
    assert output == inputData * 5
