# coding: utf-8

# get input
A, B, C = map(int, input().split())

# calculate
ans = min(abs(B - A) + abs(C - B), abs(C - A) + abs(B - C), abs(B - C) + abs(A - B))

# output
print(ans)
