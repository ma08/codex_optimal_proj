# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))


def solve(a):
    ans = 0
    while True:
        if all(i % 2 == 0 for i in a):
            a = [i / 2 for i in a]
            ans += 1
        else:
            break
    return ans


print(solve(a))
