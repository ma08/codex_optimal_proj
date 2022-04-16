
import sys

n, k = map(int, sys.stdin.readline().split())
p = map(int, sys.stdin.readline().split())

print(sum(sorted(p)[:k]))
