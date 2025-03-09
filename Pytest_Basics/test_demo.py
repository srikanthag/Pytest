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