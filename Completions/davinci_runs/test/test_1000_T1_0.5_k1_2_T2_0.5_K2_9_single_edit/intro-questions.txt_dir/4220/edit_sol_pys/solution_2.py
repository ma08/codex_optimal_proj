
from sys import stdin
k, m = map(int, stdin.readline().split())
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + m*".")
