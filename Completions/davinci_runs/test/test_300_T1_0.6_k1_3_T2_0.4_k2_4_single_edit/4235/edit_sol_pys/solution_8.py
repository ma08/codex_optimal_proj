#!/usr/bin/env python

import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='File type identification utility')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('file', nargs='+', help='file(s) to identify')
    args = parser.parse_args()

    for f in args.file:
        if not os.path.isfile(f):
            print('%s: not a file' % f)
            continue

        print('%s: %s' % (f, os.popen('file -b %s' % f).read().strip()))

if __name__ == '__main__':
    main()
