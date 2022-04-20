

N, K = map(int, input().split()) # N:個数, K:最低値
h = list(map(int, input().split())) # h:高さ

count = 0
for i in range(N):
    if h[i] >= K:
        count += 1

print(count)
