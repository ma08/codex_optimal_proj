# https://codeforces.com/problemset/problem/158/A

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

if len(set(a)) == 1:
    print("YES")
else:
    print("NO")
