# coding: utf-8

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)
avg = sum_a / n

if avg >= m:
    print(0)
    exit()

if k <= m:
    print(-1)
    exit()

print(m*n - sum_a)
