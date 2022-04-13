n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    ans += a[i]
    ans -= a[n-1-i]
print(ans)
