import sys

n, p = map(int, sys.stdin.readline().split())
distances = sorted(map(int, sys.stdin.readline().split()))

i = 0
while i < n:
    if i + p - 1 < n:
        if distances[i] != distances[i + p - 1]:
            print(distances[i + p - 1])
            break
    i += 1
