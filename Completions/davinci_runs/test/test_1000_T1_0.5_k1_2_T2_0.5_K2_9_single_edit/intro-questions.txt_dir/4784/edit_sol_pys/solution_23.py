#!/usr/bin/env python3
"""
This program reads the contents of the file passed in as an argument.
"""


import sys

def readfile(filename):
    """Prints the contents of a file."""
    f = open(filename, 'r')
    for line in f:
        print(line)

def main():
    """Reads the file passed in as an argument."""
    readfile(sys.argv[1])

if __name__ == "__main__":
    main()
