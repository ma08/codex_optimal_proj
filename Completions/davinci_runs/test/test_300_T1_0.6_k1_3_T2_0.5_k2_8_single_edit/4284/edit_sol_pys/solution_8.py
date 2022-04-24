
import sys

q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    k, n, a, b = map(int, sys.stdin.readline().rstrip().split())

    print(max(0, k - n * b))
