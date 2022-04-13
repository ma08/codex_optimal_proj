# coding: utf-8

n = int(input())
times = list(map(int, input().split()))

times.sort()

total = 0
for i in range(n - 1):
    total += (i + 1) * times[i]

total += times[n - 1] * n

print(total)
