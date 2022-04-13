#!/usr/bin/env python3

import os

import sys


def main():
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print('File {} does not exist'.format(filename))
        sys.exit(1)

    if not os.path.isfile(filename):
        print('{} is not a file'.format(filename))
        sys.exit(1)

    with open(filename, 'r') as f:
        m = int(f.readline().strip())
        n = int(f.readline().strip())

        if m < 8 or n < 8: print('unsatisfactory')
        else: print('satisfactory')


if __name__ == '__main__':
    main()
