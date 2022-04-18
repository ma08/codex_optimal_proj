

N, K, X, Y = map(int, input().split())

print(min(N, K) * X + max(0, N - K) * Y)
