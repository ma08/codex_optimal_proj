

# N, M, K = map(int, input().split())
N, M, K = 2, 1, 3

if K <= N:
    print(K)
elif K <= N+M:
    print(N)
else:
    print(N - (K - N - M))
