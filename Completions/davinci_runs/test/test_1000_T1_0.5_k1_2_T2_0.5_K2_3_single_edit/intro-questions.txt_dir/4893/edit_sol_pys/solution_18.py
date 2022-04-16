
import sys

n, m = map(int, sys.stdin.readline().split())
distances = sorted(map(int, sys.stdin.readline().split()), reverse=True)

i = 0
while i < n:
    if i + m - 1 < n:
        if distances[i] != distances[i + m - 1]:
            print(distances[i + m - 1])
            break
    i += 1
