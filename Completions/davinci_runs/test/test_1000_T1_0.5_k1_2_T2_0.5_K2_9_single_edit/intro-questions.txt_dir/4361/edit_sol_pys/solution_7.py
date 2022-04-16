
n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()

ans = h[n-1] - h[0]
for i in range(n-k+1):
    ans = min(ans, h[i+k-1] - h[i])
print(ans)
