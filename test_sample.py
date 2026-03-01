import pytest
from sample import (
    add,
    subtract,
    multiply,
    divide,
    is_even,
    factorial,
    reverse_string,
    is_palindrome,
)


# --- add ---

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_add_mixed_numbers():
    assert add(-3, 7) == 4


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


# --- subtract ---

def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 8) == -5


def test_subtract_same_numbers():
    assert subtract(5, 5) == 0


# --- multiply ---

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(7, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


def test_multiply_mixed_sign():
    assert multiply(-2, 5) == -10


# --- divide ---

def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0


def test_divide_results_in_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)


def test_divide_negative_numbers():
    assert divide(-9, 3) == -3.0


# --- is_even ---

def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(7) is False


def test_is_even_with_zero():
    assert is_even(0) is True


def test_is_even_with_negative_even():
    assert is_even(-6) is True


# --- factorial ---

def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_one():
    assert factorial(1) == 1


def test_factorial_of_five():
    assert factorial(5) == 120


def test_factorial_of_ten():
    assert factorial(10) == 3628800


def test_factorial_negative_raises():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-1)


# --- reverse_string ---

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_single_char():
    assert reverse_string("a") == "a"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh"


# --- is_palindrome ---

def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True


def test_is_palindrome_case_insensitive():
    assert is_palindrome("Racecar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") is False


def test_is_palindrome_single_char():
    assert is_palindrome("a") is True
