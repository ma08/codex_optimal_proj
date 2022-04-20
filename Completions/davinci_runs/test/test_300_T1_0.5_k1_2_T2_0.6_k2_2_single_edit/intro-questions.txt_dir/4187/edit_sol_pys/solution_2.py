# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))

print(max(len(set(a)), len(a) - a.count(0)))
