#!/usr/bin/env python
# coding: utf-8


def solve(n, m, c, b, a, start_index=0):
    if start_index > n:
        return 0

    if (a[start_index][0] * b[0] + a[start_index][1] * b[1] + a[start_index][2] * b[2] + c > 0):
        return 1 + solve(n, m, c, b, a, start_index+1)
    else:
        return solve(n, m, c, b, a, start_index+1)

if __name__ == '__main__':
    n, m, c = map(int, raw_input().split())
    b = map(int, raw_input().split())
    a = []
    for i in range(n):
        a.append(map(int, raw_input().split()))
    print(solve(n, m, c, b, a))
