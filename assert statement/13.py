def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor of two integers.
 
    :param a: The first integer.
    :param b: The second integer.
    :return: The greatest common divisor of the two integers.
    """
    while b:
        a, b = b, a % b
    return a
 
 
# Test that the GCD of 8 and 12 is 4
assert gcd(8, 12) == 4
 
# Test that the GCD of 17 and 23 is 1
assert gcd(17, 23) == 1
 
# Test that the GCD of 40 and 60 is 20
assert gcd(40, 60) == 20
 
# Test that the GCD of 0 and 5 is 5
assert gcd(0, 5) == 5