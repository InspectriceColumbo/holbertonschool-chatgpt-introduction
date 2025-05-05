#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer. If n = 0, return is 1 bc 0! equals to 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Reads an integer from command line's args & calculates its factorial
f = factorial(int(sys.argv[1]))
print(f)
