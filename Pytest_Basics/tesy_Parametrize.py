import pytest

# Function to test
def add(a, b):
    return a + b

# Parameterized test
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# --------------------------------------------------------------------------------------------------------
import pytest

# Function to test
def reverse_string(s):
    return s[::-1]

# Parameterized test
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "olleh"),
    ("world", "world"),
    ("", ""),
    ("a", "a"),
])
def test_reverse_string(input_str, expected):
    assert reverse_string(input_str) == expected

# --------------------------------------------------------------------------------------------------------

import pytest

# Function to test
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Parameterized test
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (5, 0, ValueError),  # This case expects an exception
])
def test_divide(a, b, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            divide(a, b)
    else:
        assert divide(a, b) == expected
