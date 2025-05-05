#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer. If n = 0, it returns 1 bc 0! is defined to be equal to 1.
    """
    if n == 0:  # Normal case: Factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Reads an integer from command line's args and calculates its factorial
f = factorial(int(sys.argv[1]))
print(f)
