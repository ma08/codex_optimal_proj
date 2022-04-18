import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
X = int(sys.stdin.readline().strip())
Y = int(sys.stdin.readline().strip())

if N <= K:
    print(N * X)
elif N > K:
    print(K * X + (N - K) * Y)
