import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
X = int(sys.stdin.readline().rstrip())
Y = int(sys.stdin.readline().rstrip())

if N <= K:
    print(N * X)
elif N > K:
    print(K * X + (N - K) * Y)
