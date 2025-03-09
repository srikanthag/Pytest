import pytest


# Fixture definition
@pytest.fixture
def sample_data():
    # Setup: Code that runs before the test
    data = {"name": "pytest", "type": "testing"}
    print("Setting up sample_data fixture")

    # Yield the data to the test function
    yield data

    # Teardown: Code that runs after the test
    print("Tearing down sample_data fixture")


# Test function that uses the fixture
def test_name(sample_data):
    assert sample_data["name"] == "pytest"


def test_type(sample_data):
    assert sample_data["type"] == "testing1"



