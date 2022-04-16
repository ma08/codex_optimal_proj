#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def main():
    n = int(input())
    s = [input() for _ in range(n)]

    c = collections.Counter(s)

    print("\n".join(sorted(k for k, v in c.items() if v == max(c.values()))))

if __name__ == '__main__':
    main()
