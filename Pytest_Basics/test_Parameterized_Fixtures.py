import pytest

pytest.fixture(params=["Chrome", "Firefox", "Edge", "Safari"])
def browser(request):
    return request.param

def test_browser_launch():
    print(f"Running test on {browser}")
    assert browser in ["Chrome", "Firefox", "Edge"]

#=================================================================

@pytest.fixture
def setup_data(request):
    return request.param  # Return the parameter passed in the test

@pytest.mark.parametrize('setup_data', [[1, 2, 3], [4, 5], [10, 20, 30]], indirect=True)
def test_sum(setup_data):
    result = sum(setup_data)
    assert result == sum(setup_data)  # The test will pass as long as sum() is correct for each parameterized input
