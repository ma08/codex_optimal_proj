#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: ./file.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename) as f:
        print(f.read().rstrip())

if __name__ == "__main__":
    main()
