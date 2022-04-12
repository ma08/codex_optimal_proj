#!/usr/bin/env python3

import sys
import os
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("Error: File '{}' not found".format(filename))
        sys.exit(1)

    infile = open(filename, 'r')
    text = infile.read()
    infile.close()

    text = re.sub(r'\bFOO\b', 'bar', text)

    outfile = open(filename, 'w')
    outfile.write(text)
    outfile.close()

if __name__ == '__main__':
    main()
