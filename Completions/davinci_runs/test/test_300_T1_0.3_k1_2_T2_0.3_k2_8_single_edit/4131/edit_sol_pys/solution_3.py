# -*- coding: utf-8 -*-
# AtCoder Beginner Contest
# Problem A

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

prefectures = [[] for _ in range(n)]
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())
    prefectures[p-1].append(y)

for p in prefectures:
    p.sort()

for p in prefectures:
    for i, y in enumerate(p):
        print("{:06}{:06}".format(prefectures.index(p)+1, i+1))
