#!/usr/bin/python

import sys
import os
import time

def main():
    if len(sys.argv)!=2:
        print("Usage: ", sys.argv[0], " <file>")
        sys.exit(0)

    filename = sys.argv[1]

    if os.path.exists(filename):
        print("File %s exists" % filename)
        print("Last modified: %s" % time.ctime(os.path.getmtime(filename)))
        print("Created: %s" % time.ctime(os.path.getctime(filename)))
    else:
        print("File %s does not exist" % filename)
        sys.exit(1)

if __name__ == "__main__":
    main()
