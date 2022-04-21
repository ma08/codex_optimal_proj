
# coding: utf-8
# Your code here!
a, b, k = map(int, input().split())
if a >= k:
    print(a - k, b)
else:
    print(0, max(0, b - (k - a)))
