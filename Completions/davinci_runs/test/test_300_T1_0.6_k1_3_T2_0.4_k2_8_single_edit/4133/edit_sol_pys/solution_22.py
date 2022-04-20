#!/usr/bin/python

import os
import sys

def main():
    if len(sys.argv) == 2:
        if os.path.isfile(sys.argv[1]):
            f = open(sys.argv[1], 'r')
            print f.read()
            f.close()
        else:
            print sys.argv[1] + ": No such file or directory"
    else:
        print "Usage: ./file.py <filename>"

if __name__ == '__main__':
    main()
