
N, K = map(int, input().split())

if N == 1 or N == 2:
    print(K ** N)
else:
    print(K * (K - 1) ** (N - 1))
