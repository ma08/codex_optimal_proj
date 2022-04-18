
N, K = map(int, input().split())
h = [int(i) for i in input().split()]
h.sort()
print(h)
d = [0] * N
for i in range(N):
    if i < K:
        d[i] = 0
    else:
        d[i] = h[i] - h[i - K]
print(min(d))
