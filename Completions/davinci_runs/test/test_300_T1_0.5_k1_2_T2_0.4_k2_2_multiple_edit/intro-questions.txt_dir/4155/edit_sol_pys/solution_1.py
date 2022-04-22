# coding: utf-8

N, K = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in range(N - K + 1):
    if h[i] < h[i + K - 1]:
        ans += h[i]
    else:
        ans += h[i + K - 1]
print(ans)
