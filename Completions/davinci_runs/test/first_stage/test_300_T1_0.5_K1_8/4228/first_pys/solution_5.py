

N, L = map(int, input().split())

print(sum(N * L - N * (N - 1) // 2))