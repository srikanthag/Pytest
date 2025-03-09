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

def test_largets_odd():
    result = is_even_or_odd(1000000)
    assert result == "Odd" , "1000000 is largest"

# ================================================================
# Example with an Exception
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0  # This will raise a ZeroDivisionError

def test_zero_division1():
    with pytest.raises(ZeroDivisionError):
        1/1
