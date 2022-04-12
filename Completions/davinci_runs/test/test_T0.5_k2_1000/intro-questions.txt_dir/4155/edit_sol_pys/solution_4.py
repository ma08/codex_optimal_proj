
N = int(input())
h = list(map(int, input().split()))

cnt = 0
for i in range(1, N):
    if h[i - 1] >= h[i]:
        cnt += h[i - 1] - h[i]
        h[i] = h[i - 1]

print(cnt)
