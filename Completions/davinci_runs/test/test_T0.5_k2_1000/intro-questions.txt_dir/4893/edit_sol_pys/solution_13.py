import sys

n, k = map(int, sys.stdin.readline().split())
distances = list(map(int, sys.stdin.readline().split()))

def find_max_dist(n, k, distances):
    max_dist = 0
    for i in range(n - k + 1):
        if distances[i + k - 1] - distances[i] > max_dist:
            max_dist = distances[i + k - 1] - distances[i]
    return max_dist

print(find_max_dist(n, k, distances))
