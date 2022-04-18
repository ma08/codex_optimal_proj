#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <FILE>".format(sys.argv[0]))
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line in f:
            print(line, end='')

if __name__ == '__main__':
    main()
