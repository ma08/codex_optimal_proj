#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division, print_function

import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)
    args = parser.parse_args()

    with args.infile as fp:
        with args.outfile as wp:
            solve(fp, wp)


def solve(fp, wp):
    n, a, b = map(int, fp.readline().split())
    print(min(n*a, b), file=wp)


if __name__ == '__main__':
    main()
