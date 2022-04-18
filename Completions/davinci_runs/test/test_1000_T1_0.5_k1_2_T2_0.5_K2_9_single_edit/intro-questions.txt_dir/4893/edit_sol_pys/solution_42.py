
import sys

n, p = map(int, sys.stdin.readline().split())
distances = sorted(map(int, sys.stdin.readline().split()))

if p == 1:
    print(1)
else:
    i = 0
    if i + p - 1 < n:
        if distances[i] != distances[i + p - 1]:
            print(distances[i + p - 1])
