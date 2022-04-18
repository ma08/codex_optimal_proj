# coding: utf-8

n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
print(sum(1 if i >= k else 0 for i in h))
