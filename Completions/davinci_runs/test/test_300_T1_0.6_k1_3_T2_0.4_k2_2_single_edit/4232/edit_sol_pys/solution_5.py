#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        exit(1)

    for filename in sys.argv[1:]:
        with open(filename) as f:
            data = f.read()
            print("{}: {}".format(filename, len(data)))

if __name__ == "__main__":
    main()
