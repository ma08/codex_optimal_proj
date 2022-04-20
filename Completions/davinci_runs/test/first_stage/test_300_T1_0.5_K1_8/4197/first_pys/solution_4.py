

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

B = [0] * n
for i in range(n):
    B[A[i] - 1] = i + 1

print(*B)