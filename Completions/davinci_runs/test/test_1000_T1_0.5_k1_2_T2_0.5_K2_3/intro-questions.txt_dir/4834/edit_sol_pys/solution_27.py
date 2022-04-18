# coding: utf-8

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

b = []
for i in range(1, m+1):
    b.append(a[-i])

print(sum(b))
