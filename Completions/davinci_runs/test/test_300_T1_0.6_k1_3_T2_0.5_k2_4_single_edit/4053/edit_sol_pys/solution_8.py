#!/usr/bin/env python3

import sys

def main():
    """
    Main function.
    """
    f = open(sys.argv[1], "r")
    print(f.read())
    f.close()

if __name__ == "__main__":
    main()
