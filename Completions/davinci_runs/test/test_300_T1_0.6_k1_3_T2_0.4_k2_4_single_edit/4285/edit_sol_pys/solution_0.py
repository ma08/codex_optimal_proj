#!/usr/bin/env python

import os
import sys

def main():
    # Check if user has provided a file
    if len(sys.argv) != 2:
        print("Usage: python file.py <filename>")
        sys.exit(1)

    # Check if file exists
    if not os.path.exists(sys.argv[1]):
        print("File '{}' does not exist.".format(sys.argv[1]))
        sys.exit(1)

    # Check if file is a file
    if not os.path.isfile(sys.argv[1]):
        print("'{}' is not a file.".format(sys.argv[1]))
        sys.exit(1)

    # Check if file is readable
    if not os.access(sys.argv[1], os.R_OK):
        print("File '{}' is not readable.".format(sys.argv[1]))
        sys.exit(1)

    # Check if file is executable
    if not os.access(sys.argv[1], os.X_OK):
        print("File '{}' is not executable.".format(sys.argv[1]))
        sys.exit(1)

    # Check if file is writable
    if os.access(sys.argv[1], os.W_OK):
        print("File '{}' is writable.".format(sys.argv[1]))
    else:
        print("File '{}' is not writable.".format(sys.argv[1]))

if __name__ == '__main__':
    main()
