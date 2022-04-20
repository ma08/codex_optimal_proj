

# S = sum(Ai)
# x = M * N - S  # x = K - S

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
x = M * N - S  # x = K - S

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
