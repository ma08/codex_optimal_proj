#!/usr/bin/env python3

import sys

def main():
    # Check for correct arguments
    if len(sys.argv) != 2:
        print("Usage: ./file filename")
        sys.exit(1)

    # Open file
    try:
        f = open(sys.argv[1], 'r')
    except:
        print("Could not open file")
        sys.exit(1)

    # Read file
    text = f.read()

    # Close file
    f.close()

    # Print file
    print(text)

if __name__ == "__main__":
    main()
