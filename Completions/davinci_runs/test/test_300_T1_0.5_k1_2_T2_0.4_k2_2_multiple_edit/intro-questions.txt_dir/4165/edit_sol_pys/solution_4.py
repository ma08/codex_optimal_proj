#!/usr/bin/env python3
n = int(input())

l = list(map(int, input().split()))
print(l)
if max(l) < sum(l)-max(l):
    print("Yes")
else:
    print("No")
