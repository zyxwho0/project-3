"""Unit tests for the sample module.

Tests cover all functions including add, subtract, multiply, divide,
is_even, factorial, reverse_string, and is_palindrome.
"""

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
    """Test addition of two positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """Test addition of two negative numbers."""
    assert add(-1, -4) == -5


def test_add_mixed_numbers():
    """Test addition of positive and negative numbers."""
    assert add(-3, 7) == 4


def test_add_floats():
    """Test addition of floating point numbers."""
    assert add(1.5, 2.5) == 4.0


# --- subtract ---

def test_subtract_positive_numbers():
    """Test subtraction of two positive numbers."""
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    """Test subtraction resulting in negative number."""
    assert subtract(3, 8) == -5


def test_subtract_same_numbers():
    """Test subtraction of identical numbers."""
    assert subtract(5, 5) == 0


# --- multiply ---

def test_multiply_positive_numbers():
    """Test multiplication of two positive numbers."""
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    """Test multiplication by zero."""
    assert multiply(7, 0) == 0


def test_multiply_negative_numbers():
    """Test multiplication of two negative numbers."""
    assert multiply(-2, -3) == 6


def test_multiply_mixed_sign():
    """Test multiplication of positive and negative numbers."""
    assert multiply(-2, 5) == -10


# --- divide ---

def test_divide_positive_numbers():
    """Test division of two positive numbers."""
    assert divide(10, 2) == 5.0


def test_divide_results_in_float():
    """Test division resulting in float."""
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    """Test that dividing by zero raises ValueError."""
    error_msg = "Cannot divide by zero."
    with pytest.raises(ValueError, match=error_msg):
        divide(5, 0)


def test_divide_negative_numbers():
    """Test division of negative numbers."""
    assert divide(-9, 3) == -3.0


# --- is_even ---

def test_is_even_with_even_number():
    """Test is_even with an even number."""
    assert is_even(4) is True


def test_is_even_with_odd_number():
    """Test is_even with an odd number."""
    assert is_even(7) is False


def test_is_even_with_zero():
    """Test is_even with zero."""
    assert is_even(0) is True


def test_is_even_with_negative_even():
    """Test is_even with a negative even number."""
    assert is_even(-6) is True


# --- factorial ---

def test_factorial_of_zero():
    """Test factorial of zero."""
    assert factorial(0) == 1


def test_factorial_of_one():
    """Test factorial of one."""
    assert factorial(1) == 1


def test_factorial_of_five():
    """Test factorial of five."""
    assert factorial(5) == 120


def test_factorial_of_ten():
    """Test factorial of ten."""
    assert factorial(10) == 3628800


def test_factorial_negative_raises():
    """Test that factorial of negative number raises ValueError."""
    error_msg = "Factorial is not defined for negative numbers."
    with pytest.raises(ValueError, match=error_msg):
        factorial(-1)


# --- reverse_string ---

def test_reverse_string_basic():
    """Test reversing a basic string."""
    assert reverse_string("hello") == "olleh"


def test_reverse_string_single_char():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"


def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""


def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"


# --- is_palindrome ---

def test_is_palindrome_simple():
    """Test simple palindrome detection."""
    assert is_palindrome("racecar") is True


def test_is_palindrome_case_insensitive():
    """Test palindrome detection is case-insensitive."""
    assert is_palindrome("Racecar") is True


def test_is_palindrome_with_spaces():
    """Test palindrome detection ignores spaces."""
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_not_palindrome():
    """Test non-palindrome string."""
    assert is_palindrome("hello") is False


def test_is_palindrome_single_char():
    """Test single character is palindrome."""
    assert is_palindrome("a") is True
