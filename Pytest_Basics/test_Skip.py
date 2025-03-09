import pytest


def is_even_or_odd(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

def test_even_number():
    result = is_even_or_odd(4)
    print(result)

def test_odd_number():
    result = is_even_or_odd(7)
    print(result)

def test_largets_even():
    result = is_even_or_odd(1000000)
    assert result == "Even" , "1000000 is largest"

@pytest.mark.skip(reason="Not functional test case")
def test_largets_odd():
    result = is_even_or_odd(1000000)
    assert result == "Odd" , "1000000 is largest"