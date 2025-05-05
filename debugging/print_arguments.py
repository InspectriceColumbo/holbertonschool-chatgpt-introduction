#!/usr/bin/python3
import sys

for i in range(1, len(sys.argv)):
    # Arg 0=file's name, so loop has to start at index 1, which is the 1st arg
    print(sys.argv[i])
