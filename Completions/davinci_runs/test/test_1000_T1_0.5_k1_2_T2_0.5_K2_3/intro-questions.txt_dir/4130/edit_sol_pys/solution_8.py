# coding: utf-8

n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

count = 0
for i in range(n):
    if a[i] > i:
        count += a[i] - i
    else:
        break

print(count)
