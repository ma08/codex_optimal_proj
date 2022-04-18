#!/usr/bin/python3

n = int(input())
q = list(map(int, input().split()))
q.sort(reverse=True)

p = [0]*n
p[0] = q[0]
for i in range(1, n):
    p[i] = q[i] + p[i - 1]

if p[n-1] < 1:
    print(-1)
else:

    print(*p)
