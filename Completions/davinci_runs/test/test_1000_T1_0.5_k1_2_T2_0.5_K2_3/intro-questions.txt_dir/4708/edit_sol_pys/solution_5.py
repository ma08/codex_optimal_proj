
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

if N <= K:
    print(N * X)
else:
    print(K * X + (N - K) * Y)
