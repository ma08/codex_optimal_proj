

# S = sum(Ai) + x
# x = M * N - S
import sys
input = sys.stdin.readline
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
x = M * N - S

if x < 0 or x > K:
    print(-1)
else:
    print(x)
