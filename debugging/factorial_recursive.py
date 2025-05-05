#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer.
    """
    if n == 0:  # Normal case: Factorial of 0 is 1
        return 1
    else:  # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)

# Read the first command-line argument, convert it to an integer,
# calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
