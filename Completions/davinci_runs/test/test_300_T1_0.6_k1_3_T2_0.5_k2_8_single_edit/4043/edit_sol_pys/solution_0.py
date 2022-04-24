#!/usr/bin/env python

import sys
import os
import re

def main():
    """Reads a file and prints it to the screen"""
    filename = sys.argv[1]
    try:
        f = open(filename, 'r')
    except IOError:
        print "cannot open", filename
    else:
        for line in f:
            print line,
        f.close()

if __name__ == '__main__':
    main()
