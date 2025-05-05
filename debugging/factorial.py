#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1 # n has 2B decremented 4 each iteration or loop will b infinite
    return result

f = factorial(int(sys.argv[1]))
print(f)
