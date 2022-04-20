#!/usr/bin/env python3

import os
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print("{} doesn't exist".format(filename))
        sys.exit(1)

    if os.path.isfile(filename):
        print("{} is a file".format(filename))
    elif os.path.isdir(filename):
        print("{} is a directory".format(filename))
    else:
        print("{} is something else".format(filename))

    sys.exit(0)

if __name__ == '__main__':
    main()
