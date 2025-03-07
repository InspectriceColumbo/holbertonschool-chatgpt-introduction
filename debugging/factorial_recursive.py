#!/usr/bin/python3
import sys

# Function Description:
# This function computes the factorial of a given number using recursion.
# It multiplies the number by the factorial of the number minus one..
# ..until the base case of 0 is reached.

# Parameters:
# n (int): A positive integer for which the factorial will be calculated.

# Returns:
# int: The factorial of the input integer n. 
# If n == 0, the result is 1 (base case of the recursion).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the command-line argument and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
