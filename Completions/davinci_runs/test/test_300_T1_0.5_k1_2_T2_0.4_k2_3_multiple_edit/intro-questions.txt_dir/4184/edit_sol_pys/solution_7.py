# coding: utf-8

n = int(input())
w = list(map(int, input().split()))

min_diff = 100 * n
for t in range(1, n):
    s1 = sum(w[:t])
    s2 = sum(w[t:])
    min_diff = min(min_diff, abs(s1 - s2))

print(min_diff)
