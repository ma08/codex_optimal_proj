
N, K = map(int, input().split()) # N, Kを入力
h = list(map(int, input().split())) # hを入力

ans = 0
for i in range(N):
    if h[i] >= K:
        ans += 1

print(ans)
