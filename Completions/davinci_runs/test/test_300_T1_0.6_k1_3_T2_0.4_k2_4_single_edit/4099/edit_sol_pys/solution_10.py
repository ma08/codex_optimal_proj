

# S = sum(Ai) + X
# X = M * N - S

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
X = M * N - S

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
