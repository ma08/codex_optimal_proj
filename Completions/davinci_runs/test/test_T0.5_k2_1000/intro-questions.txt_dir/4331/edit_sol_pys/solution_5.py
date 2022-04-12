# coding: utf-8

N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    if i >= K:
        ans += 1
    else:
        ans += 0.5 ** (int(math.log2(K / i)) + 1)

print(ans / N)
