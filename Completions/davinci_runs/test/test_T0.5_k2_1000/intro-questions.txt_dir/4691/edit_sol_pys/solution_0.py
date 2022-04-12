#!/usr/bin/env python3

import sys
import collections

def main():
    n = int(sys.stdin.readline())
    words = sys.stdin.read().split()
    counts = collections.Counter(words)
    for word, count in counts.items():
        print(word, ":", count)

if __name__ == '__main__':
    main()
