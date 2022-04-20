# coding: utf-8

n = int(input())
a = list(map(int, input().split()))

q = [a[0]]
for i in range(1, n):
    if a[i] <= 2 * q[-1]:
        q[-1] = a[i]
    else:
        q.append(a[i])

print(len(q))
