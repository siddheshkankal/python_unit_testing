def factorial(n: int) -> int:
    """
    Calculates the factorial of a positive integer.
 
    :param n: The integer to calculate the factorial of.
    :return: The factorial of the integer.
    :raises ValueError: If the integer is negative.
    """
    if n < 0:
        raise ValueError(
            'Cannot calculate factorial of a negative number.'
        )
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
 
 
# Test that factorial of 0 is 1
assert factorial(0) == 1
 
# Test that factorial of 1 is 1
assert factorial(1) == 1
 
# Test that factorial of 5 is 120
assert factorial(5) == 120
 
# Test that factorial of a negative number raises a ValueError
# factorial(-1)
try:
    factorial(-1)
    assert False  # This line should not be reached
except ValueError:
    pass