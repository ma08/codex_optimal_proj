
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

ans = a[n-1] - a[0]
for i in range(n-k+1):
    ans = min(ans, a[i+k-1] - a[i])
print(ans)
