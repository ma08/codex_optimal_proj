

import sys

with open("input.txt", "r") as f:
    n, w = map(int, f.readline().split())
    a = list(map(int, f.readline().split()))

    l = [0] * (n + 1)
    for i in range(1, n + 1):
        l[i] = l[i - 1] + a[i - 1]

print(r[w + l[n]])
