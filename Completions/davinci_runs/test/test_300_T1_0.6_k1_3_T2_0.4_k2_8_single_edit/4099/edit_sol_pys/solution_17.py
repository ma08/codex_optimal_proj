

# x = M * N - sum(Ai)

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

x = M * N - sum(A)

if x < 0:
    print(-1)
elif x > K:
    print(-1)
else:
    print(x)
