
n, k = map(int, input().split())
h = list(map(int, input().split()))

h = sorted(h)

ans = h[k-1] - h[0]

for i in range(n-k+1):
    if ans > h[i+k-1] - h[i]:
        ans = h[i+k-1] - h[i]

print(ans)
