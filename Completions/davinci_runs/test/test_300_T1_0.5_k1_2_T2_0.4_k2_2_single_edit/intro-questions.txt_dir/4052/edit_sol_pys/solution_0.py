#!/usr/bin/env python

import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: file.py filename")
        return
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("File does not exist")
        return
    f = open(filename)
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()
