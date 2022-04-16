
# -*- coding: utf-8 -*-

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    verdicts = sys.stdin.read().splitlines()
    counts = collections.Counter(verdicts)
    for verdict, count in counts.items():
        print(verdict, "x", count)

if __name__ == '__main__':
    main()
