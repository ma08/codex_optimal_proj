
import sys

q = int(input())

for _ in range(q):
    k, n, a, b = map(int, input().split())

    if n * b > k:
        print(-1)
    else:
        print(k - n * b)
