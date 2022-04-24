
import sys

q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    k, n, a, b = map(int, sys.stdin.readline().rstrip().split())

    if n * b > k:
        print(-1)
    else:
        print(k - n * b)
