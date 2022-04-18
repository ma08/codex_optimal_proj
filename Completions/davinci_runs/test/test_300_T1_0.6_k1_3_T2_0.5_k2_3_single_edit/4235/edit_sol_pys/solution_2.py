#!/usr/bin/python

import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python file.py <file>")
        return

    file = sys.argv[1]
    if os.path.exists(file):
        print("File exists!")
        return

    f = open(file, 'w')
    f.write("This is a test file.")
    f.close()

if __name__ == '__main__':
    main()
