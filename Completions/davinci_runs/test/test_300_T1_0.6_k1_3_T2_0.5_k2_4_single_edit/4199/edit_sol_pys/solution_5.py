

N, K = map(int, input().split()) # N, Kをそれぞれint型に変換して、スペース区切りで受け取る
h = list(map(int, input().split())) # hをint型のリストに変換して、スペース区切りで受け取る

ans = 0
for i in range(N):
    if h[i] >= K:
        ans += 1

print(ans)
