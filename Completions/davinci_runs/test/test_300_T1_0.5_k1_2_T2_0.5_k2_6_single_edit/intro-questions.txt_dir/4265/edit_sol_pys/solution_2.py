#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
