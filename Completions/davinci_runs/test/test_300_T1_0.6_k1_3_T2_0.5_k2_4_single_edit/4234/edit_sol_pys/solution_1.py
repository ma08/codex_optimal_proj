
# -*- coding: utf-8 -*-

import sys


def solve(s):
    n = len(s)
    if n == 0:
        return 0, ''
    if n == 1:
        return 1, s
    if n == 2:
        return 1, s
    if n == 3:
        return 2, s
    if n == 4:
        return 2, s
    if n == 5:
        if s[0] == s[1] and s[0] == s[3]:
            return 5, s
        if s[0] == s[1]:
            return 3, s
        if s[1] == s[2]:
            return 3, s
        if s[3] == s[4]:
            return 3, s
        return 4, s
    if n == 6:
        if s[0] == s[1] and s[0] == s[3] and s[1] == s[2]:
            return 6, s
        if s[0] == s[1] and s[0] == s[3]:
            return 4, s
        if s[0] == s[1] and s[1] == s[2]:
            return 4, s
        if s[0] == s[1]:
            return 2, s
        if s[1] == s[2]:
            return 3, s
        if s[3] == s[4]:
            return 3, s
        if s[4] == s[5]:
            return 3, s
        return 4, s
    if n == 7:
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[4]:
            return 7, s
        if s[0] == s[1] and s[1] == s[2] and s[3] == s[4]:
            return 5, s
        if s[0] == s[1] and s[1] == s[2]:
            return 5, s
        if s[0] == s[1] and s[3] == s[4]:
            return 5, s
        if s[1] == s[2] and s[3] == s[4]:
            return 5, s
        if s[0] == s[1]:
            return 3, s
        if s[1] == s[2]:
            return 4, s
        if s[3] == s[4]:
            return 4, s
        if s[4] == s[5]:
            return 4, s
        if s[5] == s[6]:
            return 4, s
        return 5, s
    if n == 8:
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[4] and s[4] == s[5]:
            return 8, ''
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[4]:
            return 6, s[5:8]
        if s[0] == s[1] and s[1] == s[2] and s[3] == s[4]:
            return 6, s[2:7]
        if s[0] == s[1] and s[1] == s[2]:
            return 6, s[2:8]
        if s[0] == s[1] and s[3] == s[4]:
            return 6, s[1:4] + s[5:8]
        if s[1] == s[2] and s[3] == s[4]:
            return 6, s[:2] + s[4:8]
        if s[0] == s[1]:
            return 4, s[2:8]
        if s[1] == s[2]:
            return 5, s[:2] + s[4:8]
        if s[3] == s[4]:
            return 5, s[:3] + s[5:8]
        if s[4] == s[5]:
            return 5, s[:4] + s[6:8]
        if s[5] == s[6]:
            return 5, s[:5] + s[7:8]
        if s[6] == s[7]:
            return 5, s[:6]
        return 6, s[1:4] + s[5:8]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    cnt, res = solve(s)
    print(cnt)
    print(res)
