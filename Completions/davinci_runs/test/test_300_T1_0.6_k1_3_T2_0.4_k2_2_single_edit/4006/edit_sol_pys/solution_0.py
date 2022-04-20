#!/usr/bin/env python3


from __future__ import print_function

import os
import sys


def usage():
    print('Usage:', file=sys.stderr)
    print('  {} [input_file]'.format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)


def main():
    if len(sys.argv) > 2:
        usage()

    input_stream = sys.stdin
    if len(sys.argv) == 2:
        if sys.argv[1] == '-':
            pass
        elif os.path.exists(sys.argv[1]):
            input_stream = open(sys.argv[1])
        else:
            print('No such file:', sys.argv[1], file=sys.stderr)
            sys.exit(1)

    n = int(input_stream.readline())

    reachable = set()

    def solve(x):
        if x in reachable:
            return
        reachable.add(x)
        solve(f(x))

    solve(n)

    print(len(reachable))


def f(x):
    while x % 10 == 0:
        x //= 10
    return x + 1


if __name__ == '__main__':
    main()
