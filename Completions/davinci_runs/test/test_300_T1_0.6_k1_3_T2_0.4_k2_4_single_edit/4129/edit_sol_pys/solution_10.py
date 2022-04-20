#!/usr/bin/python

import sys
import os
import re

def main():
    if len(sys.argv) < 2:
        print "Usage: %s <file>" % sys.argv[0]
        sys.exit(1)
    else:
        file = sys.argv[1]
        if os.path.isfile(file):
            print file + " is a regular file"
        elif os.path.isdir(file):
            print file + " is a directory"
        else:
            print file + " is neither a regular file nor a directory"

if __name__ == "__main__":
    main()
