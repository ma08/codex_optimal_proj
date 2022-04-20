#!/usr/bin/python

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: ./file.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        f = open(filename, 'r')
        print("Opened file " + filename)
        f.close()
    except IOError:
        print("Can't open file " + filename)
        sys.exit(1)

if __name__ == '__main__':
    main()
