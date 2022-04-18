
import sys

n, p = map(int, sys.stdin.readline().split())
distances = list(map(int, sys.stdin.readline().split()))
distances.sort()

if p == 1:
    print(1)
else:
    i = 0
    while i < n:
        if i + p - 1 < n:
            if distances[i] != distances[i + p - 1]:
                print(distances[i + p - 1])
                break
        i += 1
