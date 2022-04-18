
import sys

n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))[:n]

print(sum(sorted(p)[:m]))
