# coding: utf-8

import sys

def main():
    n = int(sys.stdin.readline())
    t = sorted(list(map(int, sys.stdin.readline().split())))
    ans = 0
    for i in range(n):
        ans += t[i] * (n - i)
    print(ans)

main()
