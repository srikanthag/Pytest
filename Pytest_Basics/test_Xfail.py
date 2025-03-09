import pytest

# A test that we expect to fail
@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2  # This will fail, but pytest will consider it as expected

# A regular test that will pass
def test_pass():
    assert 1 == 1

# --------------------------------------------------------------------------------------------------------
# xfail with conditions:
# You can also conditionally mark a test as xfail based on a specific reason or condition. For example:

@pytest.mark.xfail(reason="This feature is not implemented yet")
def test_feature_not_implemented():
    assert some_feature() == expected_value

# --------------------------------------------------------------------------------------------------------
# strict=True option:
# If you want pytest to fail the test if an xfail marked test passes (i.e., the "expected failure" succeeds), you can use the strict=True option:
@pytest.mark.xfail(strict=True)
def test_should_fail():
    assert 1 == 1  # This will cause the test to fail because it unexpectedly passes
