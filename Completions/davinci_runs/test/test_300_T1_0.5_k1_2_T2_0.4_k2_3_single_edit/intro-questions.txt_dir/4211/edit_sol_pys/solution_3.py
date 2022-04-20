

n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

ans = 10**10

for i in range(n-k+1):
    ans = min(ans, h[i+k-1]-h[i])

print(ans)
