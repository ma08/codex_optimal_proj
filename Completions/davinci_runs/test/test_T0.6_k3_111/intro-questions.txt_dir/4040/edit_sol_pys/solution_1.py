#!/usr/bin/env python

import os
import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("Error: File '%s' not found" % filename)
        sys.exit(1)

    f = open(filename, 'r')
    while True:
        where = f.tell()
        line = f.readline()
        if not line:
            time.sleep(1)
            f.seek(where)
        else:
            print(line, end="") # already has newline

if __name__ == '__main__':
    main()
