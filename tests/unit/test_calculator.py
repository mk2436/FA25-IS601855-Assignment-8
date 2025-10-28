# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
        (1000000000, 2000000000, 3000000000),  # Very large integers
        (-1000000000, -2000000000, -3000000000),  # Very large negative integers
        (1e15, 2e15, 3e15),  # Very large floats
        (1e-15, 1e-15, 2e-15),  # Very small floats
        (0.1, 0.2, 0.3),    # Decimal precision test
        (0.7, 0.1, 0.8),    # Another decimal precision test
        (1.0 / 3, 1.0 / 3, 2.0 / 3),  # Recurring decimal
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
        "add_very_large_integers",
        "add_very_large_negative_integers",
        "add_very_large_floats",
        "add_very_small_floats",
        "add_decimal_precision_0.1_0.2",
        "add_decimal_precision_0.7_0.1",
        "add_recurring_decimal",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    # Use tolerance for floating point comparisons to handle precision issues
    assert result == expected or abs(result - expected) < 1e-10, \
        f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
        (1000000000000, 500000000000, 500000000000),  # Very large integers
        (-1000000000000, -500000000000, -500000000000),  # Very large negative integers
        (1e20, 5e19, 5e19),  # Very large floats
        (1e-10, 1e-10, 0.0),  # Very small floats
        (0.123456789, 0.023456789, 0.1),  # Decimal precision test
        (999.9999, 0.0001, 999.9998),  # High precision test
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
        "subtract_very_large_integers",
        "subtract_very_large_negative_integers",
        "subtract_very_large_floats",
        "subtract_very_small_floats",
        "subtract_decimal_precision",
        "subtract_high_precision",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the 'subtract' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-5, -3, -2)
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # Assert that the result of subtract(a, b) matches the expected value
    # Use tolerance for floating point comparisons to handle precision issues
    assert result == expected or abs(result - expected) < 1e-10, \
        f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
        (999999999999, 2, 1999999999998),  # Very large integer
        (-999999999999, 2, -1999999999998),  # Very large negative integer
        (1e100, 2.0, 2e100),  # Very large float
        (1e-100, 1e100, 1.0),  # Very small × very large
        (1e100, 1e-100, 1.0),  # Very large × very small
        (0.123456789, 0.987654321, 0.1219326311115269),  # Decimal precision
        (999.99999, 0.00001, 0.0099999999),  # High precision multiplication
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
        "multiply_very_large_integer",
        "multiply_very_large_negative_integer",
        "multiply_very_large_float",
        "multiply_very_small_by_very_large",
        "multiply_very_large_by_very_small",
        "multiply_decimal_precision",
        "multiply_high_precision",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    This parameterized test verifies that the 'multiply' function correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the 'multiply' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-2, 3, -6)
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # Assert that the result of multiply(a, b) matches the expected value
    # Use tolerance for floating point comparisons to handle precision issues
    assert result == expected or abs(result - expected) < abs(expected) * 1e-10, \
        f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
        (1000000000, 1000000, 1000.0),  # Very large integers
        (1e20, 1e10, 1e10),    # Very large floats
        (1.0, 3.0, 1.0 / 3.0),  # Recurring decimal division
        (1.0, 10.0, 0.1),      # Precise decimal division
        (0.000000001, 0.0000000001, 10.0),  # Very small numbers
        (999.99999, 0.001, 999999.99),  # High precision division
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
        "divide_very_large_integers",
        "divide_very_large_floats",
        "divide_recurring_decimal",
        "divide_precise_decimal",
        "divide_very_small_numbers",
        "divide_high_precision",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'divide' function correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'divide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_divide(6, 3, 2.0)
    >>> test_divide(-6, 3, -2.0)
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    # Use tolerance for floating point comparisons to handle precision issues
    assert result == expected or abs(result - expected) < abs(expected) * 1e-10, \
        f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'divide' function with arguments 6 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_divide_by_zero()
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


@pytest.mark.parametrize(
    "a, b",
    [
        (1e10, 1e-10),                      # Dividing large number by very small
        (1000000000, 0.000000001),         # Dividing billion by nano
        (-1000000000, 0.000000001),        # Dividing negative billion by nano
        (999.9999, 0.0001),                # Precision edge case
        (1.5, 0.00001),                     # Tiny divisor
    ],
    ids=[
        "divide_large_by_tiny",
        "divide_billion_by_nano",
        "divide_negative_billion_by_nano",
        "divide_precision_near_zero",
        "divide_small_divisor",
    ]
)
def test_divide_by_near_zero(a: Number, b: Number) -> None:
    """
    Test division by very small (near-zero) divisors.
    
    These tests verify that the function correctly handles division by extremely
    small numbers without overflow or precision loss.
    """
    result = divide(a, b)
    expected = float(a) / float(b)
    assert abs(result - expected) < abs(expected) * 1e-10, \
        f"Expected divide({a}, {b}) to be approximately {expected}, but got {result}"
