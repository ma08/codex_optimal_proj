#!/usr/bin/env python3
"""
Author : None
Date   : 2020-04-27
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    in_file = args.file
    out_file = args.outfile

    if out_file is None:
        out_file = sys.stdout

    for line in in_file:
        out_file.write(line)

    in_file.close()
    out_file.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()


n = int(input())
a = list(map(int, input().split()))
a.sort()

if n == 1:
    print(1)
    exit(0)

i = 0
j = 1

count = 0
while j < n:
    if a[j] - a[i] <= 5:
        j += 1
    else:
        i = j
        j += 1
    count = max(count, j - i)

print(count)
