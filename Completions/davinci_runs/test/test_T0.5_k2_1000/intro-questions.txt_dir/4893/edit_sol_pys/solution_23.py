import sys

n, p = map(int, sys.stdin.readline().strip().split())
distances = sorted(map(int, sys.stdin.readline().strip().split()))

if p == 1:
    print(distances[0])
else:
    for i in range(n - p + 1):
        if distances[i] != distances[i + p - 1]:
            print(distances[i + p - 1])
            break
