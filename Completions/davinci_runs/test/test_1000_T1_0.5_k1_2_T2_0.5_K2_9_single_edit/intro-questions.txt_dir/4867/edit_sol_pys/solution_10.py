#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Solution

import sys

def main(args):
    m, n = map(int, input().split())
    u, l, r, d = map(int, input().split())

    print('#' * (l + r + n) + '.' * (d + u))
    print('.' * (l + r + n) + '#' * (d + u))
    for i in range(m):
        print('#' * l + input() + '#' * r)
    print('.' * (l + r + n) + '#' * (d + u))
    print('#' * (l + r + n) + '.' * (d + u))

if __name__ == '__main__':
    sys.exit(main(sys.argv))
