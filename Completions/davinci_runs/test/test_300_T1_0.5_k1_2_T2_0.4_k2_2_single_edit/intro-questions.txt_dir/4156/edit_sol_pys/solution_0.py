#!/usr/bin/python3

n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < -w:
        print(0)
        break
    j += a[i]
    if j > w or j < -w:
        print(0)
        break

if i == n-1 and j >= 0:
    print(w-j+1)
