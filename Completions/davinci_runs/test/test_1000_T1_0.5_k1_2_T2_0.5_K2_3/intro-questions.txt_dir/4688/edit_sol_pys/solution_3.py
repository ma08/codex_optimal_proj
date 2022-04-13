
N, K = map(int, input().split())

if N == 1:
    print(K)
elif N == 2:
    print(K * (K - 1))
else:
    print(K * (K - 1) ** (N - 1))
