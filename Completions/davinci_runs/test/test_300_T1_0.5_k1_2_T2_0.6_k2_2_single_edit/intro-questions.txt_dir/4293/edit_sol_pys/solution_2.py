

N, K = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

ans = 100000000

for i in range(0, N-K+1):
    ans = min(ans, h[i+K-1]-h[i])

print(ans)
