n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = [0]*(n+1)
for i in range(n):
    for j in range(m):
        ans[i+1] += a[i]*b[j]
print(*ans)
