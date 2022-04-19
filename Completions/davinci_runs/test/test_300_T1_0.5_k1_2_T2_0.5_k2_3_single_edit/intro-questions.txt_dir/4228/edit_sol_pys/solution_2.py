# coding: utf-8

n, l = map(int, input().split())

flavors = [l + i - 1 for i in range(n)]

print(sum(flavors) - min([abs(f) for f in flavors]))
